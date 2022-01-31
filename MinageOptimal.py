#%% Jeux du minage

# pour q = 32.92% on peut trouver un n tel que E(a,h,n) > 0
# E [ R(x) - q H(x)] > 0 -> représente uniquement le rendement
# Cout réel trop difficile à calculer, mais toujours le même peut importe la strat
# On aura toujours le même coût
# On veut juste savoir si E [ R(x) - q H(x)] > 0 

# E(a,h,n,q,c)
#espérance du gain maximale du mineur au cours d'un cycle qui prend fin dès que n bloc ont été découverts
# a > h+1 -> écraser ou attendre
# a = h+1 -> écraser ou attendre
# a <= h -> 

# E(a,h,n,q,c) = { a-(a-h)*c si a>h
#                { 0         si a<=h

# E(0,0,3,q,q) = 0 ssi q<sqr(2)-1

import matplotlib.pyplot as plt
import numpy as np

def Max(a,b):
    if a > b:
        return a
    else:
        return b
    

def E(a,h,n,q,c):
    if n == 0 :
        if a>h:
            return a - (a-h) *c
        else:
            return 0
    else:

        if a > h:
            return max(h+1-c+E(a-h-1, 0, n, q, c), 
                    q*E(a+1,h, n-1, q, c)+(1-q)*(E(a, h+1, n-1, q, c)-c))
        if a == (h+1):
            return max(h+1-c, q*E(a+1,h, n-1, q, c)+(1-q)*(E(a, h+1, n-1, q, c)-c))
        if a <= h:
            return max(0, q*E(a+1,h, n-1, q, c)+(1-q)*(E(a, h+1, n-1, q, c)-c))

# On cherche q min tel que E(0,0,n,q,q) > 0

def courbes_simulation():
    abs = np.arange(0,0.6,0.1)
    esperances = []

    for q in range (0,6):
        esperances.append(E(0,0,3,q/10,q/10))
    
    plt.plot(abs, esperances) #creation du plot
    #plt.plot(abs, abs, label="honest mining")
    plt.xlabel('q')
    plt.ylabel('espérance de gain')
    plt.show()

courbes_simulation()


print("On remarque que la courbe croit après 0.4")

print("pour q = 0.42 : " + str(E(0,0,3,0.42,0.42)))

print("pour q = 0.41 : " + str(E(0,0,3,0.41,0.41)))

print ( "On a donc plus précisement E(0,0,n,q,q) > 0 pour q >= 0.42")