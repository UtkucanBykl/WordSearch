from elasticsearch import Elasticsearch

class Elastic:

    def __init__(self):

        self.__es = Elasticsearch()

    def search_with_count(self, gte, index="words", doc_type="words"):

        body = {"query": {
            "range": {
                "count": {
                    "gte": int(gte),
                }
            }
        }
        }
        result = self.__es.search(index=index, doc_type=doc_type, body=body)
        return [x for x in result["hits"]["hits"]]

e = Elastic()
a = e.search_with_count(index="words", gte=20)
for b in a:
    print(b["_source"])