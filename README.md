# WordSearch

### What is this ?

Finds words containing the given letters

### Example

````python
from elastic import Elastic

e = Elastic()
e.word = "d e"
e.count = 10
data = e.search_with_count(index="your_index", doc_type="yor_doc_type")
for word in data:
    print(word["_source"])

````


## ToDo

- API
- Class Fix