import numpy as np 
import random as rd 
import math as math
from copy import deepcopy

from initialisation import *

def voisins(univers, x,y):
    s= np.shape(univers)

    n  = s[0] 
    a = (x+1) % n # on fait des ajouts/soustractions modulo les tailles pour gerer les effets de bord
    b = (y+1)% n
    c = (x-1)% n
    d = (y-1)% n
    return( np.array( [[a , d] , [a , y] , [a , b] , [x , d] , [x , b] , [c , d] ,[c , y] , [c , b]] )  )




def survival(G,x,y,p,d): #G est une deepcopy de l'univers
    Y = G[x][y] # on s'intéresse à la case à changer
    V = voisins(G,x,y)

    if Y == 0: #la personne est saine
        m = 0 # nombre de malades
        for x in V:
            i , j = x[0] , x[1]
            if G[i][j] == 1 : #on compte le nombre de personnes malades
                m+=1
        r = rd.random() #on introduit le hasard 
        if m==0:
            return 0
        if m!=0:
            
            if    p**(1/m) > r : #la personne a été contaminée
                return 1
            else :  #la personne n'a pas été contaminée
                return 0

    if Y == 1: #la personne est malade 
        r = rd.random()
        if r > d: #la personne meurt
            return 4 
        else: #la personne guérit et est immunisée
            return 2
    if Y!=0 and Y!=1:               ## dans les autres cas on ne change pas d'etat
        return Y



def vaccination(L,tau,univers): #L est la liste de coordonnées des personnes saines ,tau est le taux d'efficacite du vaccin
    N = len(L) #nombre de personnnes saines
    k = int(N*tau) # nombre de personnes qui vont être vaccinées
    L_Vac = rd.sample(L,k) #liste des coordonnées des personnes vaccinées
    for coordonees in L_Vac:
        x,y = coordonees[0], coordonees[1]
        univers[x][y] = 3 

def changement_etat(univers,p,d,tau):
    n,m=np.shape(univers)
    G= deepcopy(univers)
    for x in range(n):
        for y in range(m):
            univers[x][y] = survival(G,x,y,p,d)
    L= [] #liste de personnes saines 
    for x in range(n):
        for y in range(m):
            if univers[x][y] == 0:
                L.append([x,y])
    vaccination(L,tau,univers)
    return univers 

    





    






            
        




