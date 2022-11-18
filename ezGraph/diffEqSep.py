import numpy as np 
from ezGraph import * 

#initialization 
dx = 0.1 
xold, yold = 0, 10

nsteps = 100

graph = ezGraph (xmin=0, xmax=6, ymin=0, ymax=20)

#loop calculations 
for i in range (nsteps): 
    x = xold + dx
    dydx = -yold
    dy = dydx * dx 
    y = yold + dy  #the new value  = to the old value + the change 

    graph.add(x,y)

    #update for next step
    xold = x 
    yold = y 

#post processing 
graph.keepOpen()
