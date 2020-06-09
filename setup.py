import sys
from cx_Freeze import setup, Executable

# Fichier setup pour la création d'un executable Python

# Pour créer l'executable via la console :
# Se positionner dans le dossier Python et lancer la commande "python setup.py build"


# Gestion des différents systèmes d'exploitation
# Si l'executable ne sera installé que sur Windows, rien à ajouter
# Sinon, ajouter les différents cas !
# sys.platform = "linux" pour un système Linux et "darwin" pour un système MacOS
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Creation de l'objet Executable
# 1. Nom du fichier Python qui permet de lancer le script
# 2. Nom de l'executable qui sera crée
# Si vous voulez modifier l'icone de l'executable, possibilité d'utiliser le paramètre icon
executable = [Executable("main.py", targetName="SeqMining.exe", base=base, icon="icone.ico")]

# Liste des packages utilise au sein du projet, afin de les compiler
packages = ["Bio", "os", "re", "math", "urllib","calendar", "datetime", "pymongo", "subprocess", "xlsxwriter"]

# Souvent tkinter est automatiquement compilé.
# S'il n'est pas utilisé dans le projet, il faut préciser de ne pas l'inclure
excludes = ['tkinter']

# Liste des fichiers Python (ou autre) à inclure
# Noter tous les fichiers qui appartiennent au projet
# Possibilite de tous les regrouper dans un sous dossier et dans ce cas, n'ecrire que le sous dossier
include_files = ["controllers",
                 "functions",
                 "objects",
                 "views",
                 "mongoDB.bat",
                 "icone.ico"]

# Creation du dictionnaire d'options
options = {
    "build_exe":
        {"packages": packages,
         "excludes": excludes,
         "include_files": include_files,
         "include_msvcr": True}}

# Fonction de setup
setup(
    name = "SeqMining",
    options = options,
    version = "1.0",
    description = 'Cree par Claire Ceresa. 09 juin 2020.',
    executables = executable
)