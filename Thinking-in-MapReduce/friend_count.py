"""
Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a 
friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0] 
    friend = record[1] 
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_values):
    # key: order_id
    # value: elements/attributes
    num_friends = 0
    for friend in list_of_values:
        num_friends += 1
    mr.emit((key, num_friends))
	#want to combine each lineitem to each order, one at a time
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    