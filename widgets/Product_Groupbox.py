from PyQt5.QtWidgets import *
from controllers.Project_Widget import Project_Widget
from functions.graphics_function import *
from functions.NCBI_functions import *
from functions.other_functions import *
from functions.db_functions import *

class Product_Groupbox(QScrollArea):

    def __init__(self, parent=None, datas=None, type=None):
        super(Product_Groupbox, self).__init__(parent)
        self.setWidgetResizable(True)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setMinimumWidth(200)
        self.groupbox = create_groupbox()
        self.setWidget(self.groupbox)
        self.type = type
        self.datas = datas
        self.widgets = []
        self._init_ui()

    def add_widget(self, widget):
        add_widget_to_groupbox(widget=widget, groupbox=self.groupbox)

    def _init_ui(self):
        if self.type == "References":
            self._version_ref()
        elif self.type == "Generalities":
            self._version_gen()
        elif self.type == "Organism":
            self._version_org()
        elif self.type == "Projects":
            self._version_proj()

    def _version_ref(self):
        self.groupbox.setTitle("Références")

        for index, reference in enumerate(self.datas["references"]):
            for key, value in reference.items():
                if key == "location":
                    location = create_feature_location(value[0])
                    label = create_label(text = str(index) + " : " + str(location))
                    set_label_bold(label, True)
                else:
                    label = create_label(text = key.capitalize() + " : " + get_string(value))
                self.widgets.append(label)
                add_widget_to_groupbox(widget=label, groupbox=self.groupbox)

    def _version_gen(self):
        self.groupbox.setTitle("Généralités")

    def _version_org(self):
        self.groupbox.setTitle("Organisme")

    def _version_proj(self):
        self.groupbox.setTitle("Projets associés")
        projects = get_all_projects_for_a_product(self.datas["id"])
        for project in projects:
            widget = Project_Widget(project=project, statut="Product", product=self.datas)
            add_widget_to_groupbox(widget=widget, groupbox=self.groupbox)




