import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from controllers.Principal_Window import Principal
from Bio import Entrez

Entrez.email = "claire.ceresa@hotmail.fr"

process = subprocess.Popen('mongoDB.bat')
app = QApplication(sys.argv)
form = Principal()
form.show()
app.exec()
process.terminate()
