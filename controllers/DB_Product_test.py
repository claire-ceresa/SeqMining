from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from views.db_product_test import Ui_db_product_test
from functions.NCBI_functions import *
from functions.other_functions import *
from functions.graphics_function import *

class DB_Product_TEST(QtWidgets.QMainWindow, Ui_db_product_test):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, product=None):
        super(DB_Product_TEST, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(product["id"])
        self.product = product
        self.groupbox = None
        self._init_label_title()
        self._init_features()

    ## METHODS OF THE CLASS ##

    def button_feature_clicked(self, id):
        if self.groupbox is not None:
            self.groupbox.close()
            self.scroll_area_feature.close()
        self.creation_groupbox_feature(id)
        self.set_sequence(id)

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
        self.groupbox = QGroupBox()
        layout_gb = create_layout(vertical=True, spacer=True)

        feature = self.product["features"][id]
        for key, value in feature["qualifiers"].items():
            if not key == "translation":
                label_qualifier = create_label(text = key.capitalize() + " : " + get_string(value))
                layout_gb.addWidget(label_qualifier)
        self.groupbox.setLayout(layout_gb)

        self.scroll_area_feature = QScrollArea()
        self.scroll_area_feature.setWidgetResizable(True)
        self.scroll_area_feature.setWidget(self.groupbox)
        self.layout_feature.addWidget(self.scroll_area_feature)

    def set_sequence(self, id):
        feature = self.product["features"][id]
        location_dict = feature["location"]
        location = create_feature_location(location_dict)
        title = str(location.start) + "-" + str(location.end)
        self.groupbox.setTitle(title)
        sequence = self.product["seq"]["seq"]
        if location.start == 0 and location.end == len(sequence):
            cut_sequence = breakRNA(sequence)
            self.label_seq.setText(cut_sequence)
        else:
            extract = location.extract(sequence)
            middle_sequence = "<span style='color:#ff0000;'>" + str(breakRNA(extract)) + "</span>"
            position_start_feature = sequence.find(extract)
            position_end_feature = position_start_feature + len(extract)
            begin_sequence = sequence[:position_start_feature]
            end_sequence = sequence[position_end_feature:]
            sequence_finale = breakRNA(begin_sequence) + middle_sequence + breakRNA(end_sequence)
            self.label_seq.setText(sequence_finale)


