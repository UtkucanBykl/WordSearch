# WordSearch

### What is this ?

Finds words containing the given letters

### Example

````python
from elastic import Elastic

e = Elastic()
data = e.search_with_count(letters="a b c", gte=10, index="your_index", doc_type="your_doc_type")

for word in data:
    print(word["_source"])

````


## ToDo

- API
- Class Fix