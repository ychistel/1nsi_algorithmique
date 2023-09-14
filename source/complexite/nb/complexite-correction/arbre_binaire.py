class Noeud:
    
    def __init__(self, valeur, gauche=None, droit=None):
        # instancie, crée un objet Noeud avec ces trois attributs
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def __str__(self):
        # crée une chaine de caratères pour afficher un objet Noeud avec la commande print
        if self.valeur is None:
            return ""
        else:
            return "Noeud("+str(self.valeur) + ","+ str(self.gauche) +","+ str(self.droit)+")"
    
class Arbre:
    
    def __init__(self,racine=None):
        # instancie, crée un objet Arbre avec un seul attribut dont la valeur est un objet Noeud.
        if isinstance(racine,Noeud):
            self.racine = racine
        else:
            self.racine = Noeud(racine)
        
    def __str__(