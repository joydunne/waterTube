import numpy as np
import time
from ezGraph import * 
from jStats import * 

#equilibrium is to find when the graph levels off

#primary equation: hnew = hold + dh 
#filling dh = dt/pi*r^2*Q
#draining dh = dt/pi*r^2(-kh)

# Finite Difference Model
startTime = time.perf_counter()

#PARAMETERS
dt = 15
nsteps = 500

r = 2.25 # radius (cm)
Qin = 30 # Volume inflow rate (dV/dt) : (cubic cm/s)
h = 0 #intial height (cm)
k = 0.15 #outflow rate constant

# EXPERIMENTAL DATA
y_modeled = []

# GRAPH
graph = ezGraph (xmin=0, xmax=100,
            xLabel= "Time (s)", 
            yLabel= "Height (cm)")

graph.add(0, h) # add intial vaules 

conv = 0.1 # the change between one point and the next one. Will be referred to later in the code.
# TIME LOOP
for t in range (1, nsteps) :
    modelTime = t * dt

    h_old = h #update height 

    #Filling
    dh = Qin * dt / (np.pi * r **2) #find the change in height
    h = h + dh

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r **2) #np.pi = pi 
    h = h + dh

    graph.add(modelTime , h)
    #graph.wait (0.8)

    #finding the change in height 
    dh = h - h_old 
    #stopping the graph at equalibrium 
    if dh < conv:
        break 
print (h)

endTime = time.perf_counter()

runTime - endTime - startTime
print (f'runtime: {runTime}')


# DRAW GRAPH
graph.keepOpen ()