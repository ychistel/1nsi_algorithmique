Le choixpeau magique
====================

À l'entrée à l'école de Poudlard, le Choixpeau magique répartit les élèves dans différentes maisons (Gryffondor, Serpentar, Serdaigle et Poufsouffle) en fonction de leur courage, leur loyauté , leur sagesse et leur malice.

Le Choixpeau magique dispose d'un fichier CSV dans lequel sont répertoirés les donnés d'un échatillon d'élèves.

Voici les 6 premières lignes de ce fichier.

.. table::
   :align: center
   :class: text-align-center

   ======== ======= ======= ======= ====== ==========
   Nom      Courage Loyauté Sagesse Malice Maison
   ======== ======= ======= ======= ====== ==========
   Adrian   9       4       7       10     Serpentar
   Andrew   9       3       4       7      Griffondor
   Angelina 10      6       5       9      Griffondor
   Anthony  2       8       8       3      Serdaigle
   Arthur   10      4       2       5      Griffondor
   ======== ======= ======= ======= ====== ==========

Et voici les élèves que le Choixpeau magique souhaite orienter:

.. table::
   :align: center
   :class: text-align-center

   ======== ======= ======= ======= ======
   Nom      Courage Loyauté Sagesse Malice
   ======== ======= ======= ======= ======
   Hermione 8       6       6       6
   Drago    6       6       5       8
   Cho      7       6       9       6
   Cédric   7       10      5       6
   ======== ======= ======= ======= ======

L'objectif de l'exercice est d'aider le Choixpeau magique à déterminer la maison des nouveaux élèves.

.. rubric:: Partie 1 : modéliser un élève
   :name: partie-1--modéliser-un-élève

On décide de modéliser chaque élève par un dictionnaire avec les données à disposition. Par exemple:

.. code:: python

   adrian = {"nom":"Adrian", "courage":9, "loyauté":4, "sagesse":7, "malice":10, "maison":"Serpentar"}
   hermione = {"nom":"Hermione", "courage":8, "loyauté":6, "sagesse":6, "malice":6}

#. Donner la modélisation de l'élève Anthony
#. On décide d'utiliser la distance de Manhattan pour calculer la distance entre 2 élèves, c'est à dire: 
   ``distance(élève1, élève2)=|c1-c2|+|l1-l2|+|s1-s2|+|m1-m2|``

   a. Avec cette formule, vérifier que la distance entre Hermione et Adrian est bien 8.
   b. Quelle est la distance entre Arthur et Drago?
   c. Écrire le code de la fonction ``distance`` qui prend deux élèves en paramètre et qui renvoie la distance entre ces deux élèves. Ne pas oublier de préciser la documentation et donner au moins un test.

.. rubric:: Partie 2 : charger les données en table
   :name: partie-2--charger-les-données-en-table

On donne le code incomplet d'une fonction qui permet de récupérer les données des élèves d'un fichier CSV pour les stocker dans une liste.

.. code:: python

   def charger_table(nom_fichier):
         """
         Permet de charger une liste d'élèves à partir d'un fichier CSV.
         Paramètre : le nom du fichier CSV
         Résultat: la liste des élèves.
         """
         table = []
         with open(nom_fichier, mode='r', encoding='utf-8', newline='') as f:
            data = csv.reader(f,delimiter=";")
            data.__next__() # pour passer l'entête du fichier
            for eleve in data:
               table.append({"nom": eleve[0],\
                              "courage": ...,\
                              "loyauté": ...,\ 
                              "sagesse": ...,\ 
                              "malice": ... ,\ 
                              "maison": ... })
            return table

#. Compléter le code de la fonction ``charger_table`` pour que la table contienne des dictionnaires associés à chaque élève.
#. Quels sont les types des valeurs des clefs ``courage``, ``loyauté``, ``sagesse`` et ``malice`` ? Compléter votre code Python pour que le type soit bien respecté dans la fonction.
#. La variable ``poudlard`` contient la table des élèves du fichier ``choipeauMagique.csv``. Quelle est l'instruction Python qui permet de créer cette variable. Quel est son type ?

.. rubric:: Partie 3 : trouver la maison majoritaire
   :name: partie-3--trouver-la-maison-majoritaire

On souhaite écrire le code d'une fonction qui prend en paramètre une liste d'élèves et qui renvoie la maison la plus représentée dans cette liste. Pour cela, on propose d'utiliser une fonction auxiliaire dant le code est le suivant:

.. code:: python

   def frequence_des_maisons()table:
         """
         Paramètre : liste d'élèves, chaque élève est modélisé par un dictionnaire
         Résultat : un dictionnaire dont les clefs sont les maisons et les valeurs le nombre de fois où cette maison apparait.
         """
         frequences = {}
         for eleve in table:
            maison = eleve["maison"]
            if maison in frequence.keys():
               frequences[maison] += 1
            else:
               frequences[maison] = 1
         return frequences

   assert frequence_des_maisons(poudlard) == {'Serpentar':12, 'Gryffondor': 17, 'Serdaigle': 11, 'Poufsouffle': 10}

#. Quelle est la signification du nombre 12 qui apparait dans l'instruction ``assert`` ?
#. Écrire le code de la fonction ``maison_majoritaire`` qui prend en paramètre une liste d'élèves et qui renvoie le nom de la maison la plus représentée. Ne pas oublier la documentation et au moins un test.

.. rubric:: Partie 4 : plus proches voisins
   :name: partie-4--plus-proches-voisins

#. On se propose d'écrire en langage naturel ou pseudo code l'algorithme des plus proches voisins pour associer une maison à un nouvel élève.
   Les données sont:

   -  table : une liste d'élèves déjà associés à une maison
   -  nouveau : un nouvel qui n'a pas encore de maison

   Résultat : les k plus proches voisins du nouveau

   a. Quelle est la valeur de k ?
   b. Écrire l'algorithme des k plus proches voisins à appliquer.

#. Écrire en Python cet algorithme.

.. rubric:: Partie 5 : attribuer une maison
   :name: partie-5--attribuer-une-maison

Le Choixpeau magique décide d'utiliser un algorithme de prédiction pour choisir la maison qui sera attribuée aux nouveaux élèves. Voici l'algorithme:

.. rubric:: Données
   :name: données

-  ``table`` est une liste d'élèves;
-  un nouvel élève qui n'a pas encore de maison.

.. rubric:: Résultat
   :name: résultat

-  la maison du nouvel élève

.. rubric:: Algorithme
   :name: algorithme

#. Trouver dans la table les k plus proches voisins du nouvel élève.
#. Parmi ces ``proches_voisins``, trouver la maison majoritaire.
#. Renvoyer la ``maison_majoritaire``.

Implémenter cet algorithme en Python.

.. rubric:: Conclusion
   :name: conclusion

Quelles maisons seront attribuées aux élèves donnés en début de problème par le Choixpeau magique?