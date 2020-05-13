from Bio import Entrez
from PyQt5.QtWidgets import QApplication
import sys
#from controllers.NCBI_Result_Window import NCBI
from controllers.NCBI_Product_Window import NCBI_Product_Window

Entrez.email= "claire.ceresa@hotmail.fr"

request = "stylophora [Organism] AND mRNA [Title] AND cds [Title] "

app = QApplication(sys.argv)
#form = NCBI()
form = NCBI_Product_Window(id="EU159467.1")
form.show()
app.exec()


