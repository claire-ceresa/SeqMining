from PyQt5.Qt import *
from views.db_product_view import Ui_db_product
from functions.NCBI_functions import *
from functions.other_functions import *
from functions.graphics_function import *


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
            clear_layout(self.layout_annot)
            self.layout_annot = None

    def action_ref_toggled(self, checked):
        if checked:
            try:
                self.create_ref()
            except Exception as e:
                print(e)
        else:
            clear_layout(self.layout_ref)
            self.layout_ref = None

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
            add_widget_to_groupbox(label_qualifier, self.groupbox_feature)

        self.scroll_area_feature = create_scroll_area(widget=self.groupbox_feature, frame=False)
        self.layout_feature.addWidget(self.scroll_area_feature)

    def create_annotations(self):
        groupbox_gen = create_groupbox(title='Generalities')
        scroll_area_gen = create_scroll_area(groupbox_gen, minwidth=200, frame=False)
        groupbox_org = create_groupbox(title="Organism")
        scroll_area_org = create_scroll_area(groupbox_org, minwidth=200, frame=False)
        self.layout_annot = create_layout(widgets = [scroll_area_gen, scroll_area_org], vertical=True)

        layout = self.centralwidget.layout()
        layout.addLayout(self.layout_annot)

        annotations = self.product["annotations"]
        for key, value in annotations.items():
            if key == "references":
                continue
            elif key == "organism" :
                label = create_label(text = get_string(value), wordwrap=False)
                set_label_bold(label, True)
                add_widget_to_groupbox(label, groupbox_org)
            elif key == "taxonomy":
                for rank in annotations["taxonomy"][::-1]:
                    label = create_label(text=rank, wordwrap=False)
                    add_widget_to_groupbox(label, groupbox_org)
            else:
                label = create_label(text = key.capitalize() + " : " + get_string(value), wordwrap=False)
                add_widget_to_groupbox(label, groupbox_gen)

    def create_ref(self):
        groupbox_ref = create_groupbox(title="References")
        scroll_area_ref = create_scroll_area(groupbox_ref, minwidth=200, frame=False)
        self.layout_ref = create_layout([scroll_area_ref], vertical=True)

        layout = self.centralwidget.layout()
        layout.addLayout(self.layout_ref)

        annotations = self.product["annotations"]
        for index, reference in enumerate(annotations["references"]):
            for key, value in reference.items():
                if key == "location":
                    location = create_feature_location(value[0])
                    label = create_label(text = str(index) + " : " + str(location))
                    set_label_bold(label, True)
                else:
                    label = create_label(text = key.capitalize() + " : " + get_string(value))
                add_widget_to_groupbox(label, groupbox_ref)

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
