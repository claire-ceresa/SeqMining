# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_project_widget(object):
    def setupUi(self, project_widget):
        project_widget.setObjectName("project_widget")
        project_widget.resize(161, 71)
        self.gridLayout = QtWidgets.QGridLayout(project_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.deleting = QtWidgets.QLabel(project_widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.deleting.setFont(font)
        self.deleting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleting.setStyleSheet("color: rgb(11, 0, 168);")
        self.deleting.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deleting.setObjectName("deleting")
        self.gridLayout.addWidget(self.deleting, 1, 1, 1, 1)
        self.modif = QtWidgets.QLabel(project_widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.modif.setFont(font)
        self.modif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modif.setStyleSheet("color: rgb(11, 0, 168);")
        self.modif.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.modif.setObjectName("modif")
        self.gridLayout.addWidget(self.modif, 0, 1, 1, 1)
        self.name = QtWidgets.QWidget(project_widget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.comment = QtWidgets.QWidget(project_widget)
        self.comment.setObjectName("comment")
        self.gridLayout.addWidget(self.comment, 1, 0, 1, 1)

        self.retranslateUi(project_widget)
        QtCore.QMetaObject.connectSlotsByName(project_widget)

    def retranslateUi(self, project_widget):
        _translate = QtCore.QCoreApplication.translate
        project_widget.setWindowTitle(_translate("project_widget", "Form"))
        self.deleting.setText(_translate("project_widget", "Supprimer"))
        self.modif.setText(_translate("project_widget", "Modifier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    project_widget = QtWidgets.QWidget()
    ui = Ui_project_widget()
    ui.setupUi(project_widget)
    project_widget.show()
    sys.exit(app.exec_())
