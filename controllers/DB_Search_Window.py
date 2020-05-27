from PyQt5 import QtWidgets
from controllers.DB_Results_Window import DB_Result_Window
from views.db_search_view import Ui_DB_Search
import re
import datetime

class DB_Search_Window(QtWidgets.QMainWindow, Ui_DB_Search):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, connexion=None):
        super(DB_Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rechercher sur la base de données locale")
        self.mongoDB_connexion = connexion
        self.window_result = None
        self._init_ui()

    def _init_ui(self):
        self.label_date_et.hide()
        self.edit_date_2.hide()
        self.label_download_et.hide()
        self.edit_download_2.hide()

    def button_search_clicked(self):
        try:
            query = self.construct_query()
        except Exception as e:
            print(e)
        else:
            print(query)
        results = self.mongoDB_connexion.collection.find(query)
        self.window_result = DB_Result_Window(results = results)
        self.window_result.show()

    def combobox_date_changed(self, text):
        if text == "entre":
            self.label_date_et.show()
            self.edit_date_2.show()
        else:
            self.label_date_et.hide()
            self.edit_date_2.hide()

    def combobox_download_changed(self, text):
        if text == "entre":
            self.label_download_et.show()
            self.edit_download_2.show()
        else:
            self.label_download_et.hide()
            self.edit_download_2.hide()

    def get_checkbox_corresp_key(self):
        checkboxes = {
            'checkbox_id':'id',
            'checkbox_descr':'description',
            'checkbox_download':'download_date',
            'checkbox_type':'annotations.molecule_type',
            'checkbox_topo': 'annotations.topology',
            'checkbox_date': 'annotations.date',
            'checkbox_keyword': 'annotations.keywords',
            'checkbox_comment': 'annotations.comment',
            'checkbox_species': 'annotations.organism',
            'checkbox_taxo': 'annotations.taxonomy',
            'checkbox_title': 'annotations.references.title',
            'checkbox_author': 'annotations.references.authors',
            'checkbox_journal': 'annotations.references.journal'
        }
        return checkboxes

    def find_associated_edit_name(self, checkbox):
        name = checkbox.objectName()
        name_split = name.split("_")
        attribute = name_split[1]
        edit_name = "edit_" + attribute
        return edit_name

    def find_associated_combobox_name(self, checkbox):
        name = checkbox.objectName()
        name_split = name.split("_")
        attribute = name_split[1]
        combobox_name = "combobox_" + attribute
        return combobox_name

    def construct_query(self):
        all_checkboxes = self.get_checkbox_corresp_key()
        for checkbox_name in all_checkboxes:
            checkbox = getattr(self, checkbox_name)
            key = all_checkboxes[checkbox_name]
            if checkbox.isChecked():
                edit_name = self.find_associated_edit_name(checkbox)
                if checkbox_name is 'checkbox_date' or checkbox_name is 'checkbox_download':
                    combobox_name = self.find_associated_combobox_name(checkbox)
                    combobox = getattr(self, combobox_name)
                    operation = combobox.currentText()
                    edit_1 = getattr(self, edit_name + "_1")
                    text_1 = edit_1.text()
                    date_1 = datetime.datetime.strptime(text_1, '%d/%m/%Y')
                    if operation == 'avant':
                        value = {"$lte":date_1}
                    elif operation == 'apres':
                        value = {'$gte':date_1}
                    else:
                        edit_2 = getattr(self, edit_name + "_2")
                        text_2 = edit_2.text()
                        date_2 = datetime.datetime.strptime(text_2, '%d/%m/%Y')
                        value = {"$lte":date_1, "$gt":date_2}

                else:
                    edit = getattr(self, edit_name)
                    text = edit.text()
                    if checkbox_name is 'checkbox_species' or checkbox_name is 'checkbox_taxo':
                        value = text.capitalize()
                    else:
                        value = re.compile(text, re.IGNORECASE)
                query = {key:value}
                return query
