import numpy as np
import time
from ezGraph import * 
from jStats import * 
# Finite Difference Model

#PARAMETERS
dt = 5
nsteps = 200

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

# TIME LOOP
for t in range (1, nsteps) :
    modelTime = t * dt

    if modelTime > 50:
        Qin = 0 

    #Filling
    dh = Qin * dt / (np.pi * r **2) #find the change in height
    h = h + dh #update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r **2) #np.pi = pi 
    h = h + dh

    graph.add (modelTime , h)
    #graph.wait (0.1)

# DRAW GRAPH
graph.keepOpen ()
