from Bio import Entrez, SeqIO, Seq
from PyQt5.QtWidgets import QApplication
import sys
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
# id = "GW214376.1"
#
# form = NCBI_Product_Window(id=id, connexion=connexion)
# form.show()
# app.exec()

id = "XM_031719044.1"
fiche = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
sequence = SeqIO.read(fiche, "genbank")
seq = sequence.seq

print(isinstance(seq, Seq.Seq))
print(str(seq))
print(str(seq.alphabet))
