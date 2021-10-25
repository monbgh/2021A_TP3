# -*- coding: utf-8 -*-
# Nom_du_fichier: Carte.py
# Creer le      : 2 Octobre 2021
# Creer par     : Saad Belgana
# Version num   : 1
# Modifier le   : 2 Octobre 2021

import math

def estVoisin(sommet1, sommet2):
    return sommet1['x'] - sommet2['x'] == 0 and abs(sommet1['y'] - sommet2['y']) == 1 or \
            abs(sommet1['x'] - sommet2['x']) == 1 and sommet1['y'] - sommet2['y'] == 0 or \
            abs(sommet1['x'] - sommet2['x']) == 1 and abs(sommet1['y'] - sommet2['y']) == 1;

def distanceEuclidienne(sommet1, sommet2):
    return math.sqrt((sommet1['x'] - sommet2['x']) **2 +  (sommet1['y'] - sommet2['y'])**2);

def distance3D(sommet1, sommet2):
    return math.sqrt(distanceEuclidienne(sommet1, sommet2) **2 +  (sommet1['altitude'] - sommet2['altitude'])**2);

def matriceAdjacence(sommets):   
    taille_graphe = len(sommets['no'])
    matrice = [[-1 for i in range(taille_graphe)] for i in range(taille_graphe)]
    
    for  i in range(taille_graphe):
        sommet1 = {key:value[i] for key, value in sommets.items()}
        for  j in range(taille_graphe):
            sommet2 = {key:value[j] for key, value in sommets.items()}
            if (estVoisin(sommet1, sommet2)):
                distance = distance3D(sommet1, sommet2)
                matrice[sommet1['no']][sommet2['no']] = distance
                matrice[sommet2['no']][sommet1['no']] = distance
                
    return matrice

def carteEnSommets(carte_topo):
    k = 0;
    sommets = {'no':[], 'x': [], 'y': [], 'altitude': []}
    for i in range(len(carte_topo)):
        for j in range(len(carte_topo[0])):
            sommets['no'].append(k)
            sommets['x'].append(j)
            sommets['y'].append(i)
            sommets['altitude'].append(carte_topo[i][j])
            k += 1
            
    return sommets


if __name__ == '__main__':
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 2, 'x': 1, 'y': 1, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet3 = {'no': 3, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet3)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet4 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance euclidienne entre les deux sommets est: {:.2f}"
    dist_eu = distanceEuclidienne(sommet1, sommet4)
    print(txt.format(dist_eu))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet4 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance 3D entre les deux sommets est: {:.2f}"
    dist_3D = distance3D(sommet1, sommet4)
    print(txt.format(dist_3D))
    
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
