# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(900, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acc_frame = QtWidgets.QFrame(self.frame)
        self.acc_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.acc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.acc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.acc_frame.setObjectName("acc_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.acc_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.acc_frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.linear_acc_x_label = QtWidgets.QLabel(self.acc_frame)
        self.linear_acc_x_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_x_label.setObjectName("linear_acc_x_label")
        self.gridLayout.addWidget(self.linear_acc_x_label, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.acc_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.linear_acc_y_label = QtWidgets.QLabel(self.acc_frame)
        self.linear_acc_y_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_y_label.setObjectName("linear_acc_y_label")
        self.gridLayout.addWidget(self.linear_acc_y_label, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.acc_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.linear_acc_z_label = QtWidgets.QLabel(self.acc_frame)
        self.linear_acc_z_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_z_label.setObjectName("linear_acc_z_label")
        self.gridLayout.addWidget(self.linear_acc_z_label, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.acc_frame)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addWidget(self.acc_frame)
        self.acc_max_frame = QtWidgets.QFrame(self.frame)
        self.acc_max_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.acc_max_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.acc_max_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.acc_max_frame.setObjectName("acc_max_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.acc_max_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.acc_max_frame)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.acc_max_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.linear_acc_x_max_label = QtWidgets.QLabel(self.acc_max_frame)
        self.linear_acc_x_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_x_max_label.setObjectName("linear_acc_x_max_label")
        self.gridLayout_3.addWidget(self.linear_acc_x_max_label, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.acc_max_frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.linear_acc_y_max_label = QtWidgets.QLabel(self.acc_max_frame)
        self.linear_acc_y_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_y_max_label.setObjectName("linear_acc_y_max_label")
        self.gridLayout_3.addWidget(self.linear_acc_y_max_label, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.acc_max_frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.linear_acc_z_max_label = QtWidgets.QLabel(self.acc_max_frame)
        self.linear_acc_z_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_z_max_label.setObjectName("linear_acc_z_max_label")
        self.gridLayout_3.addWidget(self.linear_acc_z_max_label, 3, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.horizontalLayout.addWidget(self.acc_max_frame)
        self.acc_min_frame = QtWidgets.QFrame(self.frame)
        self.acc_min_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.acc_min_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.acc_min_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.acc_min_frame.setObjectName("acc_min_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.acc_min_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.acc_min_frame)
        self.label_16.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.acc_min_frame)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)
        self.linear_acc_x_min_label = QtWidgets.QLabel(self.acc_min_frame)
        self.linear_acc_x_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_x_min_label.setObjectName("linear_acc_x_min_label")
        self.gridLayout_4.addWidget(self.linear_acc_x_min_label, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.acc_min_frame)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)
        self.linear_acc_y_min_label = QtWidgets.QLabel(self.acc_min_frame)
        self.linear_acc_y_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_y_min_label.setObjectName("linear_acc_y_min_label")
        self.gridLayout_4.addWidget(self.linear_acc_y_min_label, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.acc_min_frame)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 3, 0, 1, 1)
        self.linear_acc_z_min_label = QtWidgets.QLabel(self.acc_min_frame)
        self.linear_acc_z_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linear_acc_z_min_label.setObjectName("linear_acc_z_min_label")
        self.gridLayout_4.addWidget(self.linear_acc_z_min_label, 3, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.horizontalLayout.addWidget(self.acc_min_frame)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(900, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vel_frame = QtWidgets.QFrame(self.frame_3)
        self.vel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vel_frame.setObjectName("vel_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.vel_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.vel_frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.angular_vel_x_label = QtWidgets.QLabel(self.vel_frame)
        self.angular_vel_x_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_x_label.setObjectName("angular_vel_x_label")
        self.gridLayout_2.addWidget(self.angular_vel_x_label, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.vel_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.angular_vel_y_label = QtWidgets.QLabel(self.vel_frame)
        self.angular_vel_y_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_y_label.setObjectName("angular_vel_y_label")
        self.gridLayout_2.addWidget(self.angular_vel_y_label, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.vel_frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.angular_vel_z_label = QtWidgets.QLabel(self.vel_frame)
        self.angular_vel_z_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_z_label.setObjectName("angular_vel_z_label")
        self.gridLayout_2.addWidget(self.angular_vel_z_label, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.vel_frame)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.vel_frame)
        self.vel_max_frame = QtWidgets.QFrame(self.frame_3)
        self.vel_max_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vel_max_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vel_max_frame.setObjectName("vel_max_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.vel_max_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_25 = QtWidgets.QLabel(self.vel_max_frame)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)
        self.angular_vel_x_max_label = QtWidgets.QLabel(self.vel_max_frame)
        self.angular_vel_x_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_x_max_label.setObjectName("angular_vel_x_max_label")
        self.gridLayout_5.addWidget(self.angular_vel_x_max_label, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.vel_max_frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 2, 0, 1, 1)
        self.angular_vel_y_max_label = QtWidgets.QLabel(self.vel_max_frame)
        self.angular_vel_y_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_y_max_label.setObjectName("angular_vel_y_max_label")
        self.gridLayout_5.addWidget(self.angular_vel_y_max_label, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.vel_max_frame)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 3, 0, 1, 1)
        self.angular_vel_z_max_label = QtWidgets.QLabel(self.vel_max_frame)
        self.angular_vel_z_max_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_z_max_label.setObjectName("angular_vel_z_max_label")
        self.gridLayout_5.addWidget(self.angular_vel_z_max_label, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.vel_max_frame)
        self.label_23.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 2)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.vel_max_frame)
        self.vel_min_frame = QtWidgets.QFrame(self.frame_3)
        self.vel_min_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vel_min_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vel_min_frame.setObjectName("vel_min_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.vel_min_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_31 = QtWidgets.QLabel(self.vel_min_frame)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 1, 0, 1, 1)
        self.angular_vel_x_min_label = QtWidgets.QLabel(self.vel_min_frame)
        self.angular_vel_x_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_x_min_label.setObjectName("angular_vel_x_min_label")
        self.gridLayout_6.addWidget(self.angular_vel_x_min_label, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.vel_min_frame)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 2, 0, 1, 1)
        self.angular_vel_y_min_label = QtWidgets.QLabel(self.vel_min_frame)
        self.angular_vel_y_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_y_min_label.setObjectName("angular_vel_y_min_label")
        self.gridLayout_6.addWidget(self.angular_vel_y_min_label, 2, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.vel_min_frame)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 3, 0, 1, 1)
        self.angular_vel_z_min_label = QtWidgets.QLabel(self.vel_min_frame)
        self.angular_vel_z_min_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.angular_vel_z_min_label.setObjectName("angular_vel_z_min_label")
        self.gridLayout_6.addWidget(self.angular_vel_z_min_label, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.vel_min_frame)
        self.label_24.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 0, 0, 1, 2)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.vel_min_frame)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 4, 0, 1, 1)
        self.X_angle_label = QtWidgets.QLabel(self.frame_4)
        self.X_angle_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.X_angle_label.setObjectName("X_angle_label")
        self.gridLayout_7.addWidget(self.X_angle_label, 1, 1, 1, 1)
        self.Z_angle_label = QtWidgets.QLabel(self.frame_4)
        self.Z_angle_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.Z_angle_label.setObjectName("Z_angle_label")
        self.gridLayout_7.addWidget(self.Z_angle_label, 4, 1, 1, 1)
        self.Y_angle_label = QtWidgets.QLabel(self.frame_4)
        self.Y_angle_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.Y_angle_label.setObjectName("Y_angle_label")
        self.gridLayout_7.addWidget(self.Y_angle_label, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setMaximumSize(QtCore.QSize(100, 100))
        self.label_13.setText("")
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setPixmap(QtGui.QPixmap(":/Images/src/x_transfor.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setMaximumSize(QtCore.QSize(100, 100))
        self.label_14.setText("")
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setPixmap(QtGui.QPixmap(":/Images/src/y_transfor.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.label_28 = QtWidgets.QLabel(self.frame_5)
        self.label_28.setMaximumSize(QtCore.QSize(100, 100))
        self.label_28.setText("")
        self.label_28.setTextFormat(QtCore.Qt.RichText)
        self.label_28.setPixmap(QtGui.QPixmap(":/Images/src/z_transfor.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Imu Test"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.linear_acc_x_label.setText(_translate("MainWindow", "0.0"))
        self.label_3.setText(_translate("MainWindow", "Y:"))
        self.linear_acc_y_label.setText(_translate("MainWindow", "0.0"))
        self.label_5.setText(_translate("MainWindow", "Z:"))
        self.linear_acc_z_label.setText(_translate("MainWindow", "0.0"))
        self.label_7.setText(_translate("MainWindow", "Akcelerometr"))
        self.label_2.setText(_translate("MainWindow", "Acc Max"))
        self.label_6.setText(_translate("MainWindow", "X:"))
        self.linear_acc_x_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_11.setText(_translate("MainWindow", "Y:"))
        self.linear_acc_y_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_12.setText(_translate("MainWindow", "Z:"))
        self.linear_acc_z_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_16.setText(_translate("MainWindow", "Acc Min"))
        self.label_17.setText(_translate("MainWindow", "X:"))
        self.linear_acc_x_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_18.setText(_translate("MainWindow", "Y:"))
        self.linear_acc_y_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_19.setText(_translate("MainWindow", "Z:"))
        self.linear_acc_z_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_8.setText(_translate("MainWindow", "X:"))
        self.angular_vel_x_label.setText(_translate("MainWindow", "0.0"))
        self.label_9.setText(_translate("MainWindow", "Y:"))
        self.angular_vel_y_label.setText(_translate("MainWindow", "0.0"))
        self.label_10.setText(_translate("MainWindow", "Z:"))
        self.angular_vel_z_label.setText(_translate("MainWindow", "0.0"))
        self.label_4.setText(_translate("MainWindow", "Żyroskop"))
        self.label_25.setText(_translate("MainWindow", "X:"))
        self.angular_vel_x_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_26.setText(_translate("MainWindow", "Y:"))
        self.angular_vel_y_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_27.setText(_translate("MainWindow", "Z:"))
        self.angular_vel_z_max_label.setText(_translate("MainWindow", "0.0"))
        self.label_23.setText(_translate("MainWindow", "Vel Max"))
        self.label_31.setText(_translate("MainWindow", "X:"))
        self.angular_vel_x_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_32.setText(_translate("MainWindow", "Y:"))
        self.angular_vel_y_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_33.setText(_translate("MainWindow", "Z:"))
        self.angular_vel_z_min_label.setText(_translate("MainWindow", "0.0"))
        self.label_24.setText(_translate("MainWindow", "Vel Min"))
        self.label_20.setText(_translate("MainWindow", "X:"))
        self.label_15.setText(_translate("MainWindow", "Pozycja"))
        self.label_22.setText(_translate("MainWindow", "Z:"))
        self.X_angle_label.setText(_translate("MainWindow", "00"))
        self.Z_angle_label.setText(_translate("MainWindow", "00"))
        self.Y_angle_label.setText(_translate("MainWindow", "00"))
        self.label_21.setText(_translate("MainWindow", "Y:"))
import resources_rc
