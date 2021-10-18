# -*- coding: utf-8 -*-

from Carte import carteEnSommets, matriceAdjacence

def lireCarte(nom_fichier):
    #To do: Lit le contenue du fichier à partir du nom de fichier reçu en paramètre
    
    return ...

def chargeMatriceDeCarte(nom_fichier):
    #To do: Retourne la matrice d’adjacence correspondant au fichier lut
    #1) lire la carte
    
    #2) transformer la carte lu en somet
    
    #3) determiner la matrice d’adjacence
    
    return ...


if __name__ == '__main__':
    nom_fichier = 'carte.txt'
    carte = lireCarte(nom_fichier)
    print("la carte lu est:")
    for ligne in carte:
        print("\t", ligne)
        
        nom_fichier = 'mini_carte.txt'
    carte = chargeMatriceDeCarte(nom_fichier)
    
    txt = "matrice d'adjacense de la carte lu est: \n\t"
    for i in carte:
        for j in i:
            txt += "{:.3f}\t".format(j)
        txt += "\n\t"
    print(txt)
    