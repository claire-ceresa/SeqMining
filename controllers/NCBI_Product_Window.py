from PyQt5 import QtWidgets
from urllib import error
from Bio import Entrez, SeqIO
from views.ncbi_product_view import Ui_NCBI_Product
from functions.graphics_function import *
from objects.NCBI_Product import NCBI_Product


class NCBI_Product_Window(QtWidgets.QMainWindow, Ui_NCBI_Product):
    """
    controlling class for ncbi_product_view
    """

    def __init__(self, parent=None, id=None):
        super(NCBI_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.product = NCBI_Product(id=id)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.product.id)
        self._init_fiche()
        self._init_label_available()

    def button_download_clicked(self):
        # TODO : create database
        print("ok")

    def _init_fiche(self):
        if self.product.valid :
            text = open('fiche.txt').read()
            self.plainTextEdit.setPlainText(text)

    def _init_label_available(self):
        if self.product.available_on_db:
            self.label_dispo.setText("Le produit est disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(0, 200, 0);")
            self.button_download.hide()
        else:
            self.label_dispo.setText("Le produit n'est pas disponible hors ligne !")
            self.label_dispo.setStyleSheet("color: rgb(255, 0, 0);")



