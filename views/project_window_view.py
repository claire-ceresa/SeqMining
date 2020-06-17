# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Project_Dialog(object):
    def setupUi(self, Project_Dialog):
        Project_Dialog.setObjectName("Project_Dialog")
        Project_Dialog.resize(252, 249)
        self.verticalLayout = QtWidgets.QVBoxLayout(Project_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scroll_area = QtWidgets.QScrollArea(Project_Dialog)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_projects = QtWidgets.QWidget()
        self.scroll_projects.setGeometry(QtCore.QRect(0, 0, 234, 202))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_projects.sizePolicy().hasHeightForWidth())
        self.scroll_projects.setSizePolicy(sizePolicy)
        self.scroll_projects.setObjectName("scroll_projects")
        self.scroll_area.setWidget(self.scroll_projects)
        self.verticalLayout.addWidget(self.scroll_area)
        self.button_add = QtWidgets.QPushButton(Project_Dialog)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)

        self.retranslateUi(Project_Dialog)
        self.button_add.clicked.connect(Project_Dialog.button_add_clicked)
        QtCore.QMetaObject.connectSlotsByName(Project_Dialog)

    def retranslateUi(self, Project_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Project_Dialog.setWindowTitle(_translate("Project_Dialog", "Dialog"))
        self.button_add.setText(_translate("Project_Dialog", "Ajouter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project_Dialog = QtWidgets.QDialog()
    ui = Ui_Project_Dialog()
    ui.setupUi(Project_Dialog)
    Project_Dialog.show()
    sys.exit(app.exec_())
