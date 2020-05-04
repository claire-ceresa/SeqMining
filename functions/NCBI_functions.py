from Bio import Entrez, SeqIO


def get_field_list(database_name):
    list = []
    database = Entrez.einfo(db=database_name)
    database_info = Entrez.read(database)
    field_list = database_info["DbInfo"]["FieldList"]
    field_list_sorted = sorted(field_list, key=lambda x: x["FullName"])
    for field in field_list_sorted:
        list.append(field["FullName"])
    return list


def get_list_ids(request):
    result = Entrez.esearch(db="nucleotide", term=request, idtype="acc", retmax=2500, usehistory='y')
    list = Entrez.read(result)
    if 'ErrorList' in list:
        ids = []
    else:
        ids = list["IdList"]
    return ids


def get_sequence(id):
    fiche = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    sequence = SeqIO.read(fiche, "genbank")
    return sequence


def get_summary(id):
    handle = Entrez.esummary(db="nucleotide", id=id)
    record = Entrez.read(handle)
    return record
