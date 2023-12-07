# Epidémiologie


Pour notre projet de deuxième semaine des CODING WEEKS,nous avons décidé de faire une modélisation de la propagation d'une épidémie dans une population de taille N,nous utilisons le modèle de prédiction  epidemiologique SIRVD  (Susceptible, Infected, Recovered, Vaccinated, Deceased).

## Membres du groupe SOSA

 - Sara Abkari (Staffeur Forum)
 - Amadou Bassirou Diallo
 - Cyprien Fourcoy
 - Samara Ndiaye
 - Oumaima Chater

## Description 

Nous adoptons un modèle SIRVD (Susceptible, Infected, Recovered, Vaccinated, Deceased),mais avec une petite modification,nous tenons compte aussi des personnes fragiles,qui sont une probabilité de décès plus grande que les autres personnes.
Chaque personne est représentée par une case et son état est représenté par une couleur:

 - Sain=>Blanc

 - Infecté non fragile=>Rouge

 - Infecté fragile=>Magenta
            
 - Rétabli=>Jaune
            
 - Vacciné=>Vert
            
 - Mort =>Noir

 
            
Sa position dans l’espace correspond à sa position sur la grille. Le temps est discrétisé comme dans le jeu de la vie. À chaque génération, une cellule peut passer de saine (susceptible) à malade (infected) si elle est en contact d’une personne malade avec un taux de transmission p €[0,1], si elle est en contact avec plus d’une personne ce taux augmente, on a p’ > p 
Une personne saine peut, en un nombre de générations à définir, décéder (deceased) ou guérir (recovered). Après un certain nombre de générations N, la vaccination peut apparaître, (N=0 si le vaccin est préalable à l'épidémie) et chaque case saine (susceptible) peut devenir vaccinée avec un taux de vaccination à définir. 
Le jeu s’arrête quand I = 0 😃 ou S = 0 ☠️
Dans un premier temps,nous utilisons une première modélisation simple,qui ne prend pas en compte les mouvements des personnes dans la population.Après,nous avons pensé à développer plus notre projet en tenant compte des différents mouvements de la foule pendant la propagation de l'épidémie,ce qui est plus proche de la réalité,pour pouvoir enfin présenter des stratégies de confinement et déconfinement.

 ## Installation 

```bash
pip install -r requirements.txt
```

## Première modélisation : Sans prendre en compte le déplacement du peuple

### Description

Dans cette modélisation,on utilise un modèle un peu plus dévelopé que SIRVD pour modéliser la proapagation d'une épidémie ,puisque nous prenons compte aussi du niveaau de fragilité des personnes atteintes de la maladie,pour une population supposée invariable dans l'espace,c'est à dire dont nous négligeons les mouvements.

### Usage

Sur le fichier simulate.py,vous trouverez toutes les instructions d'exécution



## Deuxième modélisation : en prenant en compte le mouvement des personnes

### Description

Dans cette partie,nous avons choisi de développer plus la première modélisation et cette fois en tenant compte des déplacements des gens,ce qui est plus réaliste.Ceci nous permettera nous proposer des stratégies de confinement pour arrêter la propagation de l'épidémie le plus rapidement possible.Dans cette deuxième modélisation,nous ne prenons pas compte de la fragilité de quelques personnes.
De plus,nous avons créer une interface graphique pour permettre à l'utilisateur d'interagir avec la simulation,et de choisir quelques paramètres pour pouvoir faire la modélisation.

### Usage

le fichier "deplacement.py" contient toutes les fonctions nécessaires pour réaliser ce modèle,comme les fonctions initialisation et changement d'état,mais elles sont cette fois adaptées aux personnes en mouvement dans l'espace.Il permet donc d'exécuter l'intégralité du programme.



## lien git du projet de la première semaine

https://gitlab-ovh-04.cloud.centralesupelec.fr/sara.abkari/game_of_life_sosa/-/project_members


## Présentation Powerpoint

https://centralesupelec-my.sharepoint.com/:p:/r/personal/sara_abkari_student-cs_fr/_layouts/15/Doc.aspx?sourcedoc=%7BEA3918AB-ABD8-46A0-A895-1B8600ED6662%7D&file=Pr%C3%A9sentation.pptx&wdOrigin=OFFICECOM-WEB.MAIN.REC&ct=1637231056004&action=edit&mobileredirect=true&PreviousSessionID=70b8ec13-8aa3-45cc-a976-ab0a3efc3cbf&cid=c814639c-46e2-49a6-a6c6-0924dbdd64ec


## Bibliographie

https://en.m.wikipedia.org/wiki/Compartmental_models_in_epidemiology

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8436575/#:~:text=By%20using%20the%20model%20parameters%2C%20the%20SIRVD-DL%20model,the%20contents%20of%20each%20part%20in%20detail.%202.1

https://pythonguides.com/python-tkinter-animation/#:~:text=Python%20tkinter%20matplotlib%20animation%20Matplotlib%20is%20a%20Python,use%20freely.%20It%20is%20written%20in%20Python%20Language.


















 

 



