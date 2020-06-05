from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from views.db_product_view import Ui_db_product
from functions.NCBI_functions import *
from functions.other_functions import *
from functions.graphics_function import *

class DB_Product_Window(QtWidgets.QMainWindow, Ui_db_product):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, product=None):
        super(DB_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(product["id"])
        self.product = product
        self.groupbox_feature = None
        self.groupbox_annot = None
        self.groupbox_ref = None
        self._init_label_title()
        self._init_features()

    ## METHODS OF THE CLASS ##

    def button_feature_clicked(self, id):
        if self.groupbox_feature is not None:
            self.groupbox_feature.close()
            self.scroll_area_feature.close()
        self.creation_groupbox_feature(id)
        self.set_sequence(id)

    def action_gen_toggled(self, checked):
        if checked:
            self.create_groupbox_annot()
        else:
            self.groupbox_annot.close()
            self.groupbox_annot = None

    def action_ref_toggled(self, checked):
        if checked:
            self.create_groupbox_ref()
        else:
            self.groupbox_ref.close()
            self.groupbox_ref = None

    ## GRAPHIC METHODS ##

    def _init_label_title(self):
        self.label_id.setText(self.product["id"])
        self.label_descr.setText(self.product["description"])
        date_string = get_string(self.product["download_date"])
        self.label_download.setText("Téléchargé le " + date_string)

    def _init_features(self):
        self.creation_group_button()
        self._init_source()

    def _init_source(self):
        button = self.groupbutton.button(0)
        if button is not None:
            button.setChecked(True)
            self.button_feature_clicked(0)

    def creation_group_button(self):
        self.groupbutton = QButtonGroup()
        widget = []

        features = self.product["features"]
        for id, feature in enumerate(features):
            button = QRadioButton()
            button.setText(feature["type"])
            self.groupbutton.addButton(button, id)
            widget.append(button)

        layout = create_layout(widgets=widget, vertical=True)
        self.area_button.setLayout(layout)
        self.groupbutton.buttonClicked['int'].connect(self.button_feature_clicked)

    def creation_groupbox_feature(self, id):
        self.groupbox_feature = QGroupBox()
        layout_gb = create_layout(vertical=True, spacer=True)
        self.groupbox_feature.setLayout(layout_gb)

        feature = self.product["features"][id]
        for key, value in feature["qualifiers"].items():
            if key == "translation":
                label_qualifier = create_label(text = key.capitalize() + " :\n" + break_seq(value[0], step=60), wordwrap=True)
                label_qualifier.setTextInteractionFlags(Qt.TextSelectableByMouse)
            else:
                label_qualifier = create_label(text = key.capitalize() + " : " + get_string(value))
            layout_gb.addWidget(label_qualifier)

        self.scroll_area_feature = create_scroll_area(widget=self.groupbox_feature)
        self.layout_feature.addWidget(self.scroll_area_feature)

    def create_groupbox_annot(self):
        self.groupbox_annot = create_groupbox(title='', flat=True)
        layout = self.centralwidget.layout()
        layout.addWidget(self.groupbox_annot)

        groupbox_gen = create_groupbox(title='Generalities')
        add_widget_to_groupbox(groupbox_gen, self.groupbox_annot)
        groupbox_org = create_groupbox(title="Organism")
        add_widget_to_groupbox(groupbox_org, self.groupbox_annot)

        annotations = self.product["annotations"]
        for key, value in annotations.items():
            if key == "references":
                continue
            elif key == "organism" :
                label = create_label(text = get_string(value), wordwrap=False)
                set_label_bold(label, True)
                add_widget_to_groupbox(label, groupbox_org)
            elif key == "taxonomy":
                for rank in annotations["taxonomy"]:
                    label = create_label(text=rank, wordwrap=False)
                    add_widget_to_groupbox(label, groupbox_org)
            else:
                label = create_label(text = key.capitalize() + " : " + get_string(value), wordwrap=False)
                add_widget_to_groupbox(label, groupbox_gen)

    def create_groupbox_ref(self):
        self.groupbox_ref = create_groupbox(title="References")
        self.groupbox_ref.setMinimumWidth(200)
        self.groupbox_ref.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        layout = self.centralwidget.layout()
        layout.addWidget(self.groupbox_ref)

        annotations = self.product["annotations"]
        for index, reference in enumerate(annotations["references"]):
            for key, value in reference.items():
                if key == "location":
                    location = create_feature_location(value[0])
                    label = create_label(text = str(index) + " : " + str(location))
                    set_label_bold(label, True)
                else:
                    label = create_label(text = key.capitalize() + " : " + get_string(value))
                add_widget_to_groupbox(label, self.groupbox_ref)

    def set_sequence(self, id):
        feature = self.product["features"][id]
        location_dict = feature["location"]
        location = create_feature_location(location_dict)
        title = str(location.start) + "-" + str(location.end)
        self.groupbox_feature.setTitle(title)
        sequence = self.product["seq"]["seq"]
        if location.start == 0 and location.end == len(sequence):
            cut_sequence = break_seq(sequence)
            self.label_seq.setText(cut_sequence)
        else:
            extract = location.extract(sequence)
            middle_sequence = "<span style='color:#ff0000;'>" + str(break_seq(extract)) + "</span>"
            position_start_feature = sequence.find(extract)
            position_end_feature = position_start_feature + len(extract)
            begin_sequence = sequence[:position_start_feature]
            end_sequence = sequence[position_end_feature:]
            sequence_finale = break_seq(begin_sequence) + middle_sequence + break_seq(end_sequence)
            self.label_seq.setText(sequence_finale)


