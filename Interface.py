# -*- coding: utf-8 -*-

import random

def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    
    return ...

def genereMatriceAleatoire(nb_noeuds):
    #To do: Génère une matrice d’adjacence de manière aléatoire
    
    return ...

def afficheChemin(predecesseurs, depart, arrive):
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
    
    return ...


if __name__ == '__main__':
    saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    afficheChemin(predecesseurs, depart, arrive)
