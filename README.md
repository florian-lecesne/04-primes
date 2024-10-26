# Nombres premiers

Un [nombre premier](https://en.wikipedia.org/wiki/Prime_number) est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs. Ces deux diviseurs sont 1 et le nombre considéré. L'objectif est d'écrire du code qui permet de vérifier si un nombre est premier ou pas.

Le fichier ``primes.py`` contient :

- une fonction secondaire ``isprime()`` qui a pour but de vérifier si un entier est un nombre premier ou pas. 
  
  - elle prend en argument un nombre entier ``p`` ;
  - et retourne un booléen exprimant la vérité de « ``p`` est un nombre premier ». 
  
- la fonction principale ``main()`` qui fait quelques appels à la fonction secondaire permettant de vérifier son bon fonctionnement .

## To do

1️⃣ Ecrire le code de la fonction secondaire.

2️⃣ Ecrire quelques appels à la fonction secondaire dans ``main()``.

3️⃣ Exécuter le programme depuis le terminal

    $ python primes.py

4️⃣ Une fois le code fonctionnel, le soumettre aux tests unitaires. Le grade obtenu est le pourcentage de tests réussis. 

    $ pytest .python

Si le grade n'est pas satisfaisant, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le grade est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/python/chapters/16-style.html). Scorer cette qualité

    $ pylint *.py

Si le score n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages

6️⃣ Lorsque le grade et le score ``pylint`` sont satisfaisants, pusher le travail pour évaluation

    $ git pull
    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.
