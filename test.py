import sys
from Bio import Entrez, SeqIO, Seq, SeqFeature
from PyQt5.QtWidgets import *
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.NCBI_Product_Window import NCBI_Product_Window
from objects.MongoDB_Connexion import MongoDB_Connexion
from objects.DB_Product import DB_Product
from objects.NCBI_Product import NCBI_Product

Entrez.email= "claire.ceresa@hotmail.fr"
# app = QApplication(sys.argv)
#
# connexion = MongoDB_Connexion()
# client = connexion.client
# collection = connexion.collection

id = "KU762340.1"
product = NCBI_Product(id=id)
seq = product.sequence
print(seq)

# form = NCBI_Product_Window(id=id, connexion=connexion)
# form.show()
# app.exec()

