# -*- coding: utf-8 -*-

import math

def estVoisin(sommet1, sommet2):
    #To do: Valide que deux sommets sont voisins d’après leur emplacement en x et y sur la carte topographique
    if (sommet2['x'] - sommet1['x']) == 0 and (sommet2['y'] - sommet1['y']) == 1 or \
            (sommet2['x'] - sommet1['x']) == 1 and (sommet2['y'] - sommet1['y']) == 0 or\
            (sommet2['x'] - sommet1['x']) == 1 and (sommet2['y'] - sommet1['y']) == 1:
        return True
    else:
        return False

def distanceEuclidienne(sommet1, sommet2):
    #To do: Calcule la distance euclidienne entre deux sommets
    
    return (math.sqrt(((sommet1['x']-sommet2['x'])**2)+(sommet1['y']-sommet2['y'])**2))

def distance3D(sommet1, sommet2):
    #To do: Calcule la distance 3D entre deux sommets
    #To do: utiliser la fonction distanceEuclidienne(sommet1, sommet2)
    
    return (math.sqrt(((distanceEuclidienne(sommet1, sommet2))**2)+((sommet2['altitude']-sommet1['altitude'])**2)))

def matriceAdjacence(sommets): 
    #To do: Retourne la matrice d’adjacence à partir d’un tableau de sommets
    #To do: utiliser les fonctions:
    #To do: estVoisin(sommet1, sommet2) et distance3D(sommet1, sommet2)
    
    #1) determiner le nombre de sommet de sommets
    
    #2) creer une liste de liste de -1 de nombre de sommet
    
    #3) determiner la matrice d'adjacence des sommets
    
    return ...
              

def carteEnSommets(carte_topo):
    #To do: Converti les altitudes de la carte en tableau de sommets
    
    return ...


if __name__ == '__main__':
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 2, 'x': 1, 'y': 1, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 3, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance euclidienne entre les deux sommets est: {:.2f}"
    print(txt.format(distanceEuclidienne(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance 3D entre les deux sommets est: {:.2f}"
    print(txt.format(distance3D(sommet1, sommet2)))
    
    carte_topo = [[12, 13], [23, 21]]
    sommets = carteEnSommets(carte_topo)
    print("Le disctionnaire des sommets est: \n\t",sommets)
    
    matrice_ad= matriceAdjacence(sommets)
    txt = "la matrice d'adjacense est: \n\t"
    for i in matrice_ad:
        for j in i:
            txt += "{:.3f}\t".format(j)
        txt += "\n\t"
    print(txt)
