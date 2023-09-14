Complexité d’un algorithme
==========================


Introduction
------------

Le calcul de la complexité d’un algorithme permet de mesurer sa performance. Dans une situation précise, pour un
contexte donné, la complexité permet d'affirmer l'efficacité d'un algorithme par rapport à un autre.

Il existe deux types de complexité :

-  la complexité qui calcule l’utilisation de la mémoire par un algorithme
-  la complexité qui calcule le temps d'exécution d'un algorithme

Pour évaluer la complexité d'un algorithme:

-  on vérifie si le temps d'exécution, donc le nombre d'instructions, varie en fonction de la taille des données à traiter;
-  on cherche à évaluer ce temps dans le pire des cas, même s'il ne se produit pas systématiquement;
-  on exprime le temps d'exécution en fonction de la taille des données :math:`n`.

Les différentes complexités
---------------------------

.. rubric:: Complexité constante :math:`O(1)`

Les instructions élémentaires comme l'affectation d'une valeur à une variable, les calculs arithmétiques ou logiques, les comparaisons entre 2 valeurs ont un coût constant.

On considère que toutes ces opérations élémentaires ont un coût de 1 « unité » de temps. On note :math:`O(1)` la complexité d'une opération élémentaire.

.. admonition:: Exemple

   Soit l'instruction python : 
   
   >>> a = a + 1

   Cette instruction contient 1 addition et 1 affectation qui sont 2 opérations élémentaires à temps constant. Au final cette instruction Python a un coût de 2 unités de temps. Comme le temps est constant, sa complexité est :math:`O(1)`.

.. rubric:: Complexité linéaire :math:`O(n)`

Lorsque le temps d'exécution d'un algorithme dépend de la taille des données à traiter, il faut évaluer l'évolution de ce temps d'exécution par rapport à la taille des données.

Si ce temps d'exécution est **proportionnel** à la taille des données, on dit que la complexité de l'algorithme est linéaire. Par exemple, en doublant le nombre de données, on double le temps d'exécution.

.. admonition:: Exemple
   
   On recherche une valeur dans une liste non triée. On propose l'algorithme de recherche suivant:

   .. code:: python

      def recherche(tableau,valeur):
          for element in tableau:
              if element == valeur:
                  return True
          return False

   #. L'algorithme de recherche s'arête dès que la valeur est trouvée. Le temps d'exécution n'est pas constant. 
   #. Si la valeur cherchée ne figure pas dans le tableau, le tableau est parcouru entièrement puis la fonction renvoie ``False``. C'est la situation dite dans le "pire des cas".
   #. Dans le "pire des cas", si le nombre de valeurs du tableau est doublé, le temps d'exécution est doublé! On a un algorithme de complexité linéaire :math:`O(n)`.

.. rubric:: Complexité quadratique :math:`O(n^2)`

Les temps d'exécution d'unalgorithme qui dépend de la taille :math:`n` des données traitées n'est pas systématiquement linéaire. Pour certains algorithmes, lorsque la taille des données est multipliée par une constante :math:`k`, alors le temps d'exécution est multiplié par :math:`k^2`. 

On dit que la complexité de l'algorithme est quadratique qui se note :math:`O(n^2)`.

.. admonition:: Exemple

   On mesure les temps d'exécution d'un algorithme:

   -  Le temps d'exécution d'un algorithme est :math:`0,01` seconde pour traiter un tableau de 5000 nombres.
   -  Le temps d'exécution du même algorithme passe à :math:`0,04` seconde pour traiter un tableau de 10000 nombres.
   -  Le temps passe à :math:`0.16` seconde pour traiter 20 000 nombres.

   On observe que le temps est multiplé par 4 à chaque fois que le nombre de valeurs est multiplié par 2. L'algorithme a une complexité quadratique :math:`O(n^2)`.

Comparaison des complexités
---------------------------
Pour comparer l'efficacité d'un algorithme par rapport à un autre algorithme, on compare leurs complexité.

Il existe différentes complexités:

-  la complexité **constante** dont le temps d'exécution est constant quel que soit la taille des données. On la note :math:`O(1)`;
-  la complexité **linéaire** dont le temps dexécution est proportionnel à la taille des données. On la note :math:`O(n)`;
-  la complexité **quadratique** dont le temps d'exécution augmente proportionnellement au carré de la taille :math:`n` des données. On la note :math:`O(n^{2})`.

Ces différentes complexités traduisent l'efficacité de l'algorithme.

Un algorithme de complexité **constante** est plus efficace qu'un algorithme de complexité **linéaire**, lui-même plus efficace qu'un algorithme de complexité **quadratique**.
