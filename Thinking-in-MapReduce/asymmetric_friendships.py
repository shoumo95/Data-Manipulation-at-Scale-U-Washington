"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric 
friend relationships.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    pairlist=tuple(sorted(record)) 
    mr.emit_intermediate(pairlist, 1)
    #since the pairlist is sorted, symmetric friendships will have a duplicate key
	#ex: the key-value ( [adam,smith], 1) exists twice if there exists both
	#( [adam,smith], 1) and ( [smith,adam], 1)
	
def reducer(key, list_of_values):
	#if len(list_of_values)==2, then we have symmetric_friendship
	#ex. (self.intermediate[(adam,smith)].append(1 1)
	#where "1" got appended twice
    if len(list_of_values)==1:
        mr.emit((key[0],key[1]))
        mr.emit((key[1],key[0])) #need this line also because 
	#["Myriel", "Count"] exists in friends.json, but ["Count", "Myriel"] doesn't
	#so instead of just saying ["Myriel", "Count"] is a (person,friend)
	#["Count","Myriel"] also is a (person,friend)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    