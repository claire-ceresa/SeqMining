from PyQt5 import QtWidgets
from urllib import error
from Bio import Entrez, SeqIO
from views.ncbi_product_view import Ui_NCBI_Product
from functions.graphics_function import *


class NCBI_Product_Window(QtWidgets.QMainWindow, Ui_NCBI_Product):
    """
    controlling class for ncbi_product_view
    """

    def __init__(self, parent=None, id=None):
        super(NCBI_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.id = id
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.id)
        self.label_dispo.setText("Le produit n'est pas disponible hors ligne !")
        self.label_dispo.setStyleSheet("color: rgb(255, 0, 0);")
        self._set_fiche()

    def button_download_clicked(self):
        # TODO : create database
        print("ok")

    def _set_fiche(self):
        try:
            fiche = Entrez.efetch(db="nucleotide", id=self.id, rettype="gb", retmode="text")
        except error.HTTPError:
            create_messageBox("Erreur", "Identifiant inconnu !")
            # TODO : close window when wrong id
        else:
            sequence = SeqIO.read(fiche, "genbank")
            SeqIO.write(sequence, "fiche.txt", "genbank")
            text = open('fiche.txt').read()
            self.plainTextEdit.setPlainText(text)
