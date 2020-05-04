# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layout_filters = QtWidgets.QVBoxLayout()
        self.layout_filters.setObjectName("layout_filters")
        self.layout_widget_0 = QtWidgets.QHBoxLayout()
        self.layout_widget_0.setObjectName("layout_widget_0")
        self.combobox_field_0 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_field_0.setObjectName("combobox_field_0")
        self.layout_widget_0.addWidget(self.combobox_field_0)
        self.edit_value_0 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_value_0.setObjectName("edit_value_0")
        self.layout_widget_0.addWidget(self.edit_value_0)
        self.button_remove_0 = QtWidgets.QToolButton(self.centralwidget)
        self.button_remove_0.setObjectName("button_remove_0")
        self.layout_widget_0.addWidget(self.button_remove_0)
        self.button_add = QtWidgets.QToolButton(self.centralwidget)
        self.button_add.setObjectName("button_add")
        self.layout_widget_0.addWidget(self.button_add)
        self.layout_filters.addLayout(self.layout_widget_0)
        self.verticalLayout.addLayout(self.layout_filters)
        self.button_create = QtWidgets.QPushButton(self.centralwidget)
        self.button_create.setObjectName("button_create")
        self.verticalLayout.addWidget(self.button_create)
        self.edit_request = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_request.setObjectName("edit_request")
        self.verticalLayout.addWidget(self.edit_request)
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setObjectName("button_search")
        self.verticalLayout.addWidget(self.button_search)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_add.clicked.connect(MainWindow.button_add_clicked)
        self.button_create.clicked.connect(MainWindow.button_create_clicked)
        self.button_search.clicked.connect(MainWindow.button_search_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Construire la requete"))
        self.button_remove_0.setText(_translate("MainWindow", "-"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_create.setText(_translate("MainWindow", "Créer la requête"))
        self.button_search.setText(_translate("MainWindow", "Rechercher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
