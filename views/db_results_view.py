# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_results.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_db_results(object):
    def setupUi(self, db_results):
        db_results.setObjectName("db_results")
        db_results.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(db_results)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_result = QtWidgets.QTableWidget(self.centralwidget)
        self.table_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_result.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_result.setObjectName("table_result")
        self.table_result.setColumnCount(2)
        self.table_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(1, item)
        self.table_result.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table_result)
        db_results.setCentralWidget(self.centralwidget)

        self.retranslateUi(db_results)
        self.table_result.cellDoubleClicked['int','int'].connect(db_results.table_result_clicked)
        QtCore.QMetaObject.connectSlotsByName(db_results)

    def retranslateUi(self, db_results):
        _translate = QtCore.QCoreApplication.translate
        db_results.setWindowTitle(_translate("db_results", "MainWindow"))
        item = self.table_result.horizontalHeaderItem(0)
        item.setText(_translate("db_results", "Identifiant"))
        item = self.table_result.horizontalHeaderItem(1)
        item.setText(_translate("db_results", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_results = QtWidgets.QMainWindow()
    ui = Ui_db_results()
    ui.setupUi(db_results)
    db_results.show()
    sys.exit(app.exec_())
