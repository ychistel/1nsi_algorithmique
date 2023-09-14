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

t = [7,24,2,13,6,17,1,14,23,11]
tri_insertion(t)
print(t)