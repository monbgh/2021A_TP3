# -*- coding: utf-8 -*-
# Nom_du_fichier: Algo.py
# Creer le      : 2 Octobre 2021
# Creer par     : Saad Belgana
# Version num   : 1
# Modifier le   : 2 Octobre 2021

def indiceMinimum(vec):    
    indice, minimum = 0, vec[0]
    for i, value in enumerate(vec):
        if(((minimum < 0) or (value < minimum)) and (value > 0)):
            indice, minimum = i, value
            
    return (indice, minimum)
    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    ligne_noeuds =  matrice[noeud].copy()
    for noeud in noeuds_vis:
        ligne_noeuds[noeud] = -1

    return indiceMinimum(ligne_noeuds)

def noeudMinimalNonVisites(matrice,noeuds_vis):
    poids_min, depart, arrive = -1, -1, -1
    for noeud in noeuds_vis:
        [arrive_cou, poids_cour] = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)      
        if (arrive_cou > 0) and ((poids_min > poids_cour) or (poids_min == -1)):
            poids_min, depart, arrive = poids_cour, noeud, arrive_cou
   
    return (depart, arrive)

def noeudsVoisins(matrice, noeud):
    ligne_noeuds = matrice[noeud].copy()
    voisin =list(zip(*[[i, noeud] for i, noeud in enumerate(ligne_noeuds) if (noeud > 0)]))    
    return (list(voisin[0]), list(voisin[1]))

def dijkstra(matrice, depart, arrive):
    n               = len(matrice[0])
    noeuds_vis      = [depart]
    dis_min         = [-1] * n
    predecesseur    = [-1] * n   
    dis_min[depart] = 0;
    noeud_cour      = depart;
    
    while ((len(noeuds_vis) <= n) and (noeud_cour != arrive)):
        [noeuds, poids] = noeudsVoisins(matrice, noeud_cour)
        for i, noeud in enumerate(noeuds):
            distance  = dis_min[noeud_cour] + poids[i]
            if(distance < dis_min[noeud] or dis_min[noeud] == -1):
                dis_min[noeud] = distance
        
        [noeud_prec, noeud_cour] = noeudMinimalNonVisites(matrice, noeuds_vis)
        noeuds_vis.append(noeud_cour)
        predecesseur[noeud_cour] = noeud_prec
        
    return (dis_min[arrive], predecesseur)


if __name__ == '__main__':


    vec     = [-1, 4, 6, -1, -1, 3, 5]
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], 
               [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud_1 = 1
    noeud_2 = 3
    noeuds_vis_1 = [1]
    noeuds_vis_2 = [1, 2, 3]
    noeuds_vis_3 = [0,2]
    depart  = 0
    arrive  = 3
        
    
    res_1 = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(res_1[1], res_1[0]))
    
    
    res_2 = noeudMinimalNonVisitesDeNoeud(matrice, noeud_1, noeuds_vis_1)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(res_2[1], res_2[0]))
    
    
    res_3 = noeudMinimalNonVisitesDeNoeud(matrice, noeud_1, noeuds_vis_2)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(res_3[1], res_3[0]))
       
    
    res_4 = noeudMinimalNonVisites(matrice, noeuds_vis_3)
    txt = "le neoud de depard est {} et le noeud d'arriver est {}"
    print(txt.format(res_4[0], res_4[1]))
      
    
    res_5 = noeudsVoisins(matrice, noeud_1)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(res_5[0], res_5[1], noeud_1))
       
    
    res_6 = noeudsVoisins(matrice, noeud_2)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(res_6[0], res_6[1], noeud_2))
    
    res_7 = dijkstra(matrice, depart, arrive)
    txt = ''.join(("la distance la plus cours entre un noeud de départ {}",
                   "et un noeud d’arrivée {} est {} avec les prédécesseurs {}"))
    print(txt.format(depart, arrive, res_7[0], res_7[1]))