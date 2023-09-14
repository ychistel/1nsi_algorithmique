.. TNSI

Mesure du temps d'exécution
===========================

.. _epoch: https://docs.python.org/fr/3/library/time.html#epoch

Python dispose d'un module ``time`` qui permet de mesurer le temps. La fonction ``time`` de ce module donne le temps
écoulé en seconde depuis `epoch`_ sous la forme d'un flottant. Le terme *epoch* désigne la date du 1/1/1970 à partir de
laquelle le temps est mesuré en informatique.

La fonction ``mesure_tri`` prend en paramètre ``fct`` qui est une chaine de caractères dont la valeur est le nom de la
fonction à mesurer. Un second paramètre ``n`` indique la taille du tableau à créer et à trier.

.. literalinclude:: ../python/tp_mesure_tri.py
   :language: python
   :lines: 1-27
   :linenos:

La fonction ``mesure_tri`` effectue 50 exécutions de la fonction à mesurer et calcule le temps total dans la variable
``tps``. La fonction renvoie le temps moyen d'exécution en divisant le temps total par 50.

Les 2 fonctions de tri sont regroupées dans le fichier ``tris.py``. On les importe dans le fichier de travail.

.. literalinclude:: ../python/tp_mesure_tri.py
   :lines: 30-32

#. Effectuer une première mesure du tri par selection avec un tableau de dimension ``n=100``. Quel est le temps d'exécution du tri par selection dans ce cas ?

#. Effectuer une première mesure du tri par insertion avec un tableau de dimension ``n=100``. Quel est le temps d'exécution du tri par selection dans ce cas ?

#. Effectuer une mesure pour chaque tri avec un tableau de dimension ``n=500``. Par quel facteur a été multiplié le
   temps d'exécution par rapport au temps d'exécution d'un tableau de dimension ``n=100``?

#. Vérifier que le temps d'exécution est 100 fois plus long pour chaque tri en prenant un tableau de dimension
   ``n=1000``.

#. En réalisant plusieurs tests, contrôler que lorsque la dimension du tableau est multipliée par un facteur :math:`k`,
   alors le temps d'exécution est multiplié par :math:`k^{2}`.
