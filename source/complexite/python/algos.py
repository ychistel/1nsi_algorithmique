def algo_1(tableau):
    a = 0
    for i in range(len(tableau)):
        a = a + tableau[i]
    return a

def algo_2(tableau,valeur):
    a = 0
    for i in range(len(tableau)):
        if tableau[i] <= valeur:
            a = a + 1
    return a

def algo_3(tableau,valeur):
    i = 0
    a= 0
    while tableau[i] <= valeur:
        a = i
        i = i + 1
    return a

def algo_4(tableau):
    a = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            a = a + tableau[i][j]
    return a

if __name__ == '__main__':
    # Algorithme 1:
    a_1a = algo_1([7,3,8,4,9,5])
    print(a_1a)
    a_1b = algo_1([i**2 for i in range(100)])
    print(a_1b)

    # Algorithme 2:
    a_2a = algo_2([7,3,8,4,9,5],6)
    print(a_2a)
    a_2b = algo_2([i**2 for i in range(100)],1000)
    print(a_2b)

    # Algorithme 3
    a_3a = algo_3([7,3,8,4,9,5],6)
    print(a_3a)
    a_3b = algo_3([i**2 for i in range(100)],1000)
    print(a_3b)

    # Algorithme 4
    a_4a = algo_4([[7,3,8],[4,9,5],[1,2,6]])
    print(a_4a)
    a_4b = algo_4([ [i for i in range(j,j+10)] for j in range(10)])
    print(a_4b)