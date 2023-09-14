Activité sur la complexité
==========================

L'objectif est de compter le nombre d'instructions réalisées dans un script Python.

Algorithme 1
------------

.. literalinclude:: ../python/algos.py
   :lines: 1-5
   :linenos:
   
#. On réalise en console l'appel :

   >>> algo_1([7,3,8,4,9,5])

   -  Combien de fois l'instruction en ligne 4 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. On réalise un nouvel appel en console:

   >>> algo_1([i**2 for i in range(100)])

   -  Combien de fois l'instruction en ligne 4 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. De façon générale, quel lien existe-t-il entre le tableau et le nombre d'exécutions de l'instruction en ligne 4 ?

Algorithme 2
------------

.. literalinclude:: ../python/algos.py
   :lines: 7 - 12
   :linenos:
   
#. On réalise en console l'appel :

   >>> algo_2([7,3,8,4,9,5],6)

   -  Combien de fois l'instruction en ligne 4 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. On réalise un nouvel appel en console:

   >>> algo_2([i**2 for i in range(100)],1000)

   -  Combien de fois l'instruction en ligne 4 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. De façon générale, quel lien existe-t-il entre le tableau et le nombre d'exécutions de l'instruction en ligne 4 ?

Algorithme 3
------------

.. literalinclude:: ../python/algos.py
   :lines: 14 - 19
   :linenos:
   
#. On réalise en console l'appel :

   >>> algo_3([7,3,8,4,9,5],6)

   -  Combien de fois les instructions aux lignes 4 et 5 sont-elles réalisées ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. On réalise un nouvel appel en console:

   >>> algo_3([i**2 for i in range(100)],1000)

   -  Combien de fois les instructions aux lignes 4 et 5 sont-elles réalisées ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. De façon générale, quel lien existe-t-il entre le tableau et le nombre d'exécutions des instructions aux lignes 4 et 5 ?

Algorithme 4
------------

.. literalinclude:: ../python/algos.py
   :lines: 21 - 26
   :linenos:
   
#. On réalise en console l'appel :

   >>> algo_4([[7,3,8],[4,9,5],[1,2,6]])

   -  Combien de fois l'instruction en ligne 6 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. On réalise un nouvel appel en console:

   >>> algo_4([ [i for i in range(j,j+10)] for j in range(10)])

   -  Combien de fois l'instruction en ligne 6 est-elle réalisée ?
   -  Quelle est la valeur renvoyée par la fonction ?

#. De façon générale, quel lien existe-t-il entre le tableau et le nombre d'exécutions de l'instruction à la ligne 6 ?