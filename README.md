# Cryptofinance A5 ESILV

## Proof of Work

Dans cette partie nous simulons le fonctionnement de la preuve de travail.

### Fonctionnement

Le fonctionnement ici est assez simple. On fixe une *target* c'est à dire le nombre de zéros par lequel on souhaite que le résultat trouvé commence. Par exemple si la *target* est fixée à 3, un résultat attendu aura la forme `0x000af82bd4 ...`.

La fonction `countZero` permet de compter si le nombre de zero en début de string est bon.
La fonction `proofOfWork` simule la preuve de travail, et compte le nombre d'itérations nécéssaire pour valider la preuve de travail

### Résultat

On retrouve la distribution d'une loi exponentielle

## Attaque 1 + 2 

### Fonctionement

On défini la fonction de minage qui donne un résultat pondéré en fonction du hashrate

Puis la fonction `attack()` suit le scénario d'attaque défini

| w      | R      | H     | Pb    |
| :----: |:------:| :----:|:-----:|
| B      |   0    |  1    | p     |
| AAA    |   3    |  3    | p**3  |
| AAB    |   2    |  2    | pq**2 |
| ABA    |   2    |  2    | pq**2 |
| ABB    |   0    |  2    | p**2q |


## Attaque à la double dépense

## Minage égoïste