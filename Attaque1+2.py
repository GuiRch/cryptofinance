#%% 2. Attaque 1+2
from random import *

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
for n in range(0,1000):
    L.append(benefit(hashrate))

deno = 0
num = 0
for elem in L:
    num += elem[0]
    deno += elem[1]
    
rendement = num/deno
print(rendement)