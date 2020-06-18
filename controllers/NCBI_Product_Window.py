from views.ncbi_product_view import Ui_NCBI_Product
from functions.graphics_function import *
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product


class NCBI_Product_Window(QtWidgets.QMainWindow, Ui_NCBI_Product):
    """
    controlling class for ncbi_product_view
    """

    def __init__(self, parent=None, id=None):
        super(NCBI_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.ncbi_product = NCBI_Product(id=id)
        self.db_product = DB_Product(id=self.ncbi_product.id, data=self.ncbi_product.get_product_as_dict())
        self._init_ui()

    # METHODS OF THE CLASS #

    def button_download_clicked(self):
        """Save the product on the MongoDB database"""
        saving = self.db_product.saved_on_db()
        if saving["error"] is not None:
            create_messageBox("Attention", saving["error"])
        else:
            create_messageBox("Succès !", "Le produit " + saving["id"] + " a été téléchargé")
        self._init_label_available()

    def button_extract_clicked(self):
        """Extract the NCBI page to a text file"""
        file = get_directory()
        title = file + "/" + self.ncbi_product.id + ".txt"
        try:
            self.ncbi_product.create_txt_file(title= title)
        except Exception as e:
            create_messageBox("Erreur !", "Le fichier n'a pas pu etre crée !\n" + str(e))
        else:
            create_messageBox("Succès !", "Le fichier a été enregistré !")

    # GRAPHIC METHODS #

    def _init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(self.ncbi_product.id)
        self._init_fiche()
        self._init_label_available()

    def _init_fiche(self):
        """Initialize the fiche issued of NCBI"""
        self.ncbi_product.create_txt_file()
        if self.ncbi_product.valid:
            text = open('fiche.txt').read()
            self.edit_fiche.setPlainText(text)

    def _init_label_available(self):
        """Initialize the label for availability"""
        existed = self.db_product.existed_in_collection()
        if existed:
            self.label_dispo.setText("Le produit est disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(0, 200, 0);")
            self.button_download.hide()
        else:
            self.label_dispo.setText("Le produit n'est pas disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(255, 0, 0);")

