def tri_selection(tableau):
    
    n = len(tableau)
    i = 0
    while i < n:
        j = i
        k = j
        
        while j < n:
            if tableau[j] < tableau[k]:
                k = j
            j = j + 1

        if i != k:
            tableau[i],tableau[k] = tableau[k],tableau[i]
            
        i = i + 1
    return tableau

def tri_insertion(tableau):
    
    n = len(tableau)
    i = 1
    
    while i < n:
        j = i - 1
        tampon = tableau[i]

        while j >= 0 and tableau[j] > tampon:
            tableau[j+1] = tableau[j]
            j = j - 1
        
        tableau[j+1] = tampon
        i = i + 1
    return tableau