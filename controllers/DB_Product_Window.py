from views.db_product_view import Ui_db_product
from functions.graphics_function import *
from functions.other_functions import *


class DB_Product_Window(QtWidgets.QMainWindow, Ui_db_product):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, product=None):
        super(DB_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(product["id"])
        self.product = product
        self._init_ui()

    def _init_ui(self):
        self._init_label_title()
        self._init_generalities()
        self._init_features()

    def _init_label_title(self):
        self.label_id.setText(self.product["id"])
        self.label_descr.setText(self.product["description"])
        date_string = get_string(self.product["download_date"])
        self.label_download.setText("Téléchargé le " + date_string)
        self.edit_seq.setPlainText(self.product["seq"]["seq"])

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

    def _init_features(self):
        features = self.product["features"]
        for feature in features:
            try:
                groupbox = QtWidgets.QGroupBox()
                title = ''
                if 'type' in feature:
                    title = title + feature['type']
                if 'location' in feature:
                    title = title + " " + feature['location']
                groupbox.setTitle(title)
                layout_gb = create_layout(vertical=True, spacer=True)
                groupbox.setLayout(layout_gb)

                for key, value in feature["qualifiers"].items():
                    if not key == "translation":
                        label_key = create_label(text=key.capitalize() + " : ")
                        label_value = create_label(text=get_string(value))
                        layout_lb = create_layout([label_key, label_value], horizontal=True, spacer=True)
                        layout_gb.addLayout(layout_lb)

                self.layout_features.addWidget(groupbox)
            except Exception as e:
                print(e)



