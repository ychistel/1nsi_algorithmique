# Exercice 1 : recherche d'une occurence

def occurence(tableau, valeur):
    n = 0
    for v in tableau:
        if v == valeur:
            n = n + 1
    return n

if __name__ == '__main__':
    a = occurence([1,2,1,2,2,1,2,1,1,1,2],1)