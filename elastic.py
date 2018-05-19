from elasticsearch import Elasticsearch

class Elastic:

    def __init__(self):

        self.__es = Elasticsearch()

    def search_with_count(self, gte, letters, index="words", doc_type="words"):

        body = {
  "query": {
    "bool": {
      "should": [
        {
          "match": {
              "letters": {
                    "query": letters,
                  "operator": "and"
              }

          }
        },
        {
          "range": {
            "count": {
              "gte": gte
            }
          }
        }
      ],
    }
  }
}


        result = self.__es.search(index=index, doc_type=doc_type, body=body)
        return [x for x in result["hits"]["hits"]]

e = Elastic()
a = e.search_with_count(index="words", gte=10, letters="a b c d")
for b in a:
    print(b["_source"])