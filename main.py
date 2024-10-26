###  main.py
"""
Exercice portant sur le calcul de nombres premiers, leur affichage, et les docstrings.
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne la valeur booléenne de l'affirmation " 'p' est un nombre premier ".
    
    Args:
        p: entier positif >= 2

    Returns:
        True: p est un nombre premier
        False: p n'est pas un nombre premier 
    """

    if p <=1:
        return False
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Affiche une liste de nombres premiers jusqu'à 100.
    
    Appels:
        isprime(n): détermine si oui ou non 'n' est un nombre premier.

        print(n): effectue l'affichae au terminal de 'n'.
        
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
