from Bio import Entrez, SeqIO,  SeqFeature, SeqRecord, Seq
from urllib import error
from functions.NCBI_functions import *
from functions.other_functions import *

class NCBI_Product:

    def __init__(self, id=None):
        self.id = id
        self.fiche = None
        self.sequence = None
        self.valid = True
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

    def get_feature_by_type(self, features, type):
        """
        Get all the information of a feature
        :param type: type of the feature you need (CDS, source, etc)
        :return: the old_object SeqFeature corresponding to the type
        """
        for feature in features:
            if feature.type == type:
                return feature
        return None

    ## TRANSFORMATION METHODS ##

    def get_product_as_dict(self):
        product = self.analyse_object(self.sequence)
        if "date" in product["annotations"]:
            date = product["annotations"]["date"]
            product["annotations"]["date"] = string_to_datetime(date)
        return product

    def analyse_object(self, object):

        if isinstance(object, list):
            final_temp = []
            for element in object:
                final_temp.append(self.analyse_object(element))
            if len(final_temp) == 1:
                final = final_temp[0]
            else:
                final = final_temp

        elif isinstance(object, dict):
            final = dict()
            for key, value in object.items():
                final[key] = self.analyse_object(value)

        elif isinstance(object, SeqFeature.Reference):
            final = {}
            attribute_references = ["location", "authors", "title", "journal", "comment"]
            for name in attribute_references:
                attribute = getattr(object, name)
                final[name] = self.analyse_object(attribute)

        elif isinstance(object, SeqRecord.SeqRecord):
            final = {}
            attribute_record = ["id", "name", "description", "seq", "dbxrefs", "letter_annotations", "annotations",
                                "features"]
            for name in attribute_record:
                attribute = getattr(object, name)
                final[name] = self.analyse_object(attribute)

        elif isinstance(object, Seq.Seq):
            final = str(object)

        elif isinstance(object, SeqFeature.SeqFeature):
            feature_type = object.type
            location = self.analyse_object(object.location)
            qualifiers = self.analyse_object(object.qualifiers)
            final = {"type": feature_type, "location": location, "qualifiers": qualifiers}

        else:
            final = object

        location_classes = get_location_classes()
        if type(object) in location_classes:
            final = str(object)

        return final



