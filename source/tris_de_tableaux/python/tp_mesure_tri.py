from random import randint
from time import time

def mesure_tri(fct,n):
    
    tps = 0.0
    
    # on effectue 100 mesures de temps d'exécution de la fonction
    for _ in range(50):
        # on crée un tableau de dimension n
        t = [randint(0,100000) for i in range(n)]
        expression = fct + "(t)"
        
        # relevé du temps initial
        t_0 = time()
        
        # on exécute la fonction de tri
        eval(expression)

        # relevé du temps final
        t_1 = time()
        
        # on ajoute le temps d'exécution de la fonction
        tps = tps + (t_1-t_0)
    
    # on renvoie le temps moyen d'exécution de la fonction
    return tps/50


# on importe les fonctions de tri à mesurer
from tris import tri_selection, tri_insertion

# on définit la taille du tableau
n = 1000
# on mesure les temps moyens d'exécution des tris
tps_selection = mesure_tri("tri_selection",n)
tps_insertion = mesure_tri("tri_insertion",n)
print(tps_insertion,tps_selection)