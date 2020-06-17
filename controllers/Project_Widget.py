from views.project_widget_view import Ui_project_widget
from functions.graphics_function import *
from PyQt5 import QtWidgets


class Project_Widget(QtWidgets.QWidget, Ui_project_widget):
    """
    controlling class for db_search_view
    """

    def __init__(self, parent=None, connexion=None, project=None, statut=None):
        super(Project_Widget, self).__init__(parent)
        self.setupUi(self)
        self.connexion = connexion
        self.collection = connexion.get_collection("Projects", "Nucleotide")
        self.project = project
        self.statut = statut
        self._init_ui()

    def _init_ui(self):
        self.modif.mouseReleaseEvent = self.modif_clicked
        self.deleting.mouseReleaseEvent = self.delete_clicked
        if self.statut == "Modif":
            self.version_modif()
        elif self.statut == "Fix":
            self.version_fix()
        elif self.statut == "New":
            self.version_new()
        else:
            print(self.statut)

    def modif_clicked(self, event):
        if self.statut == 'Fix':
            self.version_modif()
            self.statut = "Modif"
        elif self.statut == "Modif":
            self.update_project()
            self.statut = "Fix"
            self.version_fix()
        elif self.statut == "New":
            saving = self.save_new()
            if saving:
                self.statut = "Fix"
                self.version_fix()
        else:
            print(self.statut)

    def delete_clicked(self, event):
        if self.statut == "New":
            self.close()
        else:
            question = QtWidgets.QMessageBox.question(self, "Supprimer le projet", "Etes vous sûr ?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if question == QtWidgets.QMessageBox.Yes:
                self.delete_project()

    def version_fix(self):
        self.name.close()
        self.comment.close()
        self.name = create_label(self.project["name"])
        self.gridLayout.addWidget(self.name, 0, 0)
        if len(self.project["comment"]) > 0:
            self.comment = create_label(self.project["comment"])
            self.gridLayout.addWidget(self.comment, 1, 0)
        self.modif.setText("Modifier")

    def version_modif(self):
        self.name.close()
        self.comment.close()
        self.name = create_edit(text=self.project["name"])
        self.gridLayout.addWidget(self.name, 0, 0)
        self.comment = create_edit()
        self.gridLayout.addWidget(self.comment, 1, 0)
        if len(self.project["comment"]) > 0:
            self.comment.setText(self.project["comment"])
        self.modif.setText("Enregistrer")

    def version_new(self):
        self.name.close()
        self.comment.close()
        self.name = create_edit()
        self.gridLayout.addWidget(self.name, 0, 0)
        self.comment = create_edit()
        self.gridLayout.addWidget(self.comment, 1, 0)
        self.modif.setText("Enregistrer")

    def update_project(self):
        id = self.project["_id"]
        updating = self.collection.update({"_id":id}, {"name":self.name.text(), "comment":self.comment.text()})
        if updating["n"] == 1:
            self.project = self.connexion.get_one("Projects", id)
        else:
            create_messageBox("Erreur", "Une erreur est survenue")

    def save_new(self):
        query = {"name":self.name.text(), "comment":self.comment.text(), "ids_gb":[]}
        existed = self.collection.find_one({"name":self.name.text()})
        if existed is not None:
            create_messageBox("Attention !", "Ce nom de projet existe déjà !")
            return False
        else:
            add = self.collection.insert_one(query)
            if add.acknowledged:
                self.project = self.connexion.get_one("Projects", add.inserted_id)
                return True
            else:
                create_messageBox("Erreur", "Une erreur est survenue")
                return False

    def delete_project(self):
        delete = self.collection.delete_one({"_id":self.project["_id"]})
        self.project = None
        self.close()
