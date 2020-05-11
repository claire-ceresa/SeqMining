from Bio import Entrez
from PyQt5.QtWidgets import QApplication
import sys
from controllers.Request import Request

Entrez.email= "claire.ceresa@hotmail.fr"

request = "stylophora [Organism] AND mRNA [Title] AND cds [Title] "

app = QApplication(sys.argv)
form = Request()
form.show()
app.exec()


