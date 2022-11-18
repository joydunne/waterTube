import numpy as np 
from ezGraph import * 
import math 

#initialization 
dx = 0.1 
xold, yold = 0, 0

nsteps = 500

graph = ezGraph (xmin=0, xmax=6, ymin=0, ymax=20)

#loop calculations 
for i in range (nsteps): 
    x = xold + dx
    if x > 0 and x < 10:
        dydx = math.sin(xold)
        dy = dydx * dx 
        y = yold + dy  #the new value  = to the old value + the change 

        graph.add(x,y)

        #update for next step
        xold = x 
        yold = y 

#post processing 
graph.keepOpen()
