from Bio import Entrez, SeqIO
from urllib import error

class NCBI_Product:

    def __init__(self, id=None):
        self.id = id
        self.fiche = None
        self.sequence = None
        self.valid = True
        self.available_on_db = True # TODO : gérer la comparaison avec la db
        self._set_properties()

    def _set_properties(self):
        self._set_fiche()
        if self.fiche is not None:
            self._set_sequence()

    def _set_fiche(self):
        try:
            fiche = Entrez.efetch(db="nucleotide", id=self.id, rettype="gb", retmode="text")
        except error.HTTPError:
            self.valid = False
        else:
            self.fiche = fiche

    def _set_sequence(self):
        sequence = SeqIO.read(self.fiche, "genbank")
        self.sequence = sequence
        SeqIO.write(self.sequence, "fiche.txt", "genbank")
