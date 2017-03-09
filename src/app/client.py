import requests

ENDPOINT = "http://virtuoso.clariah-sdh.eculture.labs.vu.nl/sparql"

# query = """
# SELECT DISTINCT ?g WHERE {{
#         GRAPH ?g {{[] ?p [] .}}
# }} LIMIT 10 OFFSET {}
# """


query = """
PREFIX np: <http://www.nanopub.org/nschema#>
PREFIX qb: <http://purl.org/linked-data/cube#>

SELECT DISTINCT ?np ?pi ?a ?p ?ds WHERE {{
    ?np  a np:Nanopublication ;
        np:hasPublicationInfo ?pi ;
        np:hasAssertion ?a ;
        np:hasProvenance ?p .
    OPTIONAL {{
        GRAPH ?a {{
   	        ?dst a qb:DataSet .
        }}
    }}
    BIND(IF(bound(?dst), ?dst, "noname") AS ?ds)
}} ORDER BY ?ds, ?np LIMIT 100 OFFSET {}
"""


def get_datasets():
    offset = 0
    all_datasets = []
    while True:
        print "Offset: {}".format(offset)
        q = query.format(offset)
        print q

        response = requests.get(ENDPOINT, params={'query': q}, headers={'Accept': 'application/sparql-results+json'})
        results = response.json()

        datasets = []
        for r in results['results']['bindings']:
            dataset_result = {}
            for k in r.keys():
                dataset_result[k] = r[k]['value']
            datasets.append(dataset_result)

        print "Retrieved {} datasets".format(len(datasets))
        if len(datasets) < 1:
            break
        # print datasets
        all_datasets += datasets
        offset += 100

    return all_datasets
