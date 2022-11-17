import numpy as np
import time
from ezGraph import * 
from jStats import * 
import math 
# Finite Difference Model

#sinusoidal input = wave

#PARAMETERS
dt = 1
nsteps = 100

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

s_old = 0 #intial slope 
Qflag = True 
# TIME LOOP
for t in range (1, nsteps) :
    modelTime = t * dt

    # y = amplitude (height of wave from the midpoint) sin * (period (how much time it takes to go through the full cycle)) + vertical shift 
    Qin = 10 * math.sin (50 * modelTime) + 11

    if Qin <= 0:
        Qin = 0 

    #Filling
    dhin = Qin * dt / (np.pi * r **2) #find the change in height
    h = h + dhin #update height

    # Draining
    dVdt = -k * h
    dhout = dVdt * dt / (np.pi * r **2) #np.pi = pi 
    h = h + dhout

    dh = dhin + dhout 
    s = dh/dt
    if s < 0 and s_old > 0:
        print (f'Max height: {h}')
    elif s > 0 and s_old < 0:
        print (f'Min height: {h}')
    s_old = s * 1 
    
    graph.add (modelTime , h)
    #graph.wait (0.1) 
# DRAW GRAPH
graph.keepOpen ()
