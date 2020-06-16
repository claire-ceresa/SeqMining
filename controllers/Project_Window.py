from controllers.Project_Widget import Project_Widget
from views.project_window_view import Ui_MainWindow
from functions.graphics_function import *


class Project_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    controlling class for db_search_view
    """

    def __init__(self, parent=None, connexion=None):
        super(Project_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des projets")
        self.connexion = connexion
        self.projects_widgets = []
        self._init_ui()

    def _init_ui(self):
        projects = self.connexion.get_all_projects()
        for project in projects:
            widget = Project_Widget(connexion=self.connexion, project=project)
            widget.version_fix()
            self.projects_widgets.append(widget)
        layout = create_layout(widgets=self.projects_widgets, vertical=True, spacer=True)
        self.scroll_projects.setLayout(layout)


    def button_add_clicked(self):
        widget = Project_Widget(connexion=self.connexion, project=None)
        widget.version_new()
        self.projects_widgets.append(widget)
        layout = self.scroll_projects.layout()
        layout.addWidget(widget)