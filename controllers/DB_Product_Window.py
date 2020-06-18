from PyQt5.Qt import *
from views.db_product_view import Ui_db_product
from controllers.Project_Widget import Project_Widget
from functions.NCBI_functions import *
from functions.other_functions import *
from functions.graphics_function import *
from functions.db_functions import *


class DB_Product_Window(QtWidgets.QMainWindow, Ui_db_product):
    """
    controlling class for db_product_view
    """

    def __init__(self, parent=None, product=None):
        super(DB_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(product["id"])
        self.product = product
        self.groupbox_feature = None
        self.layout_annot = None
        self.layout_ref = None
        self.layout_project = None
        self._init_ui()

    ## METHODS OF THE CLASS ##

    def button_feature_clicked(self, id):
        if self.groupbox_feature is not None:
            self.groupbox_feature.close()
            self.scroll_area_feature.close()
        self.creation_groupbox_feature(id)
        self.set_sequence(id)

    def action_gen_toggled(self, checked):
        if checked:
            self.create_annotations()
        else:
            clear_layout(self.layout_gb_1)

    def action_ref_toggled(self, checked):
        if self.action_projet.isChecked() == checked:
            clear_layout(self.layout_gb_2)
            self.action_projet.setChecked(False)
        if checked:
            self.create_ref()
        else:
            clear_layout(self.layout_gb_2)

    def action_projet_toggled(self, checked):
        if self.action_ref.isChecked() == checked:
            clear_layout(self.layout_gb_2)
            self.action_ref.setChecked(False)
        if checked:
            self.create_project()
        else:
            clear_layout(self.layout_gb_2)

    ## GRAPHIC METHODS ##

    def _init_ui(self):
        self._init_label_title()
        self._init_features()
        self._init_source()
        if "references" not in self.product['annotations']:
            self.action_ref.setEnabled(False)

    def _init_label_title(self):
        self.label_id.setText(self.product["id"])
        self.label_descr.setText(self.product["description"])
        date_string = get_string(self.product["download_date"])
        self.label_download.setText("Téléchargé le " + date_string)

    def _init_features(self):
        widgets = []

        features = self.product["features"]
        for id, feature in enumerate(features):
            button = create_radio_button(feature["type"])
            widgets.append(button)

        self.groupbutton = create_button_group(widgets=widgets, )
        layout = create_layout(widgets=widgets, vertical=True)
        self.area_button.setLayout(layout)
        self.groupbutton.buttonClicked['int'].connect(self.button_feature_clicked)

    def _init_source(self):
        button = self.groupbutton.button(0)
        if button is not None:
            button.setChecked(True)
            self.button_feature_clicked(0)

    def creation_groupbox_feature(self, id):
        self.groupbox_feature = create_groupbox()

        feature = self.product["features"][id]
        for key, value in feature["qualifiers"].items():
            if key == "translation":
                label_qualifier = create_label(text = key.capitalize() + " :\n" + break_seq(value[0], step=60), wordwrap=True)
                label_qualifier.setTextInteractionFlags(Qt.TextSelectableByMouse)
            else:
                label_qualifier = create_label(text = key.capitalize() + " : " + get_string(value))
            add_widget_to_groupbox(widget=label_qualifier, groupbox=self.groupbox_feature)

        self.scroll_area_feature = create_scroll_area(widget=self.groupbox_feature, frame=False)
        self.layout_feature.addWidget(self.scroll_area_feature)

    def create_annotations(self):
        groupbox_gen = create_groupbox(title='Generalities')
        scroll_area_gen = create_scroll_area(groupbox_gen, minwidth=200, frame=False)
        self.layout_gb_1.addWidget(scroll_area_gen)
        groupbox_org = create_groupbox(title="Organism")
        scroll_area_org = create_scroll_area(groupbox_org, minwidth=200, frame=False)
        self.layout_gb_1.addWidget(scroll_area_org)

        annotations = self.product["annotations"]
        for key, value in annotations.items():
            if key == "references":
                continue
            elif key == "organism" :
                label = create_label(text = get_string(value), wordwrap=False)
                set_label_bold(label, True)
                add_widget_to_groupbox(widget=label, groupbox=groupbox_org)
            elif key == "taxonomy":
                for rank in annotations["taxonomy"][::-1]:
                    label = create_label(text=rank, wordwrap=False)
                    add_widget_to_groupbox(widget=label, groupbox=groupbox_org)
            else:
                label = create_label(text = key.capitalize() + " : " + get_string(value), wordwrap=False)
                add_widget_to_groupbox(widget=label, groupbox=groupbox_gen)

    def create_ref(self):
        groupbox_ref = create_groupbox(title="References")
        scroll_area_ref = create_scroll_area(groupbox_ref, minwidth=200, frame=False)
        self.layout_gb_2.addWidget(scroll_area_ref)

        annotations = self.product["annotations"]
        for index, reference in enumerate(annotations["references"]):
            for key, value in reference.items():
                if key == "location":
                    location = create_feature_location(value[0])
                    label = create_label(text = str(index) + " : " + str(location))
                    set_label_bold(label, True)
                else:
                    label = create_label(text = key.capitalize() + " : " + get_string(value))
                add_widget_to_groupbox(widget=label, groupbox=groupbox_ref)

    def create_project(self):
        groupbox_project = create_groupbox(title="Projets associés")
        scroll_area_project = create_scroll_area(groupbox_project, minwidth=200, frame=False)
        self.layout_gb_2.addWidget(scroll_area_project)

        projects = get_all_projects_for_a_product(self.product["id"])
        for project in projects:
            widget = Project_Widget(project=project, statut="Product", product=self.product)
            add_widget_to_groupbox(widget=widget, groupbox=groupbox_project)

        label_add = create_label("Ajouter à un autre projet")
        set_label_clickable(label_add)
        label_add.mouseReleaseEvent = self.add_to_a_project
        self.layout_gb_2.addWidget(label_add)

        spacer = create_spacer(vertical=True)
        layout = groupbox_project.layout()
        layout.addItem(spacer)

    def set_sequence(self, id):
        sequence = self.product["seq"]["seq"]
        feature = self.product["features"][id]
        location_dict = feature["location"]
        location = create_feature_location(location_dict)
        self.groupbox_feature.setTitle(str(location))
        if "positions" in location_dict:
            self.colore_compound_location(location, sequence)
        else:
            if location.start == 0 and location.end == len(sequence):
                cut_sequence = break_seq(sequence)
                self.label_seq.setText(cut_sequence)
            else:
                self.colore_feature_location(location, sequence)

    def colore_feature_location(self,location, sequence):
        extract = location.extract(sequence)
        cut_sequence = self.cut_sequence(extract, sequence)
        sequence_finale = " ".join(cut_sequence)
        self.label_seq.setText(sequence_finale)

    def colore_compound_location(self, location, all_sequence):
        all_cut_part = []
        sequence = all_sequence
        for part in location.parts:
            extract = part.extract(all_sequence)
            cut_sequence = self.cut_sequence(extract, sequence)
            all_cut_part.append(cut_sequence[0])
            all_cut_part.append(cut_sequence[1])
            sequence = cut_sequence[2].replace(" ", "")
        all_cut_part.append(cut_sequence[2])
        sequence_finale = " ".join(all_cut_part)
        self.label_seq.setText(sequence_finale)

    def cut_sequence(self, extract, sequence):
        middle = "<span style='color:#ff0000;'>" + str(break_seq(extract)) + "</span>"
        position_start_feature = sequence.find(extract)
        position_end_feature = position_start_feature + len(extract)
        begin = sequence[:position_start_feature]
        end = sequence[position_end_feature:]
        return [break_seq(begin), middle, break_seq(end)]

    def add_to_a_project(self, event):
        projects = get_not_project_for_a_product(self.product["id"])
        project_name = extract_list_of_attribute(projects, "name")
        self.combobox_project = create_combobox(project_name)
        label_ok = create_label("Ok")
        set_label_clickable(label_ok)
        label_ok.mouseReleaseEvent = self.save_product_in_project
        layout = create_layout([self.combobox_project, label_ok], horizontal=True)
        self.layout_gb_2.addLayout(layout)

    def save_product_in_project(self, event):
        name = self.combobox_project.currentText()
        add_product_to_project(id=self.product["id"], project=name)
