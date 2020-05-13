from Bio import Entrez, SeqIO
from urllib import error


class NCBI_Product:

    def __init__(self, id=None):
        self.id = id
        self.fiche = None
        self.sequence = None
        self.valid = True
        self.available_on_db = False # TODO : gérer la comparaison avec la db
        self._set_properties()

    # SETTER METHODS #

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

    # GETTER METHODS #

    def get_id(self):
        return self.sequence.id

    def get_name(self):
        return self.sequence.name

    def get_description(self):
        return self.sequence.description

    def get_features(self):
        return self.sequence.features

    def get_sequence_DNA(self):
        return self.sequence.seq

    def get_annotations(self):
        return self.sequence.annotations

    def get_letter_annotations(self):
        return self.sequence.letter_annotations

    def get_dbxrefs(self):
        return self.sequence.dbxrefs
