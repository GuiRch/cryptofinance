#%% 4. Simulation double dépense

from random import *

# z nombre de confirmation
# A seuil d'abandon
# k nombre de block pré-minés
# v montant de la double dépense
# h relative hash rate -> puissance de calcul de l'attaquant en pourcentage ex : 50% de la puissance de calcul

# Conditons d'arrêts:
    #Retard >= A
    #Retard = -1 && hauteur blockchain officielle >= z
    
# Revenu / nombre de pile ou face 

def minage(h):
    n = random()
    hashRate = h/100
    if (n < hashRate):
        return 1
    else:
        return 0

def simulationDoubleSpend(h,A,v,z):
    bchHonest = 0
    bchAttacker = 0
    attackerDelay = 0
    diffBlocks = 0

    confirmations = 0
    
    while (attackerDelay < A):
        if(minage(h) == 1):
            bchAttacker += 1
        else:
            bchHonest +=1
        confirmations += 1

        # attackerDelay = abs()

