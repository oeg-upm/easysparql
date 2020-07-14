from easysparql import easysparql

DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"

albert_uri = "http://dbpedia.org/resource/Albert_Einstein"
albert_name = "Albert Einstein"
scientist = "http://dbpedia.org/ontology/Scientist"
foaf_name = "http://xmlns.com/foaf/0.1/name"


classes = easysparql.get_classes(albert_uri, DBPEDIA_ENDPOINT)
print("classes: ")
print(classes[:3])

entities = easysparql.get_entities(albert_name, DBPEDIA_ENDPOINT, "@en")
print("entities: ")
print(entities[:3])


parents = easysparql.get_parents_of_class(scientist, DBPEDIA_ENDPOINT)
print("parents: ")
print(parents[:3])

query = "select distinct ?Concept where {[] a ?Concept} LIMIT 100"
results = easysparql.run_query(query, DBPEDIA_ENDPOINT)
print("Query result: ")
print(results[:3])


subjects = easysparql.get_subjects(class_uri=scientist, endpoint=DBPEDIA_ENDPOINT)
print("subjects: ")
print(subjects[:3])


properties = easysparql.get_properties_of_subject(subject_uri=albert_uri, endpoint=DBPEDIA_ENDPOINT)
print("properties: ")
print(properties[:3])


num = easysparql.get_property_count(subject_uri=albert_uri, property_uri=foaf_name, endpoint=DBPEDIA_ENDPOINT)
print("count: ")
print(num)

