"""
Implement a relational join as a MapReduce query
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: Order/Line Item ID
    # value: Order/Line Item attributes
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: Order/Line Item ID
    # value: Order/Line Item attribute
    order_attributes =[]
    for row in list_of_values:
        # If record attribute is for the order as order has to preceed line item
        if row[0] =="order":
	    order_attributes = row
	    list_of_values.remove(row)
	    break
	    
    for row in list_of_values:
        mr.emit(order_attributes + row)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)