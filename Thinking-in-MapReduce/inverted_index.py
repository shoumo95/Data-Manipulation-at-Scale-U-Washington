"""
Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is 
associated with a list of the document identifiers in which that word appears.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier, document_id
    # value: document text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: List of Document IDs
    document_id_list =[]
    for v in list_of_values:
        # No previous entry in the document ID list
        if v not in document_id_list:
            document_id_list.append(v)
    mr.emit((key, document_id_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)