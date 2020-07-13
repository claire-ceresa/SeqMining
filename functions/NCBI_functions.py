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


def break_seq(sequence, sequence_color=None, step=10):
    position_outside = 0
    parts = []
    part = ""
    x = 0

    if sequence_color is None:
        sequence_color = sequence

    while x < len(sequence):
        c = sequence_color[position_outside]
        if c == "<":
            position_inside = position_outside
            while c != ">":
                part = part + c
                position_inside = position_inside + 1
                c = sequence_color[position_inside]
            else:
                part = part + c
                position_inside = position_inside + 1
                c = sequence_color[position_inside]
                position_outside = position_inside

        else:
            if x % step == 0 and x != 0:
                parts.append(part)
                part = c
            else:
                part = part + c
            position_outside = position_outside + 1
            x = x + 1

    parts.append(part)
    return parts


def create_feature_location(dict):
    if "positions" in dict and len(dict["positions"]) > 1:

        positions = []
        for part in dict["positions"]:
            position = create_feature_location(part)
            positions.append(position)
        location = SeqFeature.CompoundLocation(positions, operator=dict["operator"])
    else:
        start_class = getattr(SeqFeature, dict["start"][1])
        start_position = start_class(dict["start"][0])
        end_class = getattr(SeqFeature, dict["end"][1])
        end_position = end_class(dict["end"][0])
        strand = dict["strand"]
        ref = dict["ref"]
        location = SeqFeature.FeatureLocation(start=start_position, end=end_position, strand=strand, ref=ref)
    return location