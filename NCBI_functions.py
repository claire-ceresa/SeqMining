from Bio import Entrez


def get_field_list(database_name):
    list = []
    database = Entrez.einfo(db=database_name)
    database_info = Entrez.read(database)
    field_list = database_info["DbInfo"]["FieldList"]
    field_list_sorted = sorted(field_list, key=lambda x: x["FullName"])
    for field in field_list_sorted:
        list.append(field["FullName"])
    return list
