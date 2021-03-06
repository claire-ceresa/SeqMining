from views.db_product_view import Ui_db_product
from controllers.Project_Widget import Project_Widget
from widgets.Product_Groupbox import Product_Groupbox
from objects.DB_Product import DB_Product
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
        self.product = DB_Product(data=product)
        self.groupbox_feature = None
        self.layout_annot = None
        self.layout_ref = None
        self.layout_project = None
        self._init_ui()

    ## METHODS OF THE CLASS ##

    def button_feature_clicked(self, id):
        """Set the groupbox with the elements of the feature"""
        if self.groupbox_feature is not None:
            self.groupbox_feature.close()
            self.scroll_area_feature.close()
        self.creation_groupbox_feature(id)
        self.set_sequence(id)

    def action_gen_toggled(self, checked):
        """Open the groupbox with the elements of the annotations of the product"""
        clear_layout(self.layout_gb_1)
        if checked:
            self.create_annotations()
        else:
            self._init_coraliotech()

    def action_ref_toggled(self, checked):
        """Open the groupbox with the elements of the references of the product (if existed)"""
        if self.action_projet.isChecked() == checked:
            clear_layout(self.layout_gb_2)
            self.action_projet.setChecked(False)
        if checked:
            self.create_ref()


    def action_projet_toggled(self, checked):
        """Open the groupbox dealing with the project associated to the product"""
        if self.action_ref.isChecked() == checked:
            clear_layout(self.layout_gb_2)
            self.action_ref.setChecked(False)
        if checked:
            self.create_project()
        else:
            clear_layout(self.layout_gb_2)

    def action_commentaire_clicked(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Ajouter", "Commentaire:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            action = add_value_to_product(where= {'id':self.product.data["id"]},
                                 array='coraliotech.comments',
                                 value= text)
            if action["error"] is not None:
                create_messageBox("Erreur", "Une erreur est survenue !\n" + str(action['error']))

    def action_lien_clicked(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Ajouter", "Lien:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            action = add_value_to_product(where= {'id':self.product.data["id"]},
                                 array='coraliotech.links',
                                 value= text)
            if action["error"] is not None:
                create_messageBox("Erreur", "Une erreur est survenue !\n" + str(action['error']))

    ## GRAPHIC INIT METHODS ##

    def _init_ui(self):
        """Initialize the different graphic items"""
        self.action_commentaire.triggered.connect(self.action_commentaire_clicked)
        self.action_lien.triggered.connect(self.action_lien_clicked)
        self._init_label_title()
        self._init_features()
        self._init_source()
        if "coraliotech" in self.product.data:
            self._init_coraliotech()
        if "references" not in self.product.data['annotations']:
            self.action_ref.setEnabled(False)

    def _init_label_title(self):
        """Initialize the title of the product"""
        self.label_id.setText(self.product.data["id"])
        self.label_descr.setText(self.product.data["description"])
        date_string = get_string(self.product.data["download_date"])
        self.label_download.setText("Téléchargé le " + date_string)

    def _init_features(self):
        """Initialize the groupbox with the list of all the features of the product"""
        widgets = []

        features = self.product.data["features"]
        for id, feature in enumerate(features):
            button = create_radio_button(feature["type"])
            widgets.append(button)

        self.groupbutton = create_button_group(widgets=widgets, )
        layout = create_layout(widgets=widgets, vertical=True)
        self.area_button.setLayout(layout)
        self.groupbutton.buttonClicked['int'].connect(self.button_feature_clicked)

    def _init_source(self):
        """Initialize the feature source when the window open"""
        button = self.groupbutton.button(0)
        if button is not None:
            button.setChecked(True)
            self.button_feature_clicked(0)

    def _init_coraliotech(self):
        """Initialize Coraliotech caracteristics when the window open"""
        datas = self.product.data["coraliotech"]
        datas["taille"] = self.product.get_length()
        datas["poids"] = self.product.get_molecular_weight()
        self.groupbox_coraliotech = Product_Groupbox(datas=datas, type="Coraliotech")
        self.layout_gb_1.addWidget(self.groupbox_coraliotech)

    ## GRAPHIC METHODS of the groupboxes ##

    def creation_groupbox_feature(self, id):
        """Fill in the groupbox with the elements of the feature selected"""
        self.groupbox_feature = create_groupbox()
        feature = self.product.data["features"][id]
        for key, value in feature["qualifiers"].items():
            if key == "translation":
                cut_sequence = break_seq(sequence=value[0], step=60)
                label_qualifier = create_label(text = key.capitalize() + " :\n" + " ".join(cut_sequence), wordwrap=True)
                label_qualifier.setTextInteractionFlags(Qt.TextSelectableByMouse)
            else:
                label_qualifier = create_label(text = key.capitalize() + " : " + get_string(value))
            add_widget_to_groupbox(widget=label_qualifier, groupbox=self.groupbox_feature)

        self.scroll_area_feature = create_scroll_area(widget=self.groupbox_feature, frame=False)
        self.layout_feature.addWidget(self.scroll_area_feature)

    def create_annotations(self):
        """Fill in the groupbox with the element of the annotations dict of the product"""
        self.groupbox_gen = Product_Groupbox(type="Generalities")
        self.groupbox_org = Product_Groupbox(type="Organism")
        self.layout_gb_1.addWidget(self.groupbox_gen)
        self.layout_gb_1.addWidget(self.groupbox_org)
        annotations = self.product.data["annotations"]

        for key, value in annotations.items():
            if key == "references":
                continue
            elif key == "organism" :
                label = create_label(text = get_string(value), wordwrap=False)
                set_label_bold(label, True)
                self.groupbox_org.add_widget(label)
            elif key == "taxonomy":
                for rank in annotations["taxonomy"][::-1]:
                    label = create_label(text=rank, wordwrap=False)
                    self.groupbox_org.add_widget(label)
            else:
                label = create_label(text = key.capitalize() + " : " + get_string(value), wordwrap=False)
                self.groupbox_gen.add_widget(label)

    def create_ref(self):
        """Fill in the groupbox with the element of the references of the product"""
        datas = self.product.data["annotations"]
        self.groupbox_ref = Product_Groupbox(datas=datas, type="References")
        self.layout_gb_2.addWidget(self.groupbox_ref)

    def create_project(self):
        """Fill in the groupbox with the list of projects associated to the product"""
        self.groupbox_proj = Product_Groupbox(datas=self.product.data, type="Projects")
        self.layout_gb_2.addWidget(self.groupbox_proj)

        label_add = create_label("Ajouter à un autre projet")
        set_label_clickable(label_add)
        label_add.mouseReleaseEvent = self.add_to_a_project
        self.layout_button = create_layout([label_add], vertical=True)
        self.layout_gb_2.addLayout(self.layout_button)

        spacer = create_spacer(vertical=True)
        self.layout_gb_2.addItem(spacer)

    ## METHODS concerning the sequence ##

    def set_sequence(self, id):
        """Fill in the sequence"""
        sequence = self.product.data["seq"]["seq"]
        feature = self.product.data["features"][id]
        location_dict = feature["location"]
        location = create_feature_location(location_dict)
        self.groupbox_feature.setTitle(str(location))
        if "positions" in location_dict:
            self.colore_compound_location(location, sequence)
        else:
            if location.start == 0 and location.end == len(sequence):
                break_sequence = break_seq(sequence=sequence)
                self.label_seq.setText(" ".join(break_sequence))
            else:
                self.colore_feature_location(location, sequence)

    def cut_sequence(self, extract, sequence):
        """Cut the part of the sequence concerning by the feature selected"""
        middle = "<span style='color:#ff0000;'>" + extract + "</span>"
        position_start_feature = sequence.find(extract)
        position_end_feature = position_start_feature + len(extract)
        begin = sequence[:position_start_feature]
        end = sequence[position_end_feature:]
        return [begin, middle, end]


    def colore_feature_location(self, location, sequence):
        """Colore in red the part of the sequence concerning by the feature selected"""
        extract = location.extract(sequence)
        cut_sequence = "".join(self.cut_sequence(extract, sequence))
        break_sequence = break_seq(sequence=sequence, sequence_color=cut_sequence)
        sequence_finale = " ".join(break_sequence)
        self.label_seq.setText(sequence_finale)

    def colore_compound_location(self, location, all_sequence):
        """Colore in red the part of the sequence concerning by the feature selected"""
        all_cut_part = []
        sequence = all_sequence
        for part in location.parts:
            if part.ref is None:
                extract = part.extract(all_sequence)
                cut_sequence = self.cut_sequence(extract, sequence)
                all_cut_part.append(cut_sequence[0])
                all_cut_part.append(cut_sequence[1])
        all_cut_part.append(cut_sequence[2])
        sequence_finale = "".join(all_cut_part)
        break_seq_finale = break_seq(all_sequence, sequence_finale)
        self.label_seq.setText( " ".join(break_seq_finale))


    ## METHODS concerning the project associated ##

    def add_to_a_project(self, event):
        """When button Add clicked, open the combobox to choose the new project"""
        projects = get_not_project_for_a_product(self.product.data["id"])
        project_name = extract_list_of_attribute(projects, "name")
        self.combobox_project = create_combobox(project_name)
        label_ok = create_label("Ok")
        set_label_clickable(label_ok)
        label_ok.mouseReleaseEvent = self.save_product_in_project
        layout = create_layout([self.combobox_project, label_ok], horizontal=True)
        self.layout_button.addLayout(layout)

    def save_product_in_project(self, event):
        """When button Saved clicked, save the product to the project selected"""
        name = self.combobox_project.currentText()
        adding = add_product_to_project(id=self.product.data["id"], project=name)
        if adding["nModified"] != 1:
            create_messageBox("Erreur", "Impossible d'ajouter le produit au projet")
        else:
            project = get_one_project(name=name)
            widget = Project_Widget(project=project, statut="Product", product=self.product.data)
            self.groupbox_proj.add_widget(widget)