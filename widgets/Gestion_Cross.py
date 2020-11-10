from PyQt5.QtWidgets import QWidget, QTreeWidgetItem
from functions.graphics_function import *
from functools import partial


class Gestion_Cross(QWidget):

    def __init__(self, parent=None, connexion=None, widget=None):
        super(Gestion_Cross, self).__init__(parent)
        self.current = None
        self.connexion = connexion
        self.widget = widget
        self.queries = []

    # METHODS OF THE BUTTONS

    def button_save_clicked(self):
        print(self.queries)
        action = self.connexion.run_on_php(self.queries)
        if action['sent']:
            create_messageBox("Enregistré !", "Modifications enregistrées !")
            self.queries.clear()

    def tree_species_clicked(self, item, column):
        headers = self.widget.c_tree_species.headerItem()
        species = headers.text(column)
        product = item.text(0)
        query = None
        if item.checkState(column) == Qt.Checked:
            message = QtWidgets.QMessageBox.question(self, "Confirmer", "Associer " + product + " - " + species + " ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
            if message == QtWidgets.QMessageBox.Yes:
                if item.parent() is None:
                    query = self.connexion.create_query_insert("product_species", {'product': '"'+product+'"', 'species': '"'+species+'"'})
                else:
                    query = self.connexion.create_query_insert("type_species", {'type': '"'+product+'"', 'species': '"'+species+'"'})
        else:
            message = QtWidgets.QMessageBox.question(self, "Confirmer", "Dissocier " + product + " - " + species + " ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
            if message == QtWidgets.QMessageBox.Yes:
                if item.parent() is None:
                    query = self.connexion.create_query_delete("product_species",  {'product': '"'+product+'"', 'species': '"'+species+'"'})
                else:
                    query = self.connexion.create_query_delete("type_species",  {'type': '"'+product+'"', 'species': '"'+species+'"'})
        self.queries.append({'query':query})

    def tree_app_clicked(self, tree, item, column):
        headers = tree.headerItem()
        app = headers.text(column)
        product = item.text(0)
        query = None
        if item.checkState(column) == Qt.Checked:
            message = QtWidgets.QMessageBox.question(self, "Confirmer", "Associer " + product + " - " + app + " ?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
            if message == QtWidgets.QMessageBox.Yes:
                query = self.connexion.create_query_insert("is_application", {'product': '"' + product + '"', 'application': '"' + app + '"'})
        else:
            message = QtWidgets.QMessageBox.question(self, "Confirmer", "Dissocier " + product + " - " + app + " ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
            if message == QtWidgets.QMessageBox.Yes:
                query = self.connexion.create_query_delete("is_application",  {'product': '"'+product+'"', 'application': '"'+app+'"'})
        self.queries.append({'query':query})


    # GRAPHIC METHODS

    def init(self):
        self.connexion.load_datas()
        self.fill_in_species()
        self.fill_in_app()

    def fill_in_species(self):
        self.widget.c_tree_species.clear()
        all_species = self.connexion.get_all_species()
        species_product_type = self.connexion.get_species_product_type()

        headers = [""]
        for species in all_species:
            headers.append(species['name'])
        self.widget.c_tree_species.setHeaderLabels(headers)

        for product in species_product_type:
            parent = QTreeWidgetItem(self.widget.c_tree_species)
            parent.setText(0, product['name'])
            self.fill_in_item(parent, headers, product['species'])
            for type in product['types']:
                child = QTreeWidgetItem(parent)
                child.setText(0, type['name'])
                self.fill_in_item(child, headers, type['species'])

    def fill_in_item(self, item, headers, species):
        for column, species_name in enumerate(headers):
            if column > 0:
                item.setText(column, '')
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                if species_name in species:
                    item.setCheckState(column, Qt.Checked)
                else:
                    item.setCheckState(column, Qt.Unchecked)

    def fill_in_app(self):
        self.fill_in_app_trees(tree=self.widget.c_tree_app_cos, headers=self.connexion.get_app_of_domain("cosmetique"))
        self.widget.c_tree_app_cos.itemClicked.connect(partial(self.tree_app_clicked, self.widget.c_tree_app_cos))
        self.fill_in_app_trees(tree=self.widget.c_tree_app_pharma,headers=self.connexion.get_app_of_domain("pharma"))
        self.widget.c_tree_app_pharma.itemClicked.connect(partial(self.tree_app_clicked, self.widget.c_tree_app_pharma))
        self.fill_in_app_trees(tree=self.widget.c_tree_app_biotech,headers=self.connexion.get_app_of_domain("biotech"))
        self.widget.c_tree_app_biotech.itemClicked.connect(partial(self.tree_app_clicked, self.widget.c_tree_app_biotech))

    def fill_in_app_trees(self, tree, headers):
        tree.clear()
        datas = self.connexion.get_product_app()
        headers.insert(0, "")
        tree.setHeaderLabels(headers)
        for product, applications in datas.items():
            item = QTreeWidgetItem(tree)
            item.setText(0, product)
            for column, app_name in enumerate(headers):
                if column > 0:
                    item.setText(column, '')
                    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                    if app_name in applications:
                        item.setCheckState(column, Qt.Checked)
                    else:
                        item.setCheckState(column, Qt.Unchecked)

