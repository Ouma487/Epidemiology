import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches


from initialisation import *

def visualisation(A):

    fig, ax = plt.subplots()

    colors=['white', 'red','yellow','green','black' , 'magenta']
    #white:Sain
    #red:Infecté
    #yellow:Rétabli
    #green:Vacciné
    #black:Décédé
    #magenta:Personne en état fragile
    bounds=[0,1,2,3,4,5,6]
    cmap=mpl.colors.ListedColormap(colors)
    norm=mpl.colors.BoundaryNorm(bounds,cmap.N)
    
    # Ajouter la légende
    s=mpatches.Patch(color='white', label='Non fragile sain')
    i=mpatches.Patch(color='red', label='Infecté')
    r=mpatches.Patch(color='yellow', label='Rétabli')
    v=mpatches.Patch(color='green', label='Vacciné')
    d=mpatches.Patch(color='black', label='Décédé')
    f=mpatches.Patch(color='magenta',label='Fragile sain')
    plt.legend(handles=[s,i,r,v,d,f],bbox_to_anchor = (0.5, 0),loc='upper center')

    plt.imshow(A,interpolation='none',cmap=cmap,norm=norm) # fais une correspondance matrice grille avec des couleurs 
    ax.set_axis_off()
    plt.show()

    
    
a=initialisation(50,4)
print(visualisation(a))
    


