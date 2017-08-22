# python2
#  All imports
import os
from datetime import datetime
from multiprocessing import Pool
import multiprocessing
import itertools
from functools import partial

def workerWithMultiArguments(type_values,weights):
   calculation_type=type_values[0]
   weight=weights[calculation_type]
   value= type_values[1] 
   result = value * weight

   return calculation_type, value,result

# build iteration list
type_values=[]

# build prob list
labels = ['type1','type2']
values = [1,2,3,4,5,6,7,8,9]
weights = { 
  'type1' : 2,
  'type2' : 3
}

list_combine = [labels, values]

# cartesian product
for element in itertools.product(*list_combine):
    type_values.append(element)

print type_values
print weights

start_time = datetime.now()

# start 30 processes and gather results
#processes=multiprocessing.cpu_count()
nProcesses=16
pool = Pool(processes=nProcesses)
result=pool.map(partial(workerWithMultiArguments,weights=weights), type_values)
pool.close()

end_time = datetime.now()

print result
