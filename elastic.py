from elasticsearch import Elasticsearch

class Elastic:

    def __init__(self):

        self.__es = Elasticsearch()

    def search_with_count(self, gte, index="words", doc_type="words"):

        body = {
  "query": {
    "bool": {
      "should": [
        {
          "match": {
              "letters":{
                    "query":"a b d",
                  "operator": "and"
              }

          }
        },
        {
          "range": {
            "count": {
              "gte": 10
            }
          }
        }
      ],
      "minimum_should_match": 2
    }
  }
}


        result = self.__es.search(index=index, doc_type=doc_type, body=body)
        return [x for x in result["hits"]["hits"]]

e = Elastic()
a = e.search_with_count(index="words", gte=20)
for b in a:
    print(b["_source"])