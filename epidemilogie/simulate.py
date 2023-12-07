from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from chgmt_etat2 import *
from initialisation import *

def simulate(univers,p,d1,d2,tmoy,tauv,tau,s,iter,inter):
    #p : la probabilité d'infection d'une personne non fragile
    #d1: la probabilité de décès d'une personne non fragile
    #d2 : la probabilité de décès d'une personne fragile
    #tmoy:le temps moyen de guérison d'une personne
    #tau:le taux de vaccination
    #iter:le nombre d'itération
    #s: le nombre minimal de voisins malades qu'une personne doit avoir pour que l'on ajoute à la liste des personnes à vacciner
    #inter:l'intervalle du temps entre un état et un autre


    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()    ##configure la figure 
    
    colors=['cyan', 'red','yellow','green','black' , 'magenta']
    #cyan:Sain
    #red:Infecté
    #yellow:Rétabli
    #green:Vacciné
    #black:Décédé
    #magenta:Personne en état fragile
    bounds=[0,1,2,3,4,5,6]
    cmap=mpl.colors.ListedColormap(colors)
    norm=mpl.colors.BoundaryNorm(bounds,cmap.N)
    
    def update(i):      ##la fonction qui me montre quel est la prochaine image
        x=chgmt_etat2(univers,p,d1,d2,tmoy, tauv,tau,s) #change l'univers avec les regles du jeu
        im_normed =x
        plt.imshow(im_normed,interpolation='none',cmap=cmap,norm=norm) # fais une correspondance matrice grille avec des couleurs 
        ax.set_axis_off()

    anim = FuncAnimation(fig, update, frames=iter, interval=inter)

    plt.show()
# vous pouvez modifier les parametres ci-dessous
N = 50  # N**2 est le nombre de personnes
m = 50  # m est le nombre de malade initial
p = 0.2 # probalité d'infection
d1 = 0.2 # probabilté de mourrir pour un malade non vulnerable
d2 = 0.4 # probabilté de mourrir pour un malade vulnerable
tmoy = 3 # temps moyen de guerrison/ decés d'un malade
tauv = 0.1 # proportion de vulnerables parmi les malades
tau = 0.01 # proportion de personnes vaccinées parmi toutes les personnes à vacciner dans une generation 
s = 1      # s est le nombre  minimal de malades dans le voisinage d'une personne saine pour que celle-ci soit mise dans la liste des personnes à vacciner
simulate(initialisation(N, m), p, d1, d2, tmoy,tauv,tau,s,300,100)

    
    
    
   
