#%% 2. Attaque 1+2
from random import *
import matplotlib.pyplot as plt
import numpy as np


def minage(h):
    n = random()
    hashRate = h/100
    if (n < hashRate):
        return 1
    else:
        return 0
    
def selfishMining(h):
    if(minage(h) == 1):
        return("win")
    else:
        return("lose")
    
def attack(hashrate): # execute the scenario of the attack
    Results = []
    test = selfishMining(hashrate)
    if test == "lose":
        Results.append("B")
        return Results
    else:
        Results.append("A")
        test = selfishMining(hashrate)
        for i in range(0, 2):
            if(test == "win"):
                Results.append("A")
            else:
                Results.append("B")
        return (Results)
    

# rendement R1 + ... + Rn / H1 + ... + Hn    
def benefit(hashrate): # Count what does the attack give to the attacker
    A = attack(hashrate)
    if A == ['A', 'A', 'A']:
        return ([3,3])
    if A == ['A', 'B', 'A']:
        return ([2,2])
    if A == ['A', 'A', 'B']:
        return ([2,2])
    if A == ['A', 'B', 'B']:
        return ([0,2])
    if A == ['B']:
        return ([0,1])

L = []
hashrate = 50
for n in range(0,10000):
    L.append(benefit(hashrate))

deno = 0
num = 0
for elem in L:
    num += elem[0]
    deno += elem[1]
    
rendement = num/deno
print(rendement)


def simulation():
    results = []
    L=[]
    for hashrate in range(1,50):
        for n in range(0,10000):
            L.append(benefit(hashrate))
        deno = 0
        num = 0
        for elem in L:
            num += elem[0]
            deno += elem[1]
            
        rendement = num/deno
        #print(rendement)
        results.append(rendement)
    return results

# faire un graph avec diférent hashrate

rendements = simulation()
abs = np.arange(1,50,1)

plt.plot(abs, rendements, label = "attacker ") #creation du plot
plt.plot(abs, abs, label="honest mining")
plt.xlabel('puissance de hashage')
plt.ylabel('rendement')
plt.show()


#%% Test de le fonction random

def minage(h):
    n = random()
    hashRate = h/100
    if (n < hashRate):
        return 1
    else:
        return 0
A = 0
B = 0
for i in range(0,10000):
    rnd = minage(50)
    if rnd == 0:
        A += 1
    else:
        B+=1
    
print(A)
print(B)

#La fonction random semble bien aléatoire