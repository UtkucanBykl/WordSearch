from elasticsearch import Elasticsearch

es = Elasticsearch()

with open("english-words/words.txt", "r") as f:
    for count, line in enumerate(f):
        word = str(line).split("\n")[0]
        doc = {
            "word": word,
            "count": len(line),
            "letters": list(word)
        }
        print(doc)
        print(count)
        res = es.index(index="words", doc_type="words", id=count, body=doc)
        print(res["result"])