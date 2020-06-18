from views.project_window_view import Ui_Project_Dialog
from controllers.Project_Widget import Project_Widget
from functions.graphics_function import *
from functions.db_functions import *


class Project_Window(QtWidgets.QDialog, Ui_Project_Dialog):
    """
    controlling class for project_window_view
    """

    def __init__(self, parent=None):
        super(Project_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des projets")
        self.projects_widgets = []
        self._init_ui()

    def _init_ui(self):
        projects = get_all_projects()
        for project in projects:
            widget = Project_Widget(project=project, statut="Fix")
            self.projects_widgets.append(widget)
        layout = create_layout(widgets=self.projects_widgets, vertical=True)
        self.scroll_projects.setLayout(layout)

    def button_add_clicked(self):
        widget = Project_Widget(project=None, statut="New")
        self.projects_widgets.append(widget)
        layout = self.scroll_projects.layout()
        layout.addWidget(widget)