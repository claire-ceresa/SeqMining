import sys
from PyQt5.QtWidgets import QApplication
from controllers.Request import Request
from Bio import Entrez

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Request()
form.show()
app.exec()