# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ncbi_result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NCBI_Result(object):
    def setupUi(self, NCBI_Result):
        NCBI_Result.setObjectName("NCBI_Result")
        NCBI_Result.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NCBI_Result)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.edit_request = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_request.setObjectName("edit_request")
        self.horizontal_layout.addWidget(self.edit_request)
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setObjectName("button_search")
        self.horizontal_layout.addWidget(self.button_search)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_help = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_help.setFont(font)
        self.label_help.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_help.setObjectName("label_help")
        self.horizontalLayout_2.addWidget(self.label_help)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_selectall = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_selectall.setFont(font)
        self.label_selectall.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_selectall.setObjectName("label_selectall")
        self.horizontalLayout.addWidget(self.label_selectall)
        self.label_deselectall = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_deselectall.setFont(font)
        self.label_deselectall.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_deselectall.setObjectName("label_deselectall")
        self.horizontalLayout.addWidget(self.label_deselectall)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setShowGrid(False)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table)
        NCBI_Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(NCBI_Result)
        self.button_search.clicked.connect(NCBI_Result.button_search_clicked)
        QtCore.QMetaObject.connectSlotsByName(NCBI_Result)

    def retranslateUi(self, NCBI_Result):
        _translate = QtCore.QCoreApplication.translate
        NCBI_Result.setWindowTitle(_translate("NCBI_Result", "MainWindow"))
        self.button_search.setText(_translate("NCBI_Result", "Rechercher"))
        self.label_help.setText(_translate("NCBI_Result", "Aide à la construction de la requête"))
        self.label_selectall.setText(_translate("NCBI_Result", "Tout sélectionner"))
        self.label_deselectall.setText(_translate("NCBI_Result", "Tout désélectionner"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("NCBI_Result", "Accession"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("NCBI_Result", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NCBI_Result = QtWidgets.QMainWindow()
    ui = Ui_NCBI_Result()
    ui.setupUi(NCBI_Result)
    NCBI_Result.show()
    sys.exit(app.exec_())
