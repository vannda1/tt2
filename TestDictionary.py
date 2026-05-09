from functools import reduce

import numpy as nm
import pandas as pd

def fns(a,b):
    return (a+b)

val=[1,2,3,4,5]
add=reduce(fns,val)
print(add)

add1=reduce(lambda a,b:a+b,val)
print(add1)








