import sys
from PyQt5 import QtWidgets
import rclpy
from sensor_msgs.msg import Imu
from rclpy.node import Node
from threading import Thread
from datetime import datetime, timedelta

from MainWindow import Ui_MainWindow

class ImuSubscriber(Node):
    def __init__(self, main_window):
        super().__init__('imu_subscriber')
        self.main_window = main_window
        self.data_lists = {
            'linear_acc_x': [],
            'linear_acc_y': [],
            'linear_acc_z': [],
            'angular_vel_x': [],
            'angular_vel_y': [],
            'angular_vel_z': []
        }
        self.last_updated_time = datetime.now()

        self.subscription = self.create_subscription(
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
            self.data_lists[key] = [(val, time) for val, time in self.data_lists[key] if datetime.now() - time <= timedelta(seconds=3)]

            max_value = max(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]
            min_value = min(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]

            getattr(self.main_window, f"{key}_label").setText(str(value))
            getattr(self.main_window, f"{key}_max_label").setText(str(max_value))
            getattr(self.main_window, f"{key}_min_label").setText(str(min_value))

        if datetime.now() - self.last_updated_time > timedelta(seconds=3):
            self.last_updated_time = datetime.now()
            for key, value in data.items():
                max_value = max(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]
                min_value = min(self.data_lists[key], key=lambda x: x[0], default=(0, None))[0]

                getattr(self.main_window, f"{key}_max_label").setText(str(max_value))
                getattr(self.main_window, f"{key}_min_label").setText(str(min_value))

        print(f'Akcelerometr: x={linear_acceleration.x}, y={linear_acceleration.y}, z={linear_acceleration.z}')
        print(f'Żyroskop: x={angular_velocity.x}, y={angular_velocity.y}, z={angular_velocity.z}')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Inicjalizacja węzła ROS 2
        rclpy.init()
        self.imu_subscriber = ImuSubscriber(self)

        # Uruchamianie pętli zdarzeń ROS 2 w oddzielnym wątku
        self.spin_thread = Thread(target=rclpy.spin, args=(self.imu_subscriber,))
        self.spin_thread.start()

    def closeEvent(self, event):
        # Wywołanie destroy_node i shutdown podczas zamykania aplikacji
        self.imu_subscriber.destroy_node()
        rclpy.shutdown()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
