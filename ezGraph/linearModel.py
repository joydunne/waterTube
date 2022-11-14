import numpy as np #numpy mean numerical python. a module for math stuff
import time
from ezGraph import * # * stand for everything (wildcard)

# Model
# h = -20.5t + 552

# PARAMETERS
dt = .25 #floating point number
nsteps = 164

# linear model 
m = -20.5 
b = 552

#GRAPH 
graph = ezGraph(xmax = 31) # changes the length of the graph 

# TIME LOOP
for t in range (nsteps):
    modelTime = t * dt
    h = m * modelTime + b 
    print (modelTime, h) 
    graph.add (modelTime, h)
    #graph.wait (0.1)

#graph.keepOpen() #keeps the graph open 

#60 seconds = -678.0
#100 seconds = -1498.0
#40.25 = -273.125cm 