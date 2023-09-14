def tri_selection(tableau,cle):
    i = 0
    n = len(tableau)
       
    # on parcourt le tableau, l'indice i prend les valeurs de 0 à n-1
    while i < n:
        # on initialise les indices à la valeur de l'indice i (début du sous tableau non trié)
        j = i
        indice_valeur_minimale = j
        
        # on parcourt le sous tableau non trié à partir de l'indice i
        while j < n:
               
            # on cherche l'indice de la plus petite valeur du sous tableau non trié
            if tableau[j][cle] < tableau[indice_valeur_minimale][cle]:
                indice_valeur_minimale = j
            j = j + 1
               
        # on échange la première valeur du sous tableau non trié avec la valeur minimale
        if i != indice_valeur_minimale:
            tableau[i],tableau[indice_valeur_minimale] = tableau[indice_valeur_minimale],tableau[i]
            
        # on passe à l'indice suivant dans le sous tableau non trié
        i = i + 1
    return tableau

def tri_insertion(tableau,cle):
    # indice de la valeur à insérer (la valeur d'indice 0 est déjà insérée)
    j = 1
    n = len(tableau)
    while j < n:
        i = j - 1
        
        # une variable tampon prend la valeur du tableau à insérer dans le sous tableau trié
        valeur_a_inserer = tableau[j]
        
        # on décale les valeurs du tableau supérieures à la variable tampon
        while i >= 0 and tableau[i][cle] > valeur_a_inserer[cle]:
            tableau[i+1] = tableau[i]
            i = i - 1
        
        # on insère la variable tampon dans le sous tableau trié en bonne place
        tableau[i+1] = valeur_a_inserer
        
        # on passe à la valeur suivante dans le sous tableau non trié
        j = j + 1
    return tableau

# on construit un dictionnaire pour chaque objet contenant son nom, sa valeur en pièces d'or et sa masse
# tous les objets sont réunis dans une même liste objets
cape = {"nom":'cape',"masse":2,"valeur":15}
horloge = {"nom":'horloge',"masse":4,"valeur":16}
miroir = {"nom":'miroir',"masse":4,"valeur":12}
baguette = {"nom":'baguette magique',"masse":1,"valeur":10}
antidote = {'nom':"antidote","masse":1,"valeur":8}
epee = {"nom":'épée',"masse":6,"valeur":10}
diademe = {"nom":"diadème","masse":4,"valeur":30}

# Tableau contenant les différents objets collectés par le héros
objets = [cape, horloge, miroir, baguette, antidote, epee, diademe]

tri_selection(objets,'valeur')
print(objets)

# Tableau contenant les différents objets collectés par le héros
objets = [cape, horloge, miroir, baguette, antidote, epee, diademe]

tri_insertion(objets, 'masse')
print(objets)