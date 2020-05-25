from Bio import Entrez
from PyQt5.QtWidgets import QApplication
import sys
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.NCBI_Product_Window import NCBI_Product_Window

Entrez.email= "claire.ceresa@hotmail.fr"
request = "stylophora [Organism] AND mRNA [Title] AND cds [Title] "
id =  "LSMT01000001.1"
#id =  "XM_022924805.1"
#id = "EU159467.1"
app = QApplication(sys.argv)
form = NCBI_Search_Window()
#form = NCBI_Product_Window(id=id)
form.show()
app.exec()