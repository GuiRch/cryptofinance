# Cryptofinance A5 ESILV

## Proof of Work

Dans cette partie nous simulons le fonctionnement de la preuve de travail.

### Fonctionnement

Le fonctionnement ici est assez simple. On fixe une *target* c'est à dire le nombre de zéros par lequel on souhaite que le résultat trouvé commence. Par exemple si la **target** est fixée à 3, un résultat attendu aura la forme `0x000af82bd4 ...`.

La fonction `countZero` permet de compter si le nombre de zero en début de string est bon.
La fonction `proofOfWork` simule la preuve de travail, et compte le nombre d'itérations nécéssaire pour valider la preuve de travail

### Résultat

On retrouve la distribution d'une loi exponentielle.

![POW](https://user-images.githubusercontent.com/62909821/151864524-6bac4758-cd47-4eff-90f7-f2fe117399b5.PNG)


## Attaque 1 + 2 

### Fonctionement

On défini la fonction de minage qui donne un résultat pondéré en fonction du hashrate

Puis la fonction `attack()` suit le scénario d'attaque défini

| w      | R      | H     | Pb    |
| :----: |:------:| :----:|:-----:|
| B      |   0    |  1    | p     |
| AAA    |   3    |  3    | q**3  |
| AAB    |   2    |  2    | pq**2 |
| ABA    |   2    |  2    | pq**2 |
| ABB    |   0    |  2    | p**2q |

Puis on simule en fonction de diférents hashrate le rendement de l'attaque sur 10 000 itérations.

### Résultats

On observe que pour un certain hashrate (41.5%) l'attaque 1 + 2 est plus rentable que le minage honnête.

![Attaque1+2](https://user-images.githubusercontent.com/62909821/151863990-4f75bdc5-d6af-486e-8242-607b83ead3ae.PNG)


## Minage égoïste

![selfishminning](https://user-images.githubusercontent.com/62909821/151870611-fdb23686-51d7-4028-9d2a-2c480f8f64fd.PNG)


## Jeu du minage / Minage optimal

### Fonctionnement 
 
A l'aide de la fonction récursive `E()`, on calcule l'espérance de gain maximale, en fonction de **q** la puissance de hashage de l'attaquant, **a** le nombre de blocks minés par l'attaquant, **h** le nombre de blocks minés par la blockchain officielle et **n** le nombre d'actions.

### Résultats

On remarque que pour q > 42 % de puissance de hashage relative, l'attaquant à intérêt à opter pour la méthode de minage non conventionnelle qui consiste à miner de son côté puis d'écraser la blockchain officielle quand c'est possible.

A vrai dire le seuile ou cette méthode devient rentable est atteint précisement pour q = sqrt(2) - 1.
