#%% 2. Attaque 1+2
from random import *
import matplotlib.pyplot as plt
import numpy as np


def selfishMining(proba):
    Block=np.random.choice(('A','B'),p=[proba/100,1-proba/100])
    return Block
    

def attack(proba):
    Tentative1 =  selfishMining(proba) 
    if(Tentative1 =='A'):
        Tentative2=selfishMining(proba)
        Tentative3=selfishMining(proba)
        #AAX
        if(Tentative2 =='A'):
            #AAA
            if(Tentative3 =='A'):
                return ['A', 'A', 'A']
            #AAB
            else:
                P=(1-proba)*proba**2
                return ['A', 'A', 'B']
        #ABX
        else:
            #ABA
            if(Tentative3 =='A'):
                return ['A', 'B', 'A']
            #ABB
            else:
                return ['A', 'B', 'B']
        #BXX
    else:
        return ['B']
    

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
hashrate = 42
for n in range(0,100):
    L.append(benefit(hashrate))
    
print(L)
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
        #results.append([rendement,hashrate])
        results.append(rendement)
    return results


# faire un graph avec diférent hashrate

rendements = simulation()
print(rendements)
abs = np.arange(0.01,0.50,0.01)

plt.plot(abs, rendements) #creation du plot
#plt.plot(abs, abs, label="honest mining")
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
