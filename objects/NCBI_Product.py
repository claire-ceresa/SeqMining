from Bio import SeqRecord, Seq
from urllib import error
from functions.NCBI_functions import *
from functions.other_functions import *

class NCBI_Product:

    """Object representing a product available online on NCBI"""

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

    # TRANSFORMATION METHODS #

    def create_txt_file(self, title=None):
        if title is None:
            SeqIO.write(self.sequence, "fiche.txt", "genbank")
        else:
            SeqIO.write(self.sequence, title, "genbank")

    def get_product_as_dict(self):
        """Transform the product as a dictionnary"""
        product = self.analyse_object(self.sequence)
        if "date" in product["annotations"]:
            date = product["annotations"]["date"]
            product["annotations"]["date"] = string_to_datetime(date)
        return product

    def analyse_object(self, object):
        """Analyse an object and transform it to simple object (str, int, dict, list)"""
        if isinstance(object, list):
            final = []
            for element in object:
                final.append(self.analyse_object(element))

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
            final = {"seq": str(object), "alphabet": str(object.alphabet)}

        elif isinstance(object, SeqFeature.SeqFeature):
            feature_type = object.type
            location = self.analyse_object(object.location)
            qualifiers = self.analyse_object(object.qualifiers)
            final = {"type": feature_type, "location": location, "qualifiers": qualifiers}

        elif isinstance(object, SeqFeature.FeatureLocation):
            start = [int(object.start), object.start.__class__.__name__]
            end = [int(object.end), object.end.__class__.__name__]
            strand = object.strand
            ref = object.ref
            final = {"start": start, "end": end, "strand": strand, "ref": ref}

        elif isinstance(object, SeqFeature.CompoundLocation):
            operator = object.operator
            parts = object.parts
            positions = []
            for part in parts:
                position = self.analyse_object(part)
                positions.append(position)
            final = {"positions": positions, "operator": operator}

        else:
            final = object

        return final



