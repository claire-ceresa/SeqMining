import sys
import json
import subprocess
from Bio import Entrez, SeqIO, Seq, SeqFeature
from PyQt5.QtWidgets import *
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.NCBI_Product_Window import NCBI_Product_Window
from controllers.DB_Search_Window import DB_Search_Window
from controllers.DB_Product_Window import DB_Product_Window
from controllers.Project_Window import Project_Window
from controllers.Gestion_Window import Gestion_Window
from objects.MongoDB_Connexion import MongoDB_Connexion
from objects.DB_Product import DB_Product
from objects.NCBI_Product import NCBI_Product
from objects.MySQL_Connexion import MySQL_Connexion
from functions.db_functions import *
from ftplib import FTP
import requests

# process = subprocess.Popen('mongoDB.bat')
# Entrez.email= "claire.ceresa@hotmail.fr"
app = QApplication(sys.argv)
form = Gestion_Window()
form.show()
app.exec()
# process.terminate()


# id ="KC777188.1"
# datas = get_one_product(id=id)
# product = DB_Product(id=id)
# app = QApplication(sys.argv)
# form = DB_Product_Window(product=datas)
# form.show()
# app.exec()

# keys = {"id": "test"}
# r = requests.post("http://www.coraliotech.com/app/test.php", data = keys)
#
# print(r.url)
# print(r.status_code)