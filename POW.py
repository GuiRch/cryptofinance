#%% 1. proof of work

import hashlib
from random import *
import time
import matplotlib.pyplot as plt


# target = nombre de "0" au début du hash pour résoudre la preuve de travail
target = 3

# fonction étudiant le hash pour évaluer si le nombre de "0" au début du hash est celui requis
def countZero(string, target):
    for i in range(0,target):
        if(string[0:target] == "0"*target):
            return True
        else:
            return False

# fonction de simulation de minage, pour résoudre la preuve de travail
def proofOfWork(target):
    
    x = random()
    hexaHash = hashlib.sha256(str(x).encode()).hexdigest()
    count = 0
    
    while(countZero(hexaHash, target) == False):
        x = random()
        hexaHash = hashlib.sha256(str(x).encode()).hexdigest()
        count += 1
      
    return(count)
 
# Evaluation du temps nécessaire à la fonction pour résoudre la preuve de travail
tmps1=time.time()       
proofOfWork(target)
tmps2=time.time()
executionTime = tmps2-tmps1

print("Temps d'execution = " + str((tmps2 - tmps1)))

L = []
for n in range(0,100):
    tmps1=time.time()       
    count = proofOfWork(target)
    tmps2=time.time()
    executionTime = tmps2-tmps1
    
    L.append([count, executionTime])

print(L)

# -> trouver le nombre de 0 dans le début du hash pour lequel la machine met moins de 20 sec à trouver
# -> faire tourner pendant un certain temps 
# -> garder les temps et tracer la loi de pb 