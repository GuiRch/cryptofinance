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

# cas a > h
# E(a,h,n,q,c) = max(h+1-c+E())
# cas a = h
# E()
# cas a < h

def Max(a,b):
    if a > b:
        return a
    else:
        return b
    
def esperance(a,h,n,q,c):
    if a > h:
        return (a-(a-h)*c)
    else:
        return 0

def E(a,h,n,q,c):
    if a > h:
        return Max(h+1-c+esperance(a-h-1, 0, n, q, c), 
                   q*esperance(a+1,h, n-1, q, c)+(1-q)*(esperance(a, h+1, n-1, q, c)-c))
    if a == (h+1):
        return Max(h+1-c, q*esperance(a+1,h, n-1, q, c)+(1-q)*(esperance(a, h+1, n-1, q, c)-c))
    if a <= h:
        return Max(0, q*esperance(a+1,h, n-1, q, c)+(1-q)*(esperance(a, h+1, n-1, q, c)-c))

# On cherche q min tel que E(0,0,n,q,q) > 0
print(E(0,0,3,0.41,0.41))