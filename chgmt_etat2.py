import numpy as np 
import random as rd 
import math as math
from copy import deepcopy

from initialisation import *

def voisins(univers, x,y):
    #Cette fonction détermine les coordonnées des voisins d'une personne de coordonnées (x,y)
    #univers=initialisation(N,m,f)
    s= np.shape(univers)
    n  = s[0] 
    a = (x+1) % n # on fait des ajouts/soustractions modulo les tailles pour gérer les effets de bord
    b = (y+1)% n
    c = (x-1)% n
    d = (y-1)% n
    return( np.array( [[a , d] , [a , y] , [a , b] , [x , d] , [x , b] , [c , d] ,[c , y] , [c , b]] )  )

def nbr_vois_malade(G, x , y):
    #La fonction détermine le nombre des voisins malade d'une personne de coordonnées (x,y)
    #G est une deepcopy de l'univers
    Y = G[x][y]
    V = voisins(G, x, y)
    m = 0 # nombre de malades
    for x in V:
        i , j = x[0] , x[1]
        if G[i][j] == 1 : #on compte le nombre de personnes malades
            m+=1
    return m


       
def survival(G,x,y,p,d1,d2, tmoy): 
    #p : la probabilité d'infection
    #d1: la probabilité de décès d'une personne non fragile
    #d2: la probabilité de décès d'une personne fragile (d2>d1)
    #G est une deepcopy de l'univers
    #tmoy: temps moyenne
    Y = G[x][y] # on s'intéresse à la case à changer
    V = voisins(G,x,y)
    m = nbr_vois_malade(G, x, y)

    if Y == 0: #la personne est saine
        
        r = rd.random() #on introduit le hasard 
        if m==0:
            return 0
        if m != 0 and  p > r**m : #la personne a été contaminée
            return 1
        else:  #la personne n'a pas été contaminée
            return 0
    if Y == 5: # la personne malade est fragile
        r = rd.random()
        r2 = rd.random()
        if r2<(1/tmoy):
            if r<d2:
                return 4
            else:
                return 2  
        else:
            return 5             
    if Y == 1: #la personne est malade 
        r = rd.random()
        r2= rd.random()
        if r2 < (1/tmoy):
            if r < d1: #la personne meurt
                return 4 
            else: #la personne guérit et est immunisée
                return 2
    
        else:
            return 1
    else:
        return Y          

def vaccination(L,tau,univers): 
    #L est la liste de coordonnées des personnes saines 
    #tau:taux de vaccination
    N = len(L) #nombre de personnnes saines
    k = math.ceil(N*tau) # nombre de personnes qui vont être vaccinées
    L_Vac = []
    i=0
    while i <= k:                                      
        r = rd.random()               # construction de la liste des personnes à vacciner 
        for e in L:
            x , y = e[0] , e[1]
            m = nbr_vois_malade(univers, x, y)
            if r > (1/2)**m and [x,y] not in L_Vac:
                L_Vac.append([x,y])
                i+=1
    for coordonees in L_Vac:
        x,y = coordonees[0], coordonees[1]
        univers[x][y] = 3
    
            



def vulnerable(L,tauv,univers):#L liste de personnes malades,tauv:taux de vulnérabilité

    N = len(L) #nombre de personne malade
    k = math.ceil(N*tauv) # nombre de personnes qui sont vulnerables
    L_Vac = rd.sample(L,k) #liste des coordonnées des personnes vulnerables
    for coordonees in L_Vac:
        x,y = coordonees[0], coordonees[1]
        univers[x][y] = 5 
      

def chgmt_etat2(univers,p, d1,d2,tmoy,tauv,tau,s):#s est un seuil de vaccination,tmoy:tamps moyen de rétablissament,tau:la proportion des gens vaccinés parmis la liste des gens à vacciner
    n,m=np.shape(univers)
    G= deepcopy(univers)
    for x in range(n):
        for y in range(m):
            univers[x][y] = survival(G,x,y,p,d1,d2, tmoy)
    K=[] #liste des personnes malades
    L= [] #liste de personnes saines 
    for x in range(n):
        for y in range(m):
            if univers[x][y] == 0 and nbr_vois_malade(G, x,y)>=s:
                L.append([x,y])
            if  univers[x][y]==1:
                K.append([x,y])

    vulnerable(K,tauv, univers)
    vaccination(L,tau,univers)
    
    
    return univers 
