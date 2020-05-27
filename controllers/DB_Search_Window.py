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
        query = self.construct_query()
        results = self.mongoDB_connexion.collection.find(query)
        self.window_result = DB_Result_Window(results=results)
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
            'checkbox_id': 'id',
            'checkbox_descr': 'description',
            'checkbox_download': 'download_date',
            'checkbox_type': 'annotations.molecule_type',
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
        checked_checkboxes = self.get_checked_checkboxes()
        parts_of_query = []
        for key, checkbox in checked_checkboxes.items():
            checkbox_name = checkbox.objectName()
            edit_name = self.find_associated_edit_name(checkbox)
            if checkbox_name == 'checkbox_date' or checkbox_name == 'checkbox_download':
                combobox_name = self.find_associated_combobox_name(checkbox)
                combobox = getattr(self, combobox_name)
                operation = combobox.currentText()
                edit_1 = getattr(self, edit_name + "_1")
                text_1 = edit_1.text()
                date_1 = datetime.datetime.strptime(text_1, '%d/%m/%Y')
                if operation == 'avant':
                    value = {"$lte": date_1}
                elif operation == 'apres':
                    value = {'$gte': date_1}
                else:
                    edit_2 = getattr(self, edit_name + "_2")
                    text_2 = edit_2.text()
                    date_2 = datetime.datetime.strptime(text_2, '%d/%m/%Y')
                    value = {"$lte": date_1, "$gt": date_2}
            else:
                edit = getattr(self, edit_name)
                text = edit.text()
                if checkbox_name == 'checkbox_species' or checkbox_name == 'checkbox_taxo':
                    value = text.capitalize()
                else:
                    value = re.compile(text, re.IGNORECASE)
            parts_of_query.append({key: value})

        if len(parts_of_query) > 1:
            query = {"$and":parts_of_query}
        else:
            query = parts_of_query[0]
        return query

    def get_checked_checkboxes(self):
        checkbox_names = self.get_checkbox_corresp_key()
        checked = {}
        for checkbox_name in checkbox_names:
            checkbox_widget = getattr(self, checkbox_name)
            if checkbox_widget.isChecked():
                key = checkbox_names[checkbox_name]
                checked[key] = checkbox_widget
        return checked
