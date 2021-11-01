# -*- coding: utf-8 -*-
import copy
def indiceMinimum(vec): 
    #To do: Trouve l’indice et la valeur minimum dans un vecteur
    new_list = copy.deepcopy(vec)
    while -1 in new_list:
        new_list.remove(-1)
    if new_list == list():
        minimum = -1
        indice = -1
    else:
        indice = min(new_list)
        minimum = vec.index(indice)

    return (minimum, indice)
    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    #To do: Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique
    #To do: utiliser la fonction indiceMinimum(vec)
    #1) extraire la ligne du neoud de la matrice
    
    #2) affecter -1 pour chauqe noeud des noeuds_vis de la ligne
    
    #3) Trouve l’indice et la valeur minimum de la ligne
    
    return ...


def noeudMinimalNonVisites(matrice,noeuds_vis):
    #To do: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    
    return ...

def noeudsVoisins(matrice, noeud):
    #To do: Cherche les nœuds voisins et leur poids par rapport à un nœud initial.
    
    return ...

def dijkstra(matrice, depart, arrive):
    #To do: Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée.
    
    return ...


if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 3
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        
