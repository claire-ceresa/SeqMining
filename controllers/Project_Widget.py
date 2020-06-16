from views.project_widget_view import Ui_project_widget
from functions.graphics_function import *



class Project_Widget(QtWidgets.QWidget, Ui_project_widget):
    """
    controlling class for db_search_view
    """

    def __init__(self, parent=None, connexion=None, project=None):
        super(Project_Widget, self).__init__(parent)
        self.setupUi(self)
        self.connexion = connexion
        self.project = project
        self.fixed = True
        self.modified = False
        self.new = False
        self._init_ui()

    def _init_ui(self):
        self.modif.mouseReleaseEvent = self.modif_clicked
        self.deleting.mouseReleaseEvent = self.delete_clicked

    def modif_clicked(self, event):
        if self.fixed:
            self.version_modif()
        elif self.modified:
            self.update_project()
            self.version_fix()
        elif self.new:
            self.save_new()


    def delete_clicked(self, event):
        print("delete")

    def version_fix(self):
        self.fixed = True
        self.modified = False
        self.new = False
        self.name.deleteLater()
        self.comment.deleteLater()
        self.name = create_label(self.project["name"])
        self.gridLayout.addWidget(self.name, 0, 0)
        if len(self.project["comment"]) > 0:
            self.comment = create_label(self.project["comment"])
            self.gridLayout.addWidget(self.comment, 1, 0)
        self.modif.setText("Modifier")

    def version_modif(self):
        self.modified = True
        self.fixed = False
        self.new = False
        self.name.deleteLater()
        self.comment.deleteLater()
        self.name = create_edit(text=self.project["name"])
        self.gridLayout.addWidget(self.name, 0, 0)
        self.comment = create_edit()
        self.gridLayout.addWidget(self.comment, 1, 0)
        if len(self.project["comment"]):
            self.comment.setText(self.project["comment"])
        self.modif.setText("Enregistrer")

    def version_new(self):
        self.modified = False
        self.fixed = False
        self.new = True
        self.name.deleteLater()
        self.comment.deleteLater()
        self.name = create_edit()
        self.gridLayout.addWidget(self.name, 0, 0)
        self.comment = create_edit()
        self.gridLayout.addWidget(self.comment, 1, 0)
        self.modif.setText("Enregistrer")

    def update_project(self):
        print("save modification")

    def save_new(self):
        print("save new project")

