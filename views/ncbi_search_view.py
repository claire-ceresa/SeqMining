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
        NCBI_Result.resize(681, 631)
        self.centralwidget = QtWidgets.QWidget(NCBI_Result)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupbox_id = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_id.setObjectName("groupbox_id")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupbox_id)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_id = QtWidgets.QHBoxLayout()
        self.layout_id.setObjectName("layout_id")
        self.label = QtWidgets.QLabel(self.groupbox_id)
        self.label.setObjectName("label")
        self.layout_id.addWidget(self.label)
        self.edit_id = QtWidgets.QLineEdit(self.groupbox_id)
        self.edit_id.setObjectName("edit_id")
        self.layout_id.addWidget(self.edit_id)
        self.button_search_id = QtWidgets.QPushButton(self.groupbox_id)
        self.button_search_id.setObjectName("button_search_id")
        self.layout_id.addWidget(self.button_search_id)
        self.verticalLayout_2.addLayout(self.layout_id)
        self.verticalLayout_4.addWidget(self.groupbox_id)
        self.groupbox_products = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_products.setObjectName("groupbox_products")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_products)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout_request = QtWidgets.QHBoxLayout()
        self.layout_request.setObjectName("layout_request")
        self.edit_request = QtWidgets.QLineEdit(self.groupbox_products)
        self.edit_request.setObjectName("edit_request")
        self.layout_request.addWidget(self.edit_request)
        self.button_search_request = QtWidgets.QPushButton(self.groupbox_products)
        self.button_search_request.setObjectName("button_search_request")
        self.layout_request.addWidget(self.button_search_request)
        self.verticalLayout_3.addLayout(self.layout_request)
        self.layout_help = QtWidgets.QHBoxLayout()
        self.layout_help.setObjectName("layout_help")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_help.addItem(spacerItem)
        self.label_help = QtWidgets.QLabel(self.groupbox_products)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_help.setFont(font)
        self.label_help.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_help.setObjectName("label_help")
        self.layout_help.addWidget(self.label_help)
        self.verticalLayout_3.addLayout(self.layout_help)
        self.groupbox_results = QtWidgets.QGroupBox(self.groupbox_products)
        self.groupbox_results.setTitle("")
        self.groupbox_results.setFlat(True)
        self.groupbox_results.setObjectName("groupbox_results")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox_results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_result = QtWidgets.QLabel(self.groupbox_results)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.layout_select = QtWidgets.QHBoxLayout()
        self.layout_select.setObjectName("layout_select")
        self.label_selectall = QtWidgets.QLabel(self.groupbox_results)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_selectall.setFont(font)
        self.label_selectall.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_selectall.setObjectName("label_selectall")
        self.layout_select.addWidget(self.label_selectall)
        self.label_deselectall = QtWidgets.QLabel(self.groupbox_results)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_deselectall.setFont(font)
        self.label_deselectall.setStyleSheet("color: rgb(11, 0, 168);")
        self.label_deselectall.setObjectName("label_deselectall")
        self.layout_select.addWidget(self.label_deselectall)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_select.addItem(spacerItem1)
        self.label_nb = QtWidgets.QLabel(self.groupbox_results)
        self.label_nb.setObjectName("label_nb")
        self.layout_select.addWidget(self.label_nb)
        self.combobox_nb = QtWidgets.QComboBox(self.groupbox_results)
        self.combobox_nb.setMinimumSize(QtCore.QSize(41, 22))
        self.combobox_nb.setMaximumSize(QtCore.QSize(41, 22))
        self.combobox_nb.setObjectName("combobox_nb")
        self.combobox_nb.addItem("")
        self.combobox_nb.addItem("")
        self.combobox_nb.addItem("")
        self.combobox_nb.addItem("")
        self.layout_select.addWidget(self.combobox_nb)
        self.verticalLayout.addLayout(self.layout_select)
        self.label_error = QtWidgets.QLabel(self.groupbox_results)
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.verticalLayout.addWidget(self.label_error)
        self.table = QtWidgets.QTableWidget(self.groupbox_results)
        self.table.setMinimumSize(QtCore.QSize(0, 283))
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        self.layout_page = QtWidgets.QHBoxLayout()
        self.layout_page.setObjectName("layout_page")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_page.addItem(spacerItem2)
        self.label_page = QtWidgets.QLabel(self.groupbox_results)
        self.label_page.setObjectName("label_page")
        self.layout_page.addWidget(self.label_page)
        self.combobox_page = QtWidgets.QComboBox(self.groupbox_results)
        self.combobox_page.setMaximumSize(QtCore.QSize(50, 22))
        self.combobox_page.setObjectName("combobox_page")
        self.layout_page.addWidget(self.combobox_page)
        self.label_on = QtWidgets.QLabel(self.groupbox_results)
        self.label_on.setText("")
        self.label_on.setObjectName("label_on")
        self.layout_page.addWidget(self.label_on)
        self.verticalLayout.addLayout(self.layout_page)
        self.button_extract = QtWidgets.QPushButton(self.groupbox_results)
        self.button_extract.setObjectName("button_extract")
        self.verticalLayout.addWidget(self.button_extract)
        self.button_download = QtWidgets.QPushButton(self.groupbox_results)
        self.button_download.setObjectName("button_download")
        self.verticalLayout.addWidget(self.button_download)
        self.verticalLayout_3.addWidget(self.groupbox_results)
        self.verticalLayout_4.addWidget(self.groupbox_products)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        NCBI_Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(NCBI_Result)
        self.button_search_request.clicked.connect(NCBI_Result.button_search_request_clicked)
        self.table.cellDoubleClicked['int','int'].connect(NCBI_Result.row_table_clicked)
        self.button_search_id.clicked.connect(NCBI_Result.button_search_id_clicked)
        self.combobox_nb.currentTextChanged['QString'].connect(NCBI_Result.combobox_nb_changed)
        self.combobox_page.activated['int'].connect(NCBI_Result.combobox_page_changed)
        self.button_extract.clicked.connect(NCBI_Result.button_extract_clicked)
        self.button_download.clicked.connect(NCBI_Result.button_download_clicked)
        QtCore.QMetaObject.connectSlotsByName(NCBI_Result)

    def retranslateUi(self, NCBI_Result):
        _translate = QtCore.QCoreApplication.translate
        NCBI_Result.setWindowTitle(_translate("NCBI_Result", "MainWindow"))
        self.groupbox_id.setTitle(_translate("NCBI_Result", "Rechercher un produit par son identifiant"))
        self.label.setText(_translate("NCBI_Result", "Identifiant GenBank"))
        self.button_search_id.setText(_translate("NCBI_Result", "Rechercher"))
        self.groupbox_products.setTitle(_translate("NCBI_Result", "Rechercher des produits"))
        self.button_search_request.setText(_translate("NCBI_Result", "Rechercher"))
        self.label_help.setText(_translate("NCBI_Result", "Aide à la construction de la requête"))
        self.label_selectall.setText(_translate("NCBI_Result", "Tout sélectionner"))
        self.label_deselectall.setText(_translate("NCBI_Result", "Tout désélectionner"))
        self.label_nb.setText(_translate("NCBI_Result", "Affichage par page"))
        self.combobox_nb.setItemText(0, _translate("NCBI_Result", "50"))
        self.combobox_nb.setItemText(1, _translate("NCBI_Result", "100"))
        self.combobox_nb.setItemText(2, _translate("NCBI_Result", "200"))
        self.combobox_nb.setItemText(3, _translate("NCBI_Result", "500"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("NCBI_Result", "Accession"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("NCBI_Result", "Description"))
        self.label_page.setText(_translate("NCBI_Result", "Page"))
        self.button_extract.setText(_translate("NCBI_Result", "Extraire la sélection vers un fichier Excel"))
        self.button_download.setText(_translate("NCBI_Result", "Télécharger la sélection sur la base de données"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NCBI_Result = QtWidgets.QMainWindow()
    ui = Ui_NCBI_Result()
    ui.setupUi(NCBI_Result)
    NCBI_Result.show()
    sys.exit(app.exec_())
