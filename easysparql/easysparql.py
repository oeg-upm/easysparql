from SPARQLWrapper import SPARQLWrapper, JSON
import logging
from time import sleep
import random


def get_logger(name, level=logging.INFO):
    # logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=level)
    logger = logging.getLogger(name)
    return logger


logger = get_logger(__name__, level=logging.INFO)


def run_query(query, endpoint):
    """
    :param query: raw SPARQL query
    :param endpoint: endpoint source that hosts the data
    :return: query result as a dict
    """
    sparql = SPARQLWrapper(endpoint=endpoint)
    sparql.setQuery(query=query)
    sparql.setMethod("POST")
    sparql.setReturnFormat(JSON)
    try:
        results = sparql.query().convert()
        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"]
        else:
            logger.debug("returns 0 rows")
            logger.debug("query: <%s>" % str(query).strip())
            return []
    except Exception as e:
        logger.warning(str(e))
        logger.warning("sparql error: $$<%s>$$" % str(e))
        logger.warning("query: $$<%s>$$" % str(query))
        return None


def get_entities(subject_name, endpoint, language_tag=None):
    """
    assuming only in the form of name@en. To be extended to other languages and other types e.g. name^^someurltype
    :param subject_name:
    :param endpoint
    :return:
    """
    if language_tag is None:
        query = """
            select distinct ?s where{
                ?s ?p "%s"@en
            }
        """ % (subject_name)
    else:
        query = """
            select distinct ?s where{
                ?s ?p "%s"%s
            }
        """ % (subject_name, language_tag)

    results = run_query(query=query, endpoint=endpoint)
    entities = [r['s']['value'] for r in results]
    return entities


def get_classes(entity, endpoint):
    """
    :param entity: entity url without <>
    :param endpoint:
    :return:
    """
    query = """
        select distinct ?c where{
        <%s> a ?c
        }
    """ % entity
    results = run_query(query=query, endpoint=endpoint)
    classes = [r['c']['value'] for r in results]
    return classes


def get_parents_of_class(class_uri, endpoint):
    """
    get the parent class of the given class, get the first results in case of multiple ones
    :param class_uri:
    :param endpoint:
    :return:
    """
    query = """
    select distinct ?c where{
    <%s> rdfs:subClassOf ?c.
    }
    """ % class_uri
    results = run_query(query=query, endpoint=endpoint)
    classes = [r['c']['value'] for r in results]
    return classes


def get_num_class_subjects(class_uri, endpoint):
    logger.debug("count subject for class %s" % class_uri)
    query = """
    select count(?s) as ?num
    where {
    ?s a ?c.
    ?c rdfs:subClassOf* <%s>.
    }
    """ % class_uri
    results = run_query(query=query, endpoint=endpoint)
    if results != []:
        return results[0]['num']['value']
    else:
        return -1


def get_classes_subjects_count(classes, endpoint):
    logger.debug("in get_classes_subjects_count")
    d = {}
    for c in classes:
        num = get_num_class_subjects(c, endpoint)
        d[c] = int(num)
    return d