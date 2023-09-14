Exercices de tris
=================

Exercice 1
----------

#. Écrire en Python la fonction ``tri_selection`` qui a pour paramètre un tableau et renvoie ce tableau trié en appliquant l'algorithme de tri par sélection.

   Tester votre fonction avec le tableau ``t = [7,24,2,13,6,17,1,14,23,11]``.

#. Écrire en Python la fonction ``tri_insertion`` qui a pour paramètre un tableau et renvoie ce tableau trié en appliquant l'algorithme de tri par insertion.

   Tester votre fonction avec le tableau ``t = [7,24,2,13,6,17,1,14,23,11]``.

Exercice 2
----------

Dans le problème du sac à dos, nous avons construit une liste d'objets, chaque objet étant un dictionnaire. On va trier cette liste en utilisant l'algorithme de tri par sélection et l'algorithme de tri par insertion.

On redonne les objets sous formes de dictionnaires et le tableau contenant ces objets.

.. code-block:: Python

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

#. On reprend le code Python du tri par sélection.

   a. Adapter ce code pour trier la liste d'objets selon leur masse.
   b. Adapter ce code pour trier la liste d'objets selon leur valeur.
   c. Adapter ce code pour trier la liste d'objet selon une clé de dictionnaire passée en argument de la fonction.

#. On reprend le code Python du tri par insertion.

   a. Adapter ce code pour trier la liste d'objets selon leur masse.
   b. Adapter ce code pour trier la liste d'objets selon leur valeur.
   c. Adapter ce code pour trier la liste d'objet selon une clé de dictionnaire passée en argument de la fonction.

Exercice 3
----------
La fonction Python ``type`` renvoie le type de la variable passée en argument de la fonction. Par exemple:

.. code-block:: Python

   a = 7
   b = "mot"
   c = {'cle':5}

   >>> type(a)
   int
   >>> type(b)
   str
   >>> type(c)
   dict

Écrire une fonction de tri capable de trier un tableau en s'adaptant aux valeurs qu'il contient.

