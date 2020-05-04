from Bio import Entrez
from PyQt5.QtWidgets import QApplication
import sys
from controllers.Result import Result

Entrez.email= "claire.ceresa@hotmail.fr"

request = "stylophora [Organism] AND mRNA [Title] AND cds [Title] "

app = QApplication(sys.argv)
form = Result(request=request)
form.show()
app.exec()


