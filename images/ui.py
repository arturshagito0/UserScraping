# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LinledInScraper(object):
    def setupUi(self, LinledInScraper):
        LinledInScraper.setObjectName("LinledInScraper")
        LinledInScraper.resize(1125, 818)
        LinledInScraper.setAutoFillBackground(False)
        LinledInScraper.setStyleSheet("\n"
"background-color:rgb(27, 27, 27);")
        LinledInScraper.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(LinledInScraper)
        self.frame.setGeometry(QtCore.QRect(10, 0, 311, 821))
        self.frame.setStyleSheet("background-color:rgb(10, 10, 10);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 295, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(11, 0, 57, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    image: url(:/add_button/add_pressed.svg);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"image: url(:/add_button/add_default.svg);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 10, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(30, 140, 256, 192))
        self.listView.setObjectName("listView")
        self.frame_2 = QtWidgets.QFrame(LinledInScraper)
        self.frame_2.setGeometry(QtCore.QRect(330, 0, 791, 811))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(LinledInScraper)
        QtCore.QMetaObject.connectSlotsByName(LinledInScraper)

    def retranslateUi(self, LinledInScraper):
        _translate = QtCore.QCoreApplication.translate
        LinledInScraper.setWindowTitle(_translate("LinledInScraper", "LinkedInScraper"))
        self.label.setText(_translate("LinledInScraper", "<html><head/><body><p><span style=\" color:#ffffff;\">Create new request</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinledInScraper = QtWidgets.QDialog()
    ui = Ui_LinledInScraper()
    ui.setupUi(LinledInScraper)
    LinledInScraper.show()
    sys.exit(app.exec_())
