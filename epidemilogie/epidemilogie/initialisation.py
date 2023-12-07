import numpy as np
from random import *

def initialisation(N, m ): 
    #N est la racine carré du nombre de la population
    #m est le nombre des personnes infectées à l'instant initial
    
    t= [[0 for i in range(N)] for j in range(N)]
    
    n1 = 0
    while n1 != m:
        i = choice(range(N))
        j = choice(range(N))
        if t[i][j] == 0:
            t[i][j] = 1
            n1+=1

        
    return t 
