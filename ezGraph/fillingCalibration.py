import numpy as np
import time
from ezGraph import * 
from jStats import * 
# Finite Difference Model

#PARAMETERS
dt = 1
nsteps = 30

r = 2.25 # r a d i u s (cm)
Qin = 30 # Volume inflow rate (dV/dt) : (cubic cm/s)
h = 0 #intial height (cm)
k = 0.0 #outflow rate constant

# EXPERIMENTAL DATA
x_measured = [1, 7, 12, 17, 22, 26]
y_measured = [0, 10, 20, 30, 40, 50]
y_modeled = []

# GRAPH
graph = ezGraphMM (xmin=0, xmax=100,
            xLabel= "Time (s)", 
            yLabel= "Height (cm)", 
            x_measured = x_measured,
            y_measured = y_measured)

graph.addModeled (0, h) # add intial vaules 

# TIME LOOP
for t in range (1, nsteps) :
    modelTime = t * dt

    #Filling
    dh = Qin * dt / (np.pi * r **2) #find the change in height

    h = h + dh #update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r **2) #np.pi = pi 
    h = h + dh

    if (modelTime in x_measured):
        print(modelTime , h)
        y_modeled.append (h)
    graph.addModeled (modelTime , h)
    #graph.wait (0.8)

print("h_measured", y_measured)
print("h_modelded", y_modeled)

#my average 
print("h_measured average:", myAvg(y_measured),y_measured)
print("h_modeled average:", myAvg(y_modeled))

#residuals 
r = residual (y_measured, y_modeled)
print (f'residual = {r}')

#difference from the mean 
print (f'difference: {dsq (y_measured)}')

#Rs value 
print ("R2:", rSquared (y_measured, y_modeled))

# DRAW GRAPH
graph.keepOpen ()

#MODEL: Something that imitates another closely that can perdict the future. 
    #A represent of the real word. 
        # --- requires some data about the real world.
    # -  analytical model: Equation or function that represents or best fits the data. 
        # -- linear, polynomial, exponential, sinusodal, logarithmic, hyperbolic, radical. 
        # -- plug in a input and the equation gives the output
            # --- h (t) = 2 t + 7 
            # --- input = t 
            # --- output = h 
        # - only works for well behaved systems. Not a whole lot of interactions that introduce errors. Non-chaotic. 
        # - often calculus to find equations. 
    # - physical models: 
        # -- small scale physical things (you can touch it)
        # -- can be more complex 
        # -- problems with scalling (you have to make sure it is accurate)
    # - numerical models:
        # -- usually computer models because there's a lot of calculations (algebraic)
        # -- usually break the system into smaller parts that interact with each other. 
        # -- the computer is used to keep track of all the interactions. 
        # -- we'll focus on things that CHANG OVER TIME. And focus on FINITE DIFFERENCE models (finite means not infinite).