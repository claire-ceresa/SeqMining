# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_download.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_db_download(object):
    def setupUi(self, db_download):
        db_download.setObjectName("db_download")
        db_download.resize(400, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(db_download)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_result = QtWidgets.QLabel(db_download)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.table_error = QtWidgets.QTableWidget(db_download)
        self.table_error.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_error.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_error.setShowGrid(False)
        self.table_error.setGridStyle(QtCore.Qt.NoPen)
        self.table_error.setObjectName("table_error")
        self.table_error.setColumnCount(2)
        self.table_error.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_error.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_error.setHorizontalHeaderItem(1, item)
        self.table_error.horizontalHeader().setVisible(False)
        self.table_error.horizontalHeader().setStretchLastSection(True)
        self.table_error.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_error)

        self.retranslateUi(db_download)
        QtCore.QMetaObject.connectSlotsByName(db_download)

    def retranslateUi(self, db_download):
        _translate = QtCore.QCoreApplication.translate
        db_download.setWindowTitle(_translate("db_download", "Dialog"))
        item = self.table_error.horizontalHeaderItem(0)
        item.setText(_translate("db_download", "Id"))
        item = self.table_error.horizontalHeaderItem(1)
        item.setText(_translate("db_download", "Error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_download = QtWidgets.QDialog()
    ui = Ui_db_download()
    ui.setupUi(db_download)
    db_download.show()
    sys.exit(app.exec_())
