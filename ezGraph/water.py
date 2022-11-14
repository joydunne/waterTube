import numpy as np #numpy mean numerical python. a module for math stuff
import time
from ezGraph import * # * stand for everything (wildcard)

# Model
# h = 2t - 3.22

# PARAMETERS
dt = 0.5 #floating point number
nsteps = 61

# linear model 
m = 2 
b = -3.22

#GRAPH 
graph = ezGraph(xmax = 40) # changes the length of the graph 

# TIME LOOP
for t in range (nsteps):
    modelTime = t * dt
    h = m * modelTime + b 
    print (modelTime, h) 
    graph.add (modelTime, h)
    graph.wait (0.1)

graph.keepOpen() #keeps the graph open 
