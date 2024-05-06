import sys
from PyQt5 import QtWidgets, QtCore
import rclpy
import math
from sensor_msgs.msg import Imu
from rclpy.node import Node
from threading import Thread
from datetime import datetime, timedelta

from MainWindow import Ui_MainWindow

class ImuSubscriber(QtCore.QObject):
    imu_data_signal = QtCore.pyqtSignal(dict)

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.data_lists = {
            'linear_acc_x': [],
            'linear_acc_y': [],
            'linear_acc_z': [],
            'angular_vel_x': [],
            'angular_vel_y': [],
            'angular_vel_z': [],
            'acc_angle_z': []
        }
        self.last_updated_time = datetime.now()
        self.vel_angle_x = 0.0
        self.vel_angle_y = 0.0
        self.vel_angle_z = 0.0
        self.vel_last_angle_x = 0.0
        self.vel_last_angle_y = 0.0
        self.vel_last_angle_z = 0.0

        self.acc_angle_x = 0.0
        self.acc_angle_y = 0.0
        self.acc_angle_z = 0.0

    def initialize_node(self):
        self.node = Node('imu_subscriber')
        self.subscription = self.node.create_subscription(
            Imu,
            '/imu_plugin/out',
            self.imu_callback,
            10
        )

    def imu_callback(self, msg):
        linear_acceleration = msg.linear_acceleration
        angular_velocity = msg.angular_velocity

        data = {
            'linear_acc_x': linear_acceleration.x,
            'linear_acc_y': linear_acceleration.y,
            'linear_acc_z': linear_acceleration.z,
            'angular_vel_x': angular_velocity.x,
            'angular_vel_y': angular_velocity.y,
            'angular_vel_z': angular_velocity.z
        }

        for key, value in data.items():
            self.data_lists[key].append((value, datetime.now()))
            self.data_lists[key] = [(val, time) for val, time in self.data_lists[key] if datetime.now() - time <= timedelta(seconds=1)]

        # Dodawanie wartości acc_angle_z do listy
        self.data_lists['acc_angle_z'].append((self.acc_angle_z, datetime.now()))
        self.data_lists['acc_angle_z'] = [(val, time) for val, time in self.data_lists['acc_angle_z'] if datetime.now() - time <= timedelta(seconds=3)]

        self.imu_data_signal.emit(data)

        if datetime.now() - self.last_updated_time > timedelta(seconds=1):
            self.last_updated_time = datetime.now()
            for key, value in data.items():
                max_value = max(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]
                min_value = min(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]

                getattr(self.main_window, f"{key}_max_label").setText(str(max_value))
                getattr(self.main_window, f"{key}_min_label").setText(str(min_value))

            # Obliczanie średniej arytmetycznej wartości acc_angle_z
            avg_acc_angle_z = sum(val[0] for val in self.data_lists['acc_angle_z']) / len(self.data_lists['acc_angle_z'])
            self.main_window.acc_z_avg_angle_label.setText(f"{avg_acc_angle_z:.2f}°")


        # Obliczanie kąta pochylenia
        dt = (datetime.now() - self.last_updated_time).total_seconds()
        self.vel_angle_x += (self.vel_last_angle_x + data['angular_vel_x'] * dt) * dt / 2
        self.vel_last_angle_x = data['angular_vel_x']
        self.vel_angle_y += (self.vel_last_angle_y + data['angular_vel_y'] * dt) * dt / 2
        self.vel_last_angle_y = data['angular_vel_y']
        self.vel_angle_z += (self.vel_last_angle_z + data['angular_vel_z'] * dt) * dt / 2
        self.vel_last_angle_z = data['angular_vel_z']


        self.acc_angle_x = math.degrees(math.atan2(linear_acceleration.y, linear_acceleration.z))
        self.acc_angle_y = math.degrees(math.atan2(-linear_acceleration.x, linear_acceleration.z))
        self.acc_angle_z = math.degrees(math.atan2(linear_acceleration.x, linear_acceleration.y))


        self.main_window.vel_x_angle_label.setText(f"{self.vel_angle_x:.2f}°")
        self.main_window.vel_y_angle_label.setText(f"{self.vel_angle_y:.2f}°")
        self.main_window.vel_z_angle_label.setText(f"{self.vel_angle_z:.2f}°")

        self.main_window.acc_x_angle_label.setText(f"{self.acc_angle_x:.2f}°")
        self.main_window.acc_y_angle_label.setText(f"{self.acc_angle_y:.2f}°")
        self.main_window.acc_z_angle_label.setText(f"{self.acc_angle_z:.2f}°")


    def close_node(self):
        self.node.destroy_node()
        rclpy.shutdown()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Inicjalizacja węzła ROS 2
        rclpy.init()
        self.imu_subscriber = ImuSubscriber(self)
        self.imu_subscriber.initialize_node()

        # Uruchamianie pętli zdarzeń ROS 2 w oddzielnym wątku
        self.spin_thread = Thread(target=rclpy.spin, args=(self.imu_subscriber.node,))
        self.spin_thread.start()

        # Połączenie sygnału z wątku IMU z odpowiednimi slotami aktualizacji interfejsu użytkownika
        self.imu_subscriber.imu_data_signal.connect(self.update_ui)

    def update_ui(self, data):
        for key, value in data.items():
            max_value = max(self.imu_subscriber.data_lists[key], key=lambda x: x[0], default=(0, None))[0]
            min_value = min(self.imu_subscriber.data_lists[key], key=lambda x: x[0], default=(0, None))[0]

            getattr(self, f"{key}_label").setText(str(value))
            getattr(self, f"{key}_max_label").setText(str(max_value))
            getattr(self, f"{key}_min_label").setText(str(min_value))

    def closeEvent(self, event):
        # Wywołanie destroy_node i shutdown podczas zamykania aplikacji
        self.imu_subscriber.close_node()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
