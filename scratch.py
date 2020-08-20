from PyQt5 import QtCore, QtGui, QtWidgets


class UI(object):
    def setupUI(self, win):
        win.setObjectName("win")
        #width = QtWidgets.QDesktopWidget.screenGeometry()
        win.resize(1600, 900)
        win.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                           QtCore.Qt.WindowMaximizeButtonHint |
                           QtCore.Qt.WindowMinimizeButtonHint)
        # print(win.resizeEvent())

        # Label

        self.fname = QtWidgets.QLabel(win)
        self.fname.setGeometry(QtCore.QRect(40, 30, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.fname.setFont(font)

        self.Sname = QtWidgets.QLabel(win)
        self.Sname.setGeometry(QtCore.QRect(40, 70, 80, 30))

        self.email = QtWidgets.QLabel(win)
        self.email.setGeometry(QtCore.QRect(40, 110, 80, 30))

        self.number = QtWidgets.QLabel(win)
        self.number.setGeometry(QtCore.QRect(40, 150, 80, 30))

        self.major = QtWidgets.QLabel(win)
        self.major.setGeometry(QtCore.QRect(350, 30, 80, 30))

        self.gpa = QtWidgets.QLabel(win)
        self.gpa.setGeometry(QtCore.QRect(350, 70, 80, 30))

        self.interst = QtWidgets.QLabel(win)
        self.interst.setGeometry(QtCore.QRect(350, 110, 80, 30))

        self.gender = QtWidgets.QLabel(win)
        self.gender.setGeometry(QtCore.QRect(350, 150, 80, 30))

        self.retranslateUI(win)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUI(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "SCRATCH"))
        self.fname.setText(_translate("win", "First Name"))
        self.Sname.setText(_translate("win", "Second Name"))
        self.email.setText(_translate("win", "Email"))
        self.number.setText(_translate("win", "Number"))
        self.gpa.setText(_translate("win", "GPA"))
        self.major.setText(_translate("win", "Major"))
        self.gender.setText(_translate("win", "Gender"))
        self.interst.setText(_translate("win", "Interst"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QDialog()
    ui = UI()
    ui.setupUI(win)
    win.show()
    sys.exit(app.exec_())
