import sys
from PyQt5.QtWidgets import QApplication
from controllers.Principal import Principal
from Bio import Entrez

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Principal()
form.show()
app.exec()