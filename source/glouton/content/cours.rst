Algorithme glouton
==================

Certains problèmes ont plusieurs solutions, voire un très grand nombre de solutions. Parmi toutes ces solutions, il en existe qui sont plus optimales selon les contraintes imposées. La recherche de toutes les solutions peut être extrêmement gourmand en ressources et en temps d'exécution. Une stratégie dite **glouton**, permet d'optimiser le temps de recherche en proposant une solution qui sera optimale dans certains cas et non optimale dans d'autres. Le problème du **rendu de monnaie** en est un bon exemple.

Problème du rendu de monnaie
-----------------------------

Le système monétaire européen basé sur l’euro utilise des pièces de 1 et 2 euros et des billets de 5, 10, 20, 50, 100 et 200 euros. Il est possible avec ce système monétaire de réaliser toutes les sommes entières en supposant qu’on ait suffisamment de pièces et de billets.

L'algorithme glouton se présente ainsi:

-  On prend la plus grande unité, inférieure à la somme à rendre, et on la retire de la somme à rendre.
-  On recommence avec la même unité si possible, sinon on prend une unité inférieure.
-  On arête lorsque la somme à rendre est nulle.

.. admonition:: Exemple

   Pour rendre 9 euros à une personne, il existe plusieurs solutions. Parmi ces solutions, il y en a une qui utilise moins de pièces et de billets que les autres.

   #. On peut rendre 9 euros avec 9 pièces de 1 euro ou avec 1 billet de 5 euros et 4 pièces de 1 euros.
   #. Il existe une combinaison qui utilise seulement 1 billet et 2 pièces. Cette solution est optimale.

   Une stratégie pour déterminer une solution consiste à soustraire à la somme à rendre les plus grosses valeurs de pièces ou de billets jusqu’à obtenir 0 euro. Cette stratégie est dite **gloutonne**.

   En l'appliquant à la somme à rendre de 9 euros :

   -  on enlève la valeur 5 (la plus grande possible) ; il reste à rendre 4 euros
   -  on enlève la valeur 2 ; il reste à rendre 2 euros
   -  on enlève la valeur 2 ; il reste 0 euro à rendre

   La combinaison est 1 billet et 2 pièces qui est la solution optimale.

Pour le problème précédent, l'algorithme glouton donnera toujours la solution optimale. Cela est dû au système monétaire européen. Si on change les valeurs des pièces et billets, la solution sera dans certains cas non optimale.

.. admonition:: Exemple

   Prenons comme système monétaire les valeurs 1, 3, 6, 12, 24 et 30.

   #. Comment rendre la somme de 27 euros de manière optimisée ?

      En appliquant l'agorithme glouton, on obtient :

      -  on enlève la plus grande valeur possible 24 ; il reste 3 unités à rendre
      -  on enlève la plus grande valeur possible 3 ; il reste 0 unité à rendre

      La solution optimale est 2 unités. L'algorithme glouton nous fournit cette solution optimale.

   #. Comment rendre la somme de 48 euros de manière optimisée ?

      En appliquant l'algorithme glouton, on obtient :

      -  on enlève la plus grande valeur possible 30 ; il reste 18 unités à rendre
      -  on enlève la plus grande valeur possible 12 ; il reste 6 unités à rendre
      -  on enlève la plus grande valeur possible 6 ; il reste 0 unité à rendre

      La solution donnée par l'algorithme glouton est 3 pièces (30, 12 et 6). Elle n'est pas optimale car on peut rendre la somme de 48 unités avec 2 pièces de 24 unités.


Programmation python
--------------------

Un algorithme glouton appliqué au problème du rendu de monnaie est en pseudo-code le suivant : 

.. code-block:: text

   système monétaire = [200, 100, 50, 20, 10, 5, 2, 1]
   nombre pièces = 0
   pour chaque pièce du système monétaire:
      tant que la somme à rendre > pièce:
         nombre pièces = nombre pièces + 1
         somme à rendre = somme à rendre - pièce

On peut en donner une version en langage Python:

.. literalinclude:: ../python/glouton_cours.python
   :lines: 1-10
   :lineos:
