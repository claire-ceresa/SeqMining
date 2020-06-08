# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_excel_window(object):
    def setupUi(self, excel_window):
        excel_window.setObjectName("excel_window")
        excel_window.resize(427, 165)
        self.centralwidget = QtWidgets.QWidget(excel_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtWidgets.QToolButton(self.centralwidget)
        self.button_add.setArrowType(QtCore.Qt.NoArrow)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(1)
        self.table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.table.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table)
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setObjectName("button_export")
        self.verticalLayout.addWidget(self.button_export)
        self.label_created = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_created.setFont(font)
        self.label_created.setText("")
        self.label_created.setAlignment(QtCore.Qt.AlignCenter)
        self.label_created.setObjectName("label_created")
        self.verticalLayout.addWidget(self.label_created)
        excel_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(excel_window)
        self.button_add.clicked.connect(excel_window.button_add_clicked)
        self.button_export.clicked.connect(excel_window.button_export_clicked)
        QtCore.QMetaObject.connectSlotsByName(excel_window)

    def retranslateUi(self, excel_window):
        _translate = QtCore.QCoreApplication.translate
        excel_window.setWindowTitle(_translate("excel_window", "MainWindow"))
        self.button_add.setText(_translate("excel_window", "Ajouter une colonne"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("excel_window", "1"))
        self.button_export.setText(_translate("excel_window", "Exporter vers un fichier Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    excel_window = QtWidgets.QMainWindow()
    ui = Ui_excel_window()
    ui.setupUi(excel_window)
    excel_window.show()
    sys.exit(app.exec_())
