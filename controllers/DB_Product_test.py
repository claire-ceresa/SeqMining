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
        #self._init_generalities()
        self._init_buttons()
        #self._init_sequence()

    ## METHODS OF THE CLASS ##

    def button_feature_clicked(self, id):
        if self.groupbox is not None:
            self.groupbox.close()
            self.scroll_area_feature.close()
        self.creation_groupbox_feature(id)
        self.set_sequence(id)

    ## GRAPHIC METHODS ##

    def _init_buttons(self):
        self.creation_group_button()
        self._init_source()

    # def _init_sequence(self):
    #     sequence = self.product["seq"]["seq"]
    #     cut_sequence = breakRNA(sequence)
    #     self.label_seq.setText(cut_sequence)

    def _init_generalities(self):
        parent = self.tree_widget
        for key, value in self.product["annotations"].items():
            self.creation_tree(parent, key, value)
        self.tree_widget.resizeColumnToContents(0)
        self.tree_widget.resizeColumnToContents(1)

    def _init_source(self):
        button = self.groupbutton.button(0)
        if button is not None:
            button.setChecked(True)
            self.button_feature_clicked(0)

    def creation_tree(self, parent, key, value):
        child = QtWidgets.QTreeWidgetItem(parent)
        string_key = key.replace("_", " ")
        child.setText(0, string_key.capitalize())

        if isinstance(value, list) and isinstance(value[0], dict):
            parent = child
            for index, element in enumerate(value):
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, str(index+1))
                if isinstance(element, dict):
                    for key, value in element.items():
                        self.creation_tree(child, key, value)

        elif isinstance(value, dict):
            for key, value in value.items():
                self.creation_tree(child, key, value)

        else:
            child.setText(1, get_string(value))

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
                label_key = create_label(text=key.capitalize() + " : ")
                label_value = create_label(text=get_string(value))
                layout_lb = create_layout([label_key, label_value], horizontal=True, spacer=True)
                layout_gb.addLayout(layout_lb)
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
            begin_sequence = sequence[:position_start_feature-1]
            end_sequence = sequence[position_end_feature+1:]
            sequence_finale = breakRNA(begin_sequence) + middle_sequence + breakRNA(end_sequence)
            self.label_seq.setText(sequence_finale)


