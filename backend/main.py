# from types import prepare_class
# import rdfextras
# rdfextras.registerplugins()

# import rdflib

# g = rdflib.Graph()
# filename = "../data/owl_dulich_nb_v2.owl"

# g.parse(filename, format='xml')

# value = "hoa lư"

# query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX xml: <http://www.w3.org/XML/1998/namespace>
#         PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#         PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
#         SELECT DISTINCT ?name
#         WHERE
#         {
#         ?x ex:tenTour ?name.
#         FILTER(regex(lcase(?name),\""""+value+"""\"))
#         }
#         """
# rows = g.query(query)
# for row in rows:
#     print(row.name)
import json
from blbase import BLBase

bl = BLBase()

print(json.dumps(bl.filter(1, "hoa lư").__dict__, ensure_ascii=False))
