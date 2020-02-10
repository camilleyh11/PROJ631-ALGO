from Freqlettre import Freqlettre #importation des classes permettant de recup le tuple freq lettre 
from Arbre import Arbre           #et pour construire l'arbre

class Main: #classe ou o fait les test
    
    a = Freqlettre('extraitalice.txt') #on crée un objet Freqlettre
    print(a.liste_freq_et_lettre) #on affiche la liste de tuple
    b= a.creation_fichier() #on crée le fichier avec les tuples
    arbre=Arbre('',a.liste_freq_et_lettre) #création d'un arbre
    liste=arbre.tant_que() #on applique la methode tant_que a notre objet arbre pour parcourir ttes les feuilles, enlever
                       #les 2 premiers elem et construire l'arbre
    liste[0].affiche_arbre() #affichage du dernier arbre restant dans la liste
    a.ecrire_octet(liste[0]) #crée le fichier avec les caractères spéciaux
    
    
    