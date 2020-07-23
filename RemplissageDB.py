import subprocess
import pandas as pd
from datetime import datetime
from pymongo.errors import *
from objects.MongoDB_Connexion import MongoDB_Connexion
from objects.NCBI_Product import NCBI_Product

process = subprocess.Popen('mongoDB.bat')
connexion = MongoDB_Connexion()
ncbi_collection = connexion.get_collection("NCBI", "SeqMining")
coraliotech_collection = connexion.get_collection("Coraliotech", "SeqMining")

excel = pd.read_excel(r"C:/Users/claire/Desktop/Anthozoa - A importer.xlsx")
dataframe = pd.DataFrame(excel)
products = dataframe.where(pd.notnull(dataframe), None)

log = open("error.txt", "a")


for index, product in products.iterrows():
    id = product["Genbank"]
    ncbi_product = NCBI_Product(id=id)
    dict_ncbi = ncbi_product.get_product_as_dict()
    dict_ncbi["_id"] = id
    dict_ncbi["download_date"] = datetime.now()

    try:
        insert_ncbi = ncbi_collection.insert_one(dict_ncbi)
    except DocumentTooLarge:
        log.write(id + " : Document trop large\n")
    except DuplicateKeyError:
        log.write(id + " : Produit déjà téléchargé\n")
    except Exception as e:
        log.write(id + " : Impossible de télécharger le produit : "  + str(e) + "\n")

    else:
        dict_coraliotech = {"_id":id, "fonction":product["Fonction"], "sous-fonction":product["Sous-fonction"], "liens":[], "commentaires":[]}
        if product["UniProt"] is not None:
            lien_uniprot = "https://www.uniprot.org/uniprot/" + product["UniProt"]
            dict_coraliotech["liens"].append(lien_uniprot)
        if product["Autre"] is not None:
            dict_coraliotech["liens"].append(product["Autre"])

        try:
            insert_coraliotech = coraliotech_collection.insert_one(dict_coraliotech)
        except Exception as e:
            log.write(id + " : Impossible d'enregistrer : " + str(e) + "\n")
        else:
            print(str(index) + " / " + str(len(products)))

log.close()