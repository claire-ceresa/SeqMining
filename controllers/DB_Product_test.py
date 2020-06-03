from PyQt5.QtWidgets import *
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
        self._init_sequence()

    def button_feature_clicked(self, id):
        if self.groupbox is not None:
            self.groupbox.close()
            self.scroll_area_feature.close()

        self.groupbox = QGroupBox()
        feature = self.product["features"][id]
        layout_gb = create_layout(vertical=True, spacer=True)
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

    def _init_buttons(self):
        self.group = QButtonGroup()
        widget = []
        features = self.product["features"]
        for id, feature in enumerate(features):
            button = QRadioButton()
            button.setText(feature["type"])
            self.group.addButton(button, id)
            widget.append(button)
        layout = create_layout(widgets=widget, vertical=True)
        self.area_button.setLayout(layout)
        self.group.buttonClicked['int'].connect(self.button_feature_clicked)
        button = self.group.button(0)
        if button is not None:
            button.setChecked(True)
            self.button_feature_clicked(0)

    def _init_sequence(self):
        sequence = self.product["seq"]["seq"]
        list_sequence = breakRNA(sequence)
        cut_sequence = " ".join(list_sequence)
        self.label_seq.setText(cut_sequence)

    def _init_generalities(self):
        parent = self.tree_widget
        for key, value in self.product["annotations"].items():
            self.creation_tree(parent, key, value)
        self.tree_widget.resizeColumnToContents(0)
        self.tree_widget.resizeColumnToContents(1)

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

