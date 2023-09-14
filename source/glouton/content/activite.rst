Activité
========

Problème du rendu de monnaie
----------------------------

Le système monétaire européen basé sur l’euro utilise des pièces de 1 et 2 euros et des billets de 5, 10, 20, 50, 100 et 200 euros. Il est possible avec ce système monétaire de réaliser toutes les sommes entières en supposant qu’on ait suffisamment de pièces et de billets.

On appelle **unité** toute pièce ou billet en euro et on suppose que l'on en dispose en nombre illimité.

Le problème du "rendu de monnaie" consiste à réaliser une somme à rendre en utilisant le moins d'unités possible.

#. Quelle est la combinaison qui utilise le moins d'unités pour rendre la somme:

   a. de 9 unités ?
   b. de 43 unités ?

#. On donne un algorithme qui résout ce problème :

   .. code-block:: text
      
      nombre d'unités = 0
      Tant que la somme à rendre est supérieure à 0 unité:
         On enlève la plus grande unité possible à la somme à rendre
         le nombre d'unités augmente de 1
      on renvoie le nombre d'unités

   a. Appliquer cet algorithme pour rendre la somme de 43 unités. On écrira les différentes étapes et valeurs dans le tableau suivant en y ajoutant des colonnes si besoin.
   
      +---------------+----+----+---+
      |somme à rendre | 43 | 23 |   |
      +---------------+----+----+---+
      |unité enlevée  | 20 |    |   |
      +---------------+----+----+---+
      |nombre unités  |  1 |    |   |
      +---------------+----+----+---+
   
   b. Le nombre d'unités est-il conforme au résultat espéré ?

#. On remplace le système monétaire européen par un système où les unités monétaires ont pour valeurs 1, 3, 6, 12, 24 et 30.

   a. Comment rendre la somme de 27 unités en utilisant le moins d'unités possible ?
   b. En appliquant l'algorithme, le nombre d'unités obtenu est-il conforme au résultat précédent ?
   c. Comment rendre la somme de 48 unités en utilisant le moins d'unités possible ?
   d. En appliquant l'algorithme, le nombre d'unités obtenu est-il conforme au résultat précédent ?
