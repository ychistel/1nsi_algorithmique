.. TNSI

Algorithmes de tri
==================

Tri par sélection
-----------------

L'algorithme de **tri par sélection** sépare le tableau en deux sous-tableaux.

-  Le premier sous tableau contient les valeurs déjà triées; il est vide au départ!
-  Le second sous tableau contient les valeurs non triées; c'est le tableau en entier au départ!

Toutes les valeurs de la partie non triée sont supérieures (ou égales) aux valeurs de la partie triée.

On cherche dans le sous-tableau non trié la plus petite valeur. Ensuite, on l'échange avec la première valeur du sous-tableau non trié. Après l'échange, le sous-tableau trié possède une valeur en plus et le sous-tableau non trié a une valeur en moins.

.. figure:: ../img/tri_selection.svg
   :align: center
   :width: 400

   Tri par sélection d'un tableau de nombres

Ainsi, par itération, le sous-tableau non trié diminue jusqu'à être vide et le tableau est entièrement trié.

.. warning::

   la difficulté de cet algorithme se situe dans la gestion des indices du tableau. On doit manipuler :

   -  l'indice de la première valeur de la partie non triée qui est incrémentée de 1 à chaque itération;
   -  l'indice de la valeur minimale de la partie non triée, qui permet l'échange avec la première valeur de la partie
      non triée.
   
.. rubric:: Algorithme du tri par sélection

On donne ci-dessous en pseudo code l'algorithme de tri par sélection:

.. code-block:: text

   n = len(tableau)     # n - 1 est l'indice du dernier élément du tableau
   i = 0                # indice des éléments du tableau à parcourir; i prend les valeurs de 0 à n - 1
   tant que i < n:
      j = i             # j est l'indice des éléments du sous-tableau non encore trié à parcourir
      k = i             # k est l'indice du plus petit élément du sous-tableau non trié
      
      # on cherche dans le sous-tableau non trié, la valeur minimale soit entre entre les indices i et n-1
      tant que j < n:
         si tableau[j] < tableau[k]:
            k = j
         j = j + 1

      # après avoir trouvé l'indice du plus petit élement du sous-tableau non trié, on échange, si elles sont 
      # différentes, la valeur minimale et la première valeur d'indice i du sous-tableau non trié
      si k != i
         on échange les valeurs d'indice i et k

      # on passe à la valeur suivante ce qui agrandit le sous-tableau trié et réduit le sous-tableau non trié.
      i = i + 1

.. .. rubric:: En python

.. Voici une version de cet algorithme écrit en Python:

.. .. literalinclude:: ../python/tri_selection.py
..    :lines: 1-25
..    :linenos:
..    :language: python

.. .. code-block:: python

..    >>> t = [7,24,2,13,6,17,1,14,23,11]
..    >>> tri_selection(t)
..    >>> print(t)

..    [1, 2, 6, 7, 11, 13, 14, 17, 23, 24]


Tri par insertion
-----------------

L'algorithme de **tri par insertion** sépare le tableau en deux sous tableaux.

-  Le premier sous-tableau contient les valeurs déjà triées; il contient la première valeur du tableau au début!
-  Le second sous-tableau contient les valeurs non triées; c'est le tableau sans son premier élément au début!

La première valeur du sous-tableau non trié est mémorisée dans une variable tampon. Toutes les valeurs du sous-tableau
trié supérieures à la variable tampon sont décalées de 1 rang vers la droite dans le tableau. Après décalage de ces
valeurs, on insère la valeur mémorisé dans la variable tampon.

.. figure:: ../img/tri_insertion.svg
   :align: center
   :width: 400
   
.. rubric:: Algorithme du tri par insertion

.. code-block:: text

   n = len(tableau)        # le dernier élément a pour indice n - 1
   i = 1                   # indice de la valeur à insérer et mémorisée dans la variable tampon
   
   tant que i < n:
      j = i - 1
      tampon = tableau[i]  # la variable tampon prend la valeur du tableau à insérer dans le sous tableau trié

      # on décale toutes les valeurs du tableau supérieures à la variable tampon
      tant que j >= 0 et tableau[j] > tampon :
         tableau[j + 1] = tableau[j]   # on décale à droite la valeur du tableau
         j = j - 1                     # on passe à l'élément plus à gauche

      # on insère la variable tampon dans le sous tableau trié en bonne place
      tableau[j + 1] = tampon    # j + 1 car pour sortir de la boucle on a décalé une fois de trop à gauche !

      # on passe à la valeur suivante dans le sous-tableau non trié
      i = i + 1

.. .. rubric:: Code en Python

.. .. literalinclude:: ../python/tri_insertion.py
..    :lines: 1-21
..    :linenos:
..    :language: python
   
.. .. code:: python

..    >>> t = [7,24,2,13,6,17,1,14,23,11]
..    >>> tri_insertion(t)
..    >>> print(t)

..    [1, 2, 6, 7, 11, 13, 14, 17, 23, 24]
   

Complexité des tris
-------------------

Les tris par selection et par insertion ont la même complexité. On peut la mesurer en comptant le nombre de comparaisons
effectuées à chaque itération des boucles ``while``. Pour les deux algorithmes, on a 2 boucles imbriquées.

Pour un tableau de dimension :math:`n`:

-  La première boucle ``while`` effectue :math:`n` fois la seconde boucle ``while``;
-  La seconde boucle ``while`` réalise :math:`n` comparaisons, puis :math:`n-1` comparaisons, puis :math:`n-2`
   comparaisons, etc.

Finalement l'algorithme effectue :math:`n+(n-1)+...+3+2+1 = \dfrac{n(n+1)}{2}` comparaisons. 

Ce nombre de comparaisons a pour ordre de grandeur :math:`n^{2}`.

On en déduit que le nombre de comparaisons dépend de la dimension :math:`n` du tableau. On dit que la complexité de ces
tris est **quadratique** et se note :math:`O(n^{2})`.
