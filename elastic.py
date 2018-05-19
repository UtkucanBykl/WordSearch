from elasticsearch import Elasticsearch

from kelimelik import Word


class Elastic(Word):

    def __init__(self):

        self.__es = Elasticsearch()
        super(Word).__init__()

    def search_with_count(self, index="words", doc_type="words"):
        body = {
  "query": {
    "bool": {
      "should": [
        {
          "match": {
              "letters": {
                    "query": self.word,
                  "operator": "and"
              }

          }
        },
        {
          "range": {
            "count": {
              "gte": self.count
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
e.word = "d e"
e.count = 10
data = e.search_with_count()
for word in data:
    print(word["_source"])
