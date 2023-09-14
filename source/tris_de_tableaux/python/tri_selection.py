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


t = [7,24,2,13,6,17,1,14,23,11]
tri_selection(t)
print(t)