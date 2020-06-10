import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from controllers.Principal_Window import Principal
from Bio import Entrez

Entrez.email = "claire.ceresa@hotmail.fr"

process = subprocess.Popen('mongod.exe')
app = QApplication(sys.argv)
form = Principal()
form.show()
form.mongoDB_connexion.close()
app.exec()
process.terminate()