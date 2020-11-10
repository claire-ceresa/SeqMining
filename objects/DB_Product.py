from datetime import datetime
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from functions.db_functions import *
from functions.other_functions import *


class DB_Product:

    """Object representing a product available on the database"""

    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data

    def existed_in_collection(self):
        """Check if the id existed in the collection"""
        result = get_one_product(self.id)
        if result is None:
            return False
        else:
            return True

    def saved_on_db(self):
        """
        Save the product on the database
        :return: {'id':str, 'error':str or None}
        """
        self.data["_id"] = self.id
        self.data["download_date"] = datetime.now()
        return save_product(self.data)

    def get_id(self):
        return self.data["_id"]

    def get_description(self):
        return self.data["description"]

    def get_protein_name(self):
        feature_cds = self.get_feature_by_type("CDS")
        if "qualifiers" in feature_cds:
            if "product" in feature_cds["qualifiers"]:
                return feature_cds["qualifiers"]["product"][0]
        return None

    def get_sequence(self):
        return self.data["seq"]["seq"]

    def get_length(self):
        return len(self.data["seq"]["seq"])

    def get_species(self):
        if "organism" in self.data["annotations"]:
            return self.data["annotations"]["organism"]
        else:
            return None

    def get_molecular_weight(self):
        translation = self.get_translation()
        if translation is not None:
            analysed_seq = ProteinAnalysis(translation)
            try:
                return round(analysed_seq.molecular_weight() * 0.001)
            except:
                return None
        return None

    def get_translation(self):
        feature_cds = self.get_feature_by_type("CDS")
        if feature_cds is not None:
            if "qualifiers" in feature_cds:
                if "translation" in feature_cds["qualifiers"]:
                    return feature_cds["qualifiers"]["translation"][0]
        return None

    def get_feature_by_type(self, type):
        for feature in self.data["features"]:
            if feature["type"] == type:
                return feature
        else:
            return None

    def get_projects(self):
        id = self.get_id()
        projects = get_all_projects_for_a_product(id)
        if len(projects) > 0:
            list_project = extract_list_of_attribute(list_old=projects, attribute="name")
            return ", ".join(list_project)
        else:
            return None