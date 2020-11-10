import requests

class MySQL_Connexion:

    def __init__(self):
        self.datas = None
        self.load_datas()

    def load_datas(self):
        session = requests.session()
        resp = session.get("http://www.coraliotech.com/app/python_datas.php")
        self.datas = resp.json()

    def run_on_php(self, queries):
        for query in queries:
            try:
                # /!\ a envoyer a request.post : {'query':str}
                r = requests.post("http://www.coraliotech.com/app/python_post.php", data=query)
            except Exception as e:
                return {'sent': False, 'error': query + " :" + str(e)}
            if r.status_code != 200:
                return {'sent': False, 'error': query + '\nLa requete n\'a pas abouti !'}
        return {'sent': True, 'error': None}

    def create_query_update(self, table, values, where=None):
        if len(values) > 0:
            query = "UPDATE " + table + " SET "
            string_values = []
            for key, value in values.items():
                string_values.append(key + " = " + value)
            query = query + " , ".join(string_values)
            if where is not None:
                query = query + " WHERE " + list(where.keys())[0] + " = " + where[list(where.keys())[0]]
            return query
        else:
            return None

    def create_query_insert(self, table, values):
        if len(values) > 0:
            query = 'INSERT INTO ' + table + ' (' + ' , '.join(values.keys()) + ') VALUES (' + ' , '.join(values.values()) + ')'
            return query
        else:
            return None

    def create_query_delete(self, table, where):
        where_text = []
        for variable, value in where.items():
            where_text.append(variable + " = " + value)
        query = "DELETE FROM " + table + " WHERE " + " AND ".join(where_text)
        return query


    # GETTER METHODS

    def get_all_products(self):
        all_products = []
        for index, product in enumerate(self.datas["products"]):
            all_products.append(product)
            product_types = []

            for type in self.datas["types"]:
                if type["product"] == product["name"]:
                    product_types.append(type["type"])
            all_products[index]["types"] = product_types

        return all_products

    def get_all_app(self):
        return self.datas['apps']

    def get_app_of_domain(self, domain):
        names = []
        for app in self.datas['apps']:
            if app['domain'] == domain:
                names.append(app['name'])
        return names

    def get_all_types(self):
        types = {}
        for product in self.datas['products']:
            types[product['name']] = []
            for type in self.datas['types']:
                if product['name'] == type['product']:
                    types[product['name']].append(type['type'])
        return types

    def get_all_species(self):
        return self.datas["species"]

    def get_species_product(self):
        product_species = {}
        for product in self.datas['products']:
            product_species[product['name']] = []
            for species in self.datas['species_product']:
                if product['name'] == species['product']:
                    product_species[product['name']].append(species['species'])
        return product_species

    def get_species_type(self):
        type_species = {}
        for product, types in self.get_all_types().items():
            for type in types:
                type_species[type] = []
                for species in self.datas["species_type"]:
                    if type == species["type"]:
                        type_species[type].append(species['species'])
        return type_species

    def get_species_product_type(self):
        datas = []
        for product in self.datas['products']:
            product_datas = {'name': product['name'], 'species': [], 'types': []}
            for species in self.datas['species_product']:
                if product['name'] == species['product']:
                    product_datas['species'].append(species['species'])
            types = self.get_all_types()[product['name']]
            for type in types:
                type_datas = {'name': type, 'species': []}
                for species in self.datas["species_type"]:
                    if type == species["type"]:
                        type_datas['species'].append(species['species'])
                product_datas['types'].append(type_datas)
            datas.append(product_datas)
        return datas


    def get_product_app(self):
        product_app = {}
        for product in self.datas["products"]:
            product_app[product["name"]] = []
            for p_a in self.datas["product_app"]:
                if p_a["product"] == product["name"]:
                    product_app[product["name"]].append(p_a["application"])
        return product_app

    def get_all_users(self):
        return self.datas["users"]



