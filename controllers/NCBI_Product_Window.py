from PyQt5 import QtWidgets
from views.ncbi_product_view import Ui_NCBI_Product
from functions.graphics_function import *
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product


class NCBI_Product_Window(QtWidgets.QMainWindow, Ui_NCBI_Product):
    """
    controlling class for ncbi_product_view
    """

    def __init__(self, parent=None, id=None, connexion=None):
        super(NCBI_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.mongoDB_connexion = connexion
        self.ncbi_product = NCBI_Product(id=id)
        self.db_product = DB_Product(id=self.ncbi_product.id, data=self.ncbi_product.get_product_as_dict())
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.ncbi_product.id)
        self._init_fiche()
        self._init_label_available()

    def button_download_clicked(self):
        saving = self.db_product.save_on_db(collection=self.mongoDB_connexion.collection)
        if saving["error"] is not None:
            create_messageBox("Attention", saving["error"])
        else:
            create_messageBox("Succès !", "Le produit" + saving["id"] + "a été téléchargé")
        self._init_label_available()

    def _init_fiche(self):
        if self.ncbi_product.valid:
            text = open('fiche.txt').read()
            self.plainTextEdit.setPlainText(text)

    def _init_label_available(self):
        existed = self.db_product.existed_in_collection(self.mongoDB_connexion.collection)

        if existed is None:
            self.label_dispo.setText("Le produit n'est pas disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.label_dispo.setText("Le produit est disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(0, 200, 0);")
            self.button_download.hide()




