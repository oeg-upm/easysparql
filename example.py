from easysparql.easysparql import run_query, get_entities, get_classes, get_parents_of_class

DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"

albert_uri = "http://dbpedia.org/resource/Albert_Einstein"
albert_name = "Albert Einstein"
scientist = "http://dbpedia.org/ontology/Scientist"


classes = get_classes(albert_uri, DBPEDIA_ENDPOINT)
print("classes: ")
print(classes[:3])

entities = get_entities(albert_name, DBPEDIA_ENDPOINT, "@en")
print("entities: ")
print(entities[:3])


parents = get_parents_of_class(scientist, DBPEDIA_ENDPOINT)
print("parents: ")
print(parents[:3])

query = "select distinct ?Concept where {[] a ?Concept} LIMIT 100"
results = run_query(query, DBPEDIA_ENDPOINT)
print("Query result: ")
print(results[:3])

