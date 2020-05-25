from Bio import Entrez, SeqIO, SeqFeature


def get_field_list(database_name):
    """
    Get all the fields of a database
    :param database_name: the name of the NCBI_Search_Window database
    :return: list of the field names
    """
    list = []
    database = Entrez.einfo(db=database_name)
    database_info = Entrez.read(database)
    field_list = database_info["DbInfo"]["FieldList"]
    field_list_sorted = sorted(field_list, key=lambda x: x["FullName"])
    for field in field_list_sorted:
        list.append(field["FullName"])
    return list


def get_result_request(request, retmax, retstart):
    """
    Launch a research on NCBI_Search_Window
    :param request: the NCBI_Search_Window request
    :return: result of the request, an object DictionaryElement
    """
    result = Entrez.esearch(db="nucleotide", term=request, idtype="acc", retstart=retstart, retmax=retmax, usehistory='y')
    list = Entrez.read(result)
    return list


def get_location_classes():
    classes = [SeqFeature.FeatureLocation,
               SeqFeature.CompoundLocation,
               SeqFeature.ExactPosition,
               SeqFeature.WithinPosition,
               SeqFeature.BetweenPosition,
               SeqFeature.BeforePosition,
               SeqFeature.AfterPosition,
               SeqFeature.OneOfPosition,
               SeqFeature.UnknownPosition]
    return classes


def get_sequence(id):
    """
    Get the all sequence for an id
    :param id : GenBank identifiant
    :return: SeqIO object
    """
    fiche = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    sequence = SeqIO.read(fiche, "genbank")
    return sequence


def get_summary(id):
    """
    Get a summary of a sequence
    :param id: GenBank identifiant
    :return: ListElement object
    """
    handle = Entrez.esummary(db="nucleotide", id=id)
    record = Entrez.read(handle)
    return record
