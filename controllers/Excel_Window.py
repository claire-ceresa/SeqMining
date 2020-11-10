from views.excel_view import Ui_excel_window
from functions.graphics_function import *
from functions.db_functions import *
from objects.DB_Product import DB_Product
from objects.Excel import Excel


class Excel_Window(QtWidgets.QMainWindow, Ui_excel_window):
    """
    controlling class for excel_view
    """

    corresp_var_method = {
        'Identifiant GenBank': 'get_id',
        'Nom': 'get_protein_name',
        'Description': 'get_description',
        'Taille': 'get_length',
        'Poids': 'get_molecular_weight',
        'Espèce': 'get_species',
        'Sequence': 'get_sequence',
        'Projets': 'get_projects'
    }

    def __init__(self, parent=None, results=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Exporter vers un fichier Excel")
        self.results = results
        self._create_cell_combobox(0)

    # METHODS OF THE CLASS #

    def button_add_clicked(self):
        count = self.table.columnCount()
        if count < len(self.corresp_var_method):
            self.table.setColumnCount(count + 1)
            self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        try:
            filename = get_save_filename("Excel")
            file = Excel(filename)
            print("file OK")

            if self.checkbox_project.isChecked():
                splitted_results = self.split_results()
                for project, data in splitted_results.items():
                    datas_to_export = self.get_data_to_export(data)
                    worksheet = file.add_worksheet(project)
                    file.add_data(worksheet, datas_to_export)

            else:
                print("not if")
                datas_to_export = self.get_data_to_export(self.results)
                print("datas")
                worksheet = file.add_worksheet()
                file.add_data(worksheet, datas_to_export)

            file.close()

        except Exception as e:
            self.label_created.setText("Le fichier n'a pas été crée !\n" + str(e))
        else:
            self.label_created.setText("Le fichier a été crée !")

    # GRAPHIC METHODS #

    def _create_cell_combobox(self, column):
        """Create a QComboBox in the header cell"""
        combobox = QtWidgets.QComboBox()
        fill_combobox(combobox, list(self.corresp_var_method))
        self.table.setCellWidget(0, column, combobox)
        self.table.resizeColumnsToContents()

    # OTHER METHODS #

    def get_data_to_export(self, results):
        headers = []
        nb_columns = self.table.columnCount()
        print("nb col : " + str(nb_columns))
        for column in range(0, nb_columns):
            item = self.table.cellWidget(0, column)
            variable_name = item.currentText()
            headers.append(variable_name)
        print(headers)

        datas = []
        for result in results:
            line = []
            product = DB_Product(data=result)
            for header in headers:
                method = self.corresp_var_method[header]
                variable_value = getattr(product, method)()
                line.append(variable_value)
            datas.append(line)

        return {"column_names":headers, "rows":datas}

    def split_results(self):
        all_projects = get_all_projects()
        splitted_results = {"Aucun":[]}
        for project in all_projects:
            name = project["name"]
            splitted_results[name] = []

        for result in self.results:
            id = result["id"]
            projects = get_all_projects_for_a_product(id)
            if len(projects) == 0:
                splitted_results["Aucun"].append(result)
            else:
                for project in projects:
                    name = project["name"]
                    splitted_results[name].append(result)
        return splitted_results
