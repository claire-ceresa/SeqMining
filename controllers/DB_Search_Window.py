import re
from datetime import datetime
from controllers.DB_Results_Window import DB_Results_Window
from controllers.DB_Product_Window import DB_Product_Window
from controllers.Project_Window import Project_Window
from views.db_search_view import Ui_DB_Search
from functions.graphics_function import *



class DB_Search_Window(QtWidgets.QMainWindow, Ui_DB_Search):
    """
    controlling class for db_search_view
    """

    def __init__(self, parent=None, connexion=None):
        super(DB_Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rechercher sur la base de données locale")
        self.mongoDB_connexion = connexion
        self.window_project = None
        self.window_result = None
        self._init_ui()

    # METHODS OF THE CLASS #

    def button_search_clicked(self):
        """Launch the search on the MongoDB database and open the result window"""
        query = self.construct_query()
        collection = self.mongoDB_connexion.get_collection("Product", "Nucleotide")
        results = list(collection.find(query))
        if len(results) == 1:
            self.window_result = DB_Product_Window(product=results[0])
        else:
            self.window_result = DB_Results_Window(results=results)
        self.window_result.show()

    def combobox_date_changed(self, text):
        """Show a 2nd DateEdit if the combobox is 'entre' for the product date"""
        if text == "entre":
            self.label_date_et.show()
            self.edit_date_2.show()
        else:
            self.label_date_et.hide()
            self.edit_date_2.hide()

    def combobox_download_changed(self, text):
        """Show a 2nd DateEdit if the combobox is 'entre' for the download date"""
        if text == "entre":
            self.label_download_et.show()
            self.edit_download_2.show()
        else:
            self.label_download_et.hide()
            self.edit_download_2.hide()

    def action_project_triggered(self):
        self.window_project = Project_Window(connexion=self.mongoDB_connexion)
        if self.window_project.exec() == 0:
            self._init_combobox_project()


    # GRAPHIC METHODS #

    def _init_ui(self):
        """Initialize the user interface"""
        self.label_date_et.hide()
        self.edit_date_2.hide()
        self.label_download_et.hide()
        self.edit_download_2.hide()
        self._init_combobox_project()

    def _init_combobox_project(self):
        self.combobox_project.clear()
        projects = self.mongoDB_connexion.get_all_projects()
        for project in projects:
            self.combobox_project.addItem(project["name"])

    def get_checked_checkboxes(self):
        """
        Get the checkbox that were checked
        :return: {name of the checkbox, attribute of the DB}
        """
        checkbox_names = self.get_checkbox_corresp_key()
        checked = {}
        for checkbox_name in checkbox_names:
            checkbox_widget = getattr(self, checkbox_name)
            if checkbox_widget.isChecked():
                key = checkbox_names[checkbox_name]
                checked[key] = checkbox_widget
        return checked

    # OTHER FUNCTIONS #

    def get_checkbox_corresp_key(self):
        """
        Correspondance between the name of the checkboxes and the attribute on the DB
        :return:  {name of the checkbox, attribute of the DB}
        """
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

    def construct_query(self):
        """
        Construct the MongoDB query based on the widgets checked
        :return: the query {}
        """
        checked_checkboxes = self.get_checked_checkboxes()
        parts_of_query = []

        for key, checkbox in checked_checkboxes.items():
            checkbox_name = checkbox.objectName()
            edit_name = self.find_associated_widget_name("edit", checkbox)

            if checkbox_name == 'checkbox_date' or checkbox_name == 'checkbox_download':
                combobox_name = self.find_associated_widget_name("combobox", checkbox)
                combobox = getattr(self, combobox_name)
                operation = combobox.currentText()
                edit_1 = getattr(self, edit_name + "_1")
                text_1 = edit_1.text()
                date_1 = datetime.strptime(text_1, '%d/%m/%Y')

                if operation == 'avant':
                    value = {"$lte": date_1}
                elif operation == 'après':
                    value = {'$gte': date_1}
                else:
                    edit_2 = getattr(self, edit_name + "_2")
                    text_2 = edit_2.text()
                    date_2 = datetime.strptime(text_2, '%d/%m/%Y')
                    value = {"$gte": date_1, "$lt": date_2}
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

    def find_associated_widget_name(self, type, reference):
        """
        For a widget, find another widget associated
        :param type: widget of reference
        :param reference: type of the widget searched
        :return: name of the widget searched
        """
        name = reference.objectName()
        name_split = name.split("_")
        attribute = name_split[1]
        name = type + "_" + attribute
        return name


