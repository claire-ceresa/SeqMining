from Bio import Entrez
from PyQt5.QtWidgets import QApplication
import sys
from controllers.NCBI import NCBI

Entrez.email= "claire.ceresa@hotmail.fr"

request = "stylophora [Organism] AND mRNA [Title] AND cds [Title] "

app = QApplication(sys.argv)
form = NCBI()
form.show()
app.exec()


