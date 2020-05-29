# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ncbi_request.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NCBI_Request(object):
    def setupUi(self, NCBI_Request):
        NCBI_Request.setObjectName("NCBI_Request")
        NCBI_Request.resize(754, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(NCBI_Request)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_filters = QtWidgets.QVBoxLayout()
        self.layout_filters.setObjectName("layout_filters")
        self.layout_widget_0 = QtWidgets.QHBoxLayout()
        self.layout_widget_0.setObjectName("layout_widget_0")
        self.combobox_field_0 = QtWidgets.QComboBox(NCBI_Request)
        self.combobox_field_0.setObjectName("combobox_field_0")
        self.layout_widget_0.addWidget(self.combobox_field_0)
        self.edit_value_0 = QtWidgets.QLineEdit(NCBI_Request)
        self.edit_value_0.setObjectName("edit_value_0")
        self.layout_widget_0.addWidget(self.edit_value_0)
        self.button_remove_0 = QtWidgets.QToolButton(NCBI_Request)
        self.button_remove_0.setObjectName("button_remove_0")
        self.layout_widget_0.addWidget(self.button_remove_0)
        self.button_add = QtWidgets.QToolButton(NCBI_Request)
        self.button_add.setObjectName("button_add")
        self.layout_widget_0.addWidget(self.button_add)
        self.layout_filters.addLayout(self.layout_widget_0)
        self.verticalLayout.addLayout(self.layout_filters)
        self.button_create = QtWidgets.QPushButton(NCBI_Request)
        self.button_create.setObjectName("button_create")
        self.verticalLayout.addWidget(self.button_create)
        self.edit_request = QtWidgets.QLineEdit(NCBI_Request)
        self.edit_request.setObjectName("edit_request")
        self.verticalLayout.addWidget(self.edit_request)
        self.button_search = QtWidgets.QPushButton(NCBI_Request)
        self.button_search.setObjectName("button_search")
        self.verticalLayout.addWidget(self.button_search)
        spacerItem = QtWidgets.QSpacerItem(20, 146, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(NCBI_Request)
        self.button_add.clicked.connect(NCBI_Request.button_add_clicked)
        self.button_create.clicked.connect(NCBI_Request.button_create_clicked)
        self.button_search.clicked.connect(NCBI_Request.button_search_clicked)
        QtCore.QMetaObject.connectSlotsByName(NCBI_Request)

    def retranslateUi(self, NCBI_Request):
        _translate = QtCore.QCoreApplication.translate
        NCBI_Request.setWindowTitle(_translate("NCBI_Request", "Dialog"))
        self.button_remove_0.setText(_translate("NCBI_Request", "-"))
        self.button_add.setText(_translate("NCBI_Request", "+"))
        self.button_create.setText(_translate("NCBI_Request", "Créer la requête"))
        self.button_search.setText(_translate("NCBI_Request", "Rechercher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NCBI_Request = QtWidgets.QDialog()
    ui = Ui_NCBI_Request()
    ui.setupUi(NCBI_Request)
    NCBI_Request.show()
    sys.exit(app.exec_())
