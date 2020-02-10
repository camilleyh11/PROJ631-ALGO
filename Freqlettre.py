class Freqlettre: #classe qui retourne la liste des tuples (freq, letre)


    def __init__(self, fichier): #constructeur
        self.fichier = fichier #fichier à ouvrir
        self.liste_lettre = [] #liste contenant les lettres du fichier
        self.liste_freq_et_lettre = self.parcours_fichier() #liste avec les tuples (freq,lettre)
        #self.code = code
        
        
    def frequence_fichier (self, lettre): #methode pour deter freq d'une lettre   
        fichier=open(self.fichier, "r") #ouvre le fichier et le stocke dans la var fichier
        compteur_frequence = 0 #initialisation du compteur
        for ligne in fichier: #parcours les lignes du fichier
            for i in ligne : #parcours les caractères de la ligne
                if i == lettre : #si la lettre considéré = la lettre parcouru
                    compteur_frequence = compteur_frequence + 1 #incrémentation du compteur
        return compteur_frequence #retourne la fréquence de la lettre
    
    
    def parcours_fichier (self):  #créer une liste de tuple triée (freq, lettre)
        fichier=open(self.fichier, "r") #ouvre le fichier et le stocke dans la var fichier
        liste=[] #initialisation d'une liste vide
        for i in fichier: #parcours les lignes du fichier
            for lettre in i : #parcours les caractères de la ligne
                if lettre not in self.liste_lettre : #si la lettre n'est pas ds la liste de lettre
                    self.liste_lettre.append(lettre) #on ajoute cette lettre ds la liste de lettre
                    frequence = self.frequence_fichier(lettre) #on stocke ds une nvlle var
                    #"frequence" la frequence de la lettre associé
                    liste.append((frequence,lettre)) #ajout du tuple (freq, lettre) dans liste
        #print("liste_freq_et_lettre = ",self.liste_freq_et_lettre)
        return self.ordre_caract(liste) #on appelle la méthode "ordre_caract" sur notre objet
            
    
    def ordre_caract (self,liste): #méthode pour trier la liste de tuple (freq, lettre)
        return sorted(liste) #retourne la liste trié à l'aide de la méthode "sorted"
    
    
    def creation_fichier(self): #methode pour créer un fichier texte avec les tuples (freq, lettre)
        self.fichier_freq_et_lettre = open(self.fichier + "_freq.txt", "w") #pr écrire ds le fichier
        self.fichier_freq_et_lettre.write(str(len(self.liste_freq_et_lettre))+"\n") #pr écrire le nbr total de lettre
        for (u,v) in self.liste_freq_et_lettre: #parcours les tuples
            self.fichier_freq_et_lettre.write(str(u) + " - "+ v +"\n") #pour écrire et que tout soit du mm type
        self.fichier_freq_et_lettre.close() #ferme le fichier une fois qu'on a tout écrit dedans
            
    def creation_dico(self, arbre): #création d'un dictionnaire avec les lettres et leurs codes associés
        dico={} #clé = lettre et valeur = code
        for i in self.liste_lettre: #parcours les lettres
            dico[i]=arbre.codage(i) #on met en valeur de la lettre le code associé
        return dico 
    
    def codage_fichier(self, arbre): #permet de coder le texte grace au dictionnaire (avec les 0 et les 1)
        dictionnaire = self.creation_dico(arbre) #on crée notre dictionnaire
        fichier=open(self.fichier, "r") #on ouvre le fichier
        code = "" #on veut écrire le code en str pcq le dictionnaire renvoit une chaine de caract
        for ligne in fichier: #parcours les lignes du fichier
            for i in ligne : #parcours les caractères de la ligne
                code = code + dictionnaire.get(i) #ajoute la valeur associé à la clé (le code à la lettre)
        #self.code=code
        return code
    
    def regroupement(self, arbre): #retourne une liste d'octet
        code = self.codage_fichier(arbre) #on stocke ds code le texte codé
        self.taux_comp(self.fichier,code) #on calcul le taux de compression
        huit = ""
        liste=[]
        for i in code: #on parcours les caractères du code (les 0 et les 1)
            if len(huit)<=8: #si la longueur <=8
                huit=huit+i #alors on ajoute le caractère (0 ou 1) dans la var "huit"
            if len(huit)==8: #si la longueur = 8
                liste.append(huit) #on ajoute l'octet à la liste
                huit="" #on réinitialise la variable à 0 pour recommencer
        while (len(huit)!=0) and (len(huit)!=8): #qd on arrive au dernier elem est que sa longueur !=8
            huit = huit+"0" #on ajoute des 0 à la fin pour que ca fasse un octet
        liste.append(huit) #on ajoute ce dernier octet à la liste
        return liste
            
    def chaine_devient_octet(self, arbre): #convertir nos octets en "caract spéciaux"
        liste = self.regroupement(arbre) #stocke ds liste les octets
        nombre = 0
        compteur = 1
        liste_octet=[]
        for elem in liste: #parcours les octets de la liste
            #print("elem=",elem)
            for chiffre in elem: #parcours chaque chiffre de l'octet
                nombre = nombre+int(chiffre)*2**(len(elem)-compteur) #converti bin -> dec
                compteur = compteur + 1
            compteur = 1 #on l'initialise à 1 une fois l'octet converti en décimal
            octet = (nombre).to_bytes(1, byteorder='big') #converti l'enter en "caract speciaux"
            liste_octet.append(octet) #on ajoute cet elem dans la liste
            #print(octet)
            nombre=0 #on le remet à 0 pour recommencer
        return liste_octet 
    
    def ecrire_octet(self, arbre): 
        fichier=open(self.fichier+"_comp.bin", "wb") #pr ecrire ds le fichier (binaire) les "caract speciaux"
        liste_octet=self.chaine_devient_octet(arbre) #recupere la liste d'octet (caract speciaux)
        for elem in liste_octet: #parcours les "caract speciaux"
            fichier.write(elem) #les ecrits dans le nouveau fichier
        fichier.close()
            
        
    def taux_comp(self,texte_original,code):
        fichier_original=open(texte_original, "r") #ouvre le fichier
        taille_original=0
        for ligne in fichier_original:  #parcours les lignes du fichier
            for lettre in ligne: #parcours les lettres du fichier
                taille_original=taille_original+1 #incrémente à chaque caractère parcouru
        fichier_original.close()
        
        print("Taux de compression : ", (1-(len(code)/(8*taille_original)))*100) #formule
        
        

        
        
        
        
        
        
        
        
                