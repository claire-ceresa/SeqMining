# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_search.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DB_Search(object):
    def setupUi(self, DB_Search):
        DB_Search.setObjectName("DB_Search")
        DB_Search.resize(525, 537)
        self.centralwidget = QtWidgets.QWidget(DB_Search)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupbox_gen = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_gen.setObjectName("groupbox_gen")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox_gen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_id = QtWidgets.QHBoxLayout()
        self.layout_id.setObjectName("layout_id")
        self.label_id = QtWidgets.QLabel(self.groupbox_gen)
        self.label_id.setObjectName("label_id")
        self.layout_id.addWidget(self.label_id)
        self.edit_id = QtWidgets.QLineEdit(self.groupbox_gen)
        self.edit_id.setObjectName("edit_id")
        self.layout_id.addWidget(self.edit_id)
        self.verticalLayout.addLayout(self.layout_id)
        self.layout_descr = QtWidgets.QHBoxLayout()
        self.layout_descr.setObjectName("layout_descr")
        self.label_descr = QtWidgets.QLabel(self.groupbox_gen)
        self.label_descr.setObjectName("label_descr")
        self.layout_descr.addWidget(self.label_descr)
        self.edit_descr = QtWidgets.QLineEdit(self.groupbox_gen)
        self.edit_descr.setObjectName("edit_descr")
        self.layout_descr.addWidget(self.edit_descr)
        self.verticalLayout.addLayout(self.layout_descr)
        self.layout_download = QtWidgets.QHBoxLayout()
        self.layout_download.setObjectName("layout_download")
        self.label_download = QtWidgets.QLabel(self.groupbox_gen)
        self.label_download.setObjectName("label_download")
        self.layout_download.addWidget(self.label_download)
        self.combobox_download = QtWidgets.QComboBox(self.groupbox_gen)
        self.combobox_download.setObjectName("combobox_download")
        self.combobox_download.addItem("")
        self.combobox_download.addItem("")
        self.combobox_download.addItem("")
        self.layout_download.addWidget(self.combobox_download)
        self.edit_download_1 = QtWidgets.QDateEdit(self.groupbox_gen)
        self.edit_download_1.setCalendarPopup(True)
        self.edit_download_1.setDate(QtCore.QDate(2020, 5, 1))
        self.edit_download_1.setObjectName("edit_download_1")
        self.layout_download.addWidget(self.edit_download_1)
        self.label_download_et = QtWidgets.QLabel(self.groupbox_gen)
        self.label_download_et.setAlignment(QtCore.Qt.AlignCenter)
        self.label_download_et.setObjectName("label_download_et")
        self.layout_download.addWidget(self.label_download_et)
        self.edit_download_2 = QtWidgets.QDateEdit(self.groupbox_gen)
        self.edit_download_2.setCalendarPopup(True)
        self.edit_download_2.setDate(QtCore.QDate(2020, 5, 1))
        self.edit_download_2.setObjectName("edit_download_2")
        self.layout_download.addWidget(self.edit_download_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_download.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layout_download)
        self.verticalLayout_5.addWidget(self.groupbox_gen)
        self.groupbox_detail = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_detail.setObjectName("groupbox_detail")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupbox_detail)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_type = QtWidgets.QHBoxLayout()
        self.layout_type.setObjectName("layout_type")
        self.label_type = QtWidgets.QLabel(self.groupbox_detail)
        self.label_type.setObjectName("label_type")
        self.layout_type.addWidget(self.label_type)
        self.edit_type = QtWidgets.QLineEdit(self.groupbox_detail)
        self.edit_type.setObjectName("edit_type")
        self.layout_type.addWidget(self.edit_type)
        self.verticalLayout_2.addLayout(self.layout_type)
        self.layout_topo = QtWidgets.QHBoxLayout()
        self.layout_topo.setObjectName("layout_topo")
        self.label_topo = QtWidgets.QLabel(self.groupbox_detail)
        self.label_topo.setObjectName("label_topo")
        self.layout_topo.addWidget(self.label_topo)
        self.edit_topo = QtWidgets.QLineEdit(self.groupbox_detail)
        self.edit_topo.setObjectName("edit_topo")
        self.layout_topo.addWidget(self.edit_topo)
        self.verticalLayout_2.addLayout(self.layout_topo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_date = QtWidgets.QLabel(self.groupbox_detail)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout.addWidget(self.label_date)
        self.combobox_date = QtWidgets.QComboBox(self.groupbox_detail)
        self.combobox_date.setObjectName("combobox_date")
        self.combobox_date.addItem("")
        self.combobox_date.addItem("")
        self.combobox_date.addItem("")
        self.horizontalLayout.addWidget(self.combobox_date)
        self.edit_date_1 = QtWidgets.QDateEdit(self.groupbox_detail)
        self.edit_date_1.setCalendarPopup(True)
        self.edit_date_1.setDate(QtCore.QDate(2020, 5, 1))
        self.edit_date_1.setObjectName("edit_date_1")
        self.horizontalLayout.addWidget(self.edit_date_1)
        self.label_date_et = QtWidgets.QLabel(self.groupbox_detail)
        self.label_date_et.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_et.setObjectName("label_date_et")
        self.horizontalLayout.addWidget(self.label_date_et)
        self.edit_date_2 = QtWidgets.QDateEdit(self.groupbox_detail)
        self.edit_date_2.setCalendarPopup(True)
        self.edit_date_2.setDate(QtCore.QDate(2020, 5, 1))
        self.edit_date_2.setObjectName("edit_date_2")
        self.horizontalLayout.addWidget(self.edit_date_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.layout_keyword = QtWidgets.QHBoxLayout()
        self.layout_keyword.setObjectName("layout_keyword")
        self.label_keyword = QtWidgets.QLabel(self.groupbox_detail)
        self.label_keyword.setObjectName("label_keyword")
        self.layout_keyword.addWidget(self.label_keyword)
        self.edit_keyword = QtWidgets.QLineEdit(self.groupbox_detail)
        self.edit_keyword.setObjectName("edit_keyword")
        self.layout_keyword.addWidget(self.edit_keyword)
        self.verticalLayout_2.addLayout(self.layout_keyword)
        self.layout_comment = QtWidgets.QHBoxLayout()
        self.layout_comment.setObjectName("layout_comment")
        self.label_comment = QtWidgets.QLabel(self.groupbox_detail)
        self.label_comment.setObjectName("label_comment")
        self.layout_comment.addWidget(self.label_comment)
        self.edit_comment = QtWidgets.QLineEdit(self.groupbox_detail)
        self.edit_comment.setObjectName("edit_comment")
        self.layout_comment.addWidget(self.edit_comment)
        self.verticalLayout_2.addLayout(self.layout_comment)
        self.verticalLayout_5.addWidget(self.groupbox_detail)
        self.groupbox_org = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_org.setFlat(False)
        self.groupbox_org.setObjectName("groupbox_org")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_org)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout_species = QtWidgets.QHBoxLayout()
        self.layout_species.setObjectName("layout_species")
        self.label_species = QtWidgets.QLabel(self.groupbox_org)
        self.label_species.setObjectName("label_species")
        self.layout_species.addWidget(self.label_species)
        self.edit_species = QtWidgets.QLineEdit(self.groupbox_org)
        self.edit_species.setObjectName("edit_species")
        self.layout_species.addWidget(self.edit_species)
        self.verticalLayout_3.addLayout(self.layout_species)
        self.layout_taxo = QtWidgets.QHBoxLayout()
        self.layout_taxo.setObjectName("layout_taxo")
        self.label_taxo = QtWidgets.QLabel(self.groupbox_org)
        self.label_taxo.setObjectName("label_taxo")
        self.layout_taxo.addWidget(self.label_taxo)
        self.edit_taxo = QtWidgets.QLineEdit(self.groupbox_org)
        self.edit_taxo.setObjectName("edit_taxo")
        self.layout_taxo.addWidget(self.edit_taxo)
        self.verticalLayout_3.addLayout(self.layout_taxo)
        self.verticalLayout_5.addWidget(self.groupbox_org)
        self.groupbox_ref = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_ref.setObjectName("groupbox_ref")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupbox_ref)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout_title = QtWidgets.QHBoxLayout()
        self.layout_title.setObjectName("layout_title")
        self.label_title = QtWidgets.QLabel(self.groupbox_ref)
        self.label_title.setObjectName("label_title")
        self.layout_title.addWidget(self.label_title)
        self.edit_title = QtWidgets.QLineEdit(self.groupbox_ref)
        self.edit_title.setObjectName("edit_title")
        self.layout_title.addWidget(self.edit_title)
        self.verticalLayout_4.addLayout(self.layout_title)
        self.layout_author = QtWidgets.QHBoxLayout()
        self.layout_author.setObjectName("layout_author")
        self.label_author = QtWidgets.QLabel(self.groupbox_ref)
        self.label_author.setObjectName("label_author")
        self.layout_author.addWidget(self.label_author)
        self.edit_author = QtWidgets.QLineEdit(self.groupbox_ref)
        self.edit_author.setObjectName("edit_author")
        self.layout_author.addWidget(self.edit_author)
        self.verticalLayout_4.addLayout(self.layout_author)
        self.layout_journal = QtWidgets.QHBoxLayout()
        self.layout_journal.setObjectName("layout_journal")
        self.label_journal = QtWidgets.QLabel(self.groupbox_ref)
        self.label_journal.setObjectName("label_journal")
        self.layout_journal.addWidget(self.label_journal)
        self.edit_journal = QtWidgets.QLineEdit(self.groupbox_ref)
        self.edit_journal.setObjectName("edit_journal")
        self.layout_journal.addWidget(self.edit_journal)
        self.verticalLayout_4.addLayout(self.layout_journal)
        self.verticalLayout_5.addWidget(self.groupbox_ref)
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setObjectName("button_search")
        self.verticalLayout_5.addWidget(self.button_search)
        DB_Search.setCentralWidget(self.centralwidget)

        self.retranslateUi(DB_Search)
        self.button_search.clicked.connect(DB_Search.button_search_clicked)
        self.combobox_download.currentTextChanged['QString'].connect(DB_Search.combobox_download_changed)
        self.combobox_date.currentTextChanged['QString'].connect(DB_Search.combobox_date_changed)
        QtCore.QMetaObject.connectSlotsByName(DB_Search)

    def retranslateUi(self, DB_Search):
        _translate = QtCore.QCoreApplication.translate
        DB_Search.setWindowTitle(_translate("DB_Search", "MainWindow"))
        self.groupbox_gen.setTitle(_translate("DB_Search", "Généralités"))
        self.label_id.setText(_translate("DB_Search", "Identifiant GenBank"))
        self.label_descr.setText(_translate("DB_Search", "Titre"))
        self.label_download.setText(_translate("DB_Search", "Date du téléchargement"))
        self.combobox_download.setItemText(0, _translate("DB_Search", "avant"))
        self.combobox_download.setItemText(1, _translate("DB_Search", "après"))
        self.combobox_download.setItemText(2, _translate("DB_Search", "entre"))
        self.label_download_et.setText(_translate("DB_Search", "et"))
        self.groupbox_detail.setTitle(_translate("DB_Search", "Détails"))
        self.label_type.setText(_translate("DB_Search", "Type de molécule"))
        self.label_topo.setText(_translate("DB_Search", "Topologie de la molécule"))
        self.label_date.setText(_translate("DB_Search", "Date"))
        self.combobox_date.setItemText(0, _translate("DB_Search", "avant"))
        self.combobox_date.setItemText(1, _translate("DB_Search", "après"))
        self.combobox_date.setItemText(2, _translate("DB_Search", "entre"))
        self.label_date_et.setText(_translate("DB_Search", "et"))
        self.label_keyword.setText(_translate("DB_Search", "Mot-clé"))
        self.label_comment.setText(_translate("DB_Search", "Commentaire"))
        self.groupbox_org.setTitle(_translate("DB_Search", "Organisme"))
        self.label_species.setText(_translate("DB_Search", "Espèce"))
        self.label_taxo.setText(_translate("DB_Search", "Dans la taxonomie"))
        self.groupbox_ref.setTitle(_translate("DB_Search", "Références"))
        self.label_title.setText(_translate("DB_Search", "Titre"))
        self.label_author.setText(_translate("DB_Search", "Auteur"))
        self.label_journal.setText(_translate("DB_Search", "Journal"))
        self.button_search.setText(_translate("DB_Search", "Rechercher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DB_Search = QtWidgets.QMainWindow()
    ui = Ui_DB_Search()
    ui.setupUi(DB_Search)
    DB_Search.show()
    sys.exit(app.exec_())
