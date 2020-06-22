import sys
import subprocess
from Bio import Entrez, SeqIO, Seq, SeqFeature
from PyQt5.QtWidgets import *
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.NCBI_Product_Window import NCBI_Product_Window
from controllers.DB_Search_Window import DB_Search_Window
from controllers.DB_Product_Window import DB_Product_Window
from controllers.Project_Window import Project_Window
from objects.MongoDB_Connexion import MongoDB_Connexion
from objects.DB_Product import DB_Product
from objects.NCBI_Product import NCBI_Product
from functions.db_functions import *

process = subprocess.Popen('mongod.exe')
Entrez.email= "claire.ceresa@hotmail.fr"
app = QApplication(sys.argv)

product = get_one_product("KU902046.1")
form = DB_Product_Window(product=product)

form.show()
app.exec()
process.terminate()

