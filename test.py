from Bio import Entrez, SeqIO, Seq, SeqFeature
from PyQt5.QtWidgets import *
import sys
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.NCBI_Product_Window import NCBI_Product_Window
from controllers.DB_Product_test import DB_Product_TEST
from objects.MongoDB_Connexion import MongoDB_Connexion
from objects.DB_Product import DB_Product
from objects.NCBI_Product import NCBI_Product

Entrez.email= "claire.ceresa@hotmail.fr"
app = QApplication(sys.argv)

connexion = MongoDB_Connexion()
client = connexion.client
collection = connexion.collection

#product = NCBI_Product(id="GW214376.1") -> beug a tester
product = NCBI_Product(id="AY313605.1")
product_dict = product.get_product_as_dict()

form = DB_Product_TEST(product=product_dict)
layout = QVBoxLayout()
form.area_feature.setLayout(layout)
button_group = QButtonGroup()

features = product_dict["features"]
for feature in features:
    button = QRadioButton()
    button.setText(feature["type"])
    layout.addWidget(button)

form.show()
app.exec()
#
# id = "XM_031719044.1"
# fiche = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
# sequence = SeqIO.read(fiche, "genbank")
# seq = sequence.seq
#
# f = sequence.features[0]
# l = f.location
# print(l.__repr__())
#
# start = [int(l.start), l.start.__class__.__name__]
# end = [int(l.end), l.end.__class__.__name__]
# strand = l.strand
#
# print(start)
# print(end)
# print(strand)
#
# start_class = getattr(SeqFeature, start[1])
# start_position = start_class(start[0])
# end_class = getattr(SeqFeature, end[1])
# end_position = end_class(end[0])
# location = SeqFeature.FeatureLocation(start=start_position, end=end_position, strand=strand)
# print(location.__repr__())

