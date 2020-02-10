class Arbre: #classe pour construire l'arbre
    
    def __init__(self, lettre, liste_freq_et_lettre, freq=None, fils_g=None, fils_d=None): #constructeur
        self.lettre = lettre #lettre
        self.fils_g = fils_g #fils gauche
        self.fils_d = fils_d #fils droit
        self.liste = liste_freq_et_lettre #liste de tuple de la classe "Freqlettre"
        self.freq = freq #frequence
        self.liste_feuille=[] #liste contenant les arbres

    
    def feuille(self): #méthode pour créer les feuilles
        liste_feuille = [] #liste pour ajouter les feuilles
        for (freq,alpha) in self.liste: #parcours des freq et des lettres de la liste importé
            liste_feuille.append(Arbre(alpha,self.liste,freq=freq)) #on ajoute dans la liste "liste_feuille"
                                                                    #les tuples mais sous forme d'arbre
        self.liste_feuille = liste_feuille #on stocke ces feuilles dans la var du constructeur pour les
                                           #utiliser plustard
    
    def affiche_feuille(self): #méthode pour afficher les feuilles
        for i in self.liste_feuille : #on parcourt les éléments de la liste contenant les feuilles
            print(i.lettre," et ",i.freq) #affichage de la lettre et la freq correspondante
            
    def affiche_arbre(self): #méthode pour afficher l'arbre
        print('arbre :',self.lettre,' et ', self.freq) #affichage de la lettre et la freq correspondante
        if self.fils_g!=None and self.fils_d!=None: #si il y a un fils gauche et droit, on l'affiche
            print('fils gauche :', self.fils_g.lettre, self.fils_g.freq, ', fils droit :', self.fils_d.lettre, self.fils_d.freq)
        for enfant in [self.fils_g, self.fils_d]: #parcours les fils gauche et droit
            if enfant!=None: #si il y a un fils
                enfant.affiche_arbre() #on applique la méthode affiche_arbre au fils
            
    def constru_arbre(self): #méthode pour construire l'arbre
        somme_freq = self.liste_feuille[0].freq + self.liste_feuille[1].freq #somme des freq des 2 premiers elem
        self.liste.pop(1) #on enleve les 2 premiers elem de la liste des     #de la liste d'abre
        self.liste.pop(0) #tuples, remarque : d'abord le 2e puis le 1er car 0 et 0 c'est bizarre
        noeud = Arbre('', self.liste, somme_freq, self.liste_feuille[0], self.liste_feuille[1]) #creation nv noeud ak somme des freq
        self.liste.append((noeud.freq,noeud.lettre)) #ajout à la liste de tuple freq et lettre du nv noeud considere        
        self.liste=sorted(self.liste) #on trie la liste de tuple
        index = self.liste.index((noeud.freq,noeud.lettre)) #on recup la position du nv noeud dans la liste freq lettre 
        self.liste_feuille.pop(1) #on enleve les 2 premiers elem de la liste des feuilles
        self.liste_feuille.pop(0)
        self.liste_feuille[index:index]=[noeud] #on ajoute l'element noeud à sa place dans la liste d'arbre
        return self.liste_feuille #retourne la liste d'arbre
    
    def tant_que(self): #methode pour parcourir toute les feuilles
        self.feuille() #on construit les feuilles
        a=None #initialisation d'une variable pour y stocker l'arbre 
        while len(self.liste_feuille)>1: #tant qu'il ne reste pas qu'une seule "feuille" (la racine)
            a=self.constru_arbre() #on construit les arbres
        return a #retourne l'objet
    
    def codage(self, lettre, code=""): #méthode pour trouver le code correspondant à un caractère/lettre
        if self.lettre == lettre: #si la lettre de l'arbre est la même que celle qu'on cherche
            return code #alors on écrit son code
        else:
            if self.fils_g != None: #si il y a un fils gauche
                if self.fils_g.codage(lettre, code+"0") != None: #si la lettre est à gauche
                    return self.fils_g.codage(lettre, code+"0") #alors on met un 0
            if self.fils_d != None: #réciproque à droite
                if self.fils_d.codage(lettre, code+"1") != None:
                    return self.fils_d.codage(lettre, code+"1") 

            
