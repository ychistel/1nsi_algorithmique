Exercices
=========

Exercice 1
----------
On donne l'algorithme suivant:

.. literalinclude:: ../python/exercice.py
	:language: python
	:linenos:
	:lines: 3-8

#. On réalise l'appel suivant:

	>>> occurence([1,2,1,2,2,1,2,1,1,1,2],1)

	Combien de fois l'instruction en ligne 5 est-elle exécutée ?

#. On réalise l'appel suivant:

	>>> occurence([i*2 for i in range(50)],50)

	Combien de fois l'instruction en ligne 5 est-elle exécutée ?

#. Quelle est la complexité de cette recherche d'occurence dans un tableau de dimension :math:`n` ?

Exercice 2
----------
La recherche d'une valeur minimale ou maximale dans un tableau de nombres peut se faire en Python avec les fonctions ``min`` et ``max``.

Ici, on s'intéresse à la recherche de ces valeurs particulières sans utiliser les fonctions ``min`` et ``max`` de python.

#. Soit ``t`` un tableau de nombres trié dans l'ordre croissant.

   a. Comment obtient-on la valeur minimale du tableau ? La valeur maximale ?
   b. Quelles est la complexité de chacune de ces recherches ?

#. On suppose maintenant que le tableau ``t`` n'est pas trié. Donner un algorithme de recherche de la valeur minimale de ce tableau.
#. Écrire la fonction Python ``recherche_min`` qui prend en paramètre un tableau non trié et qui renvoie la valeur minimale du tableau.
#. Tester votre fonction avec le tableau ``t`` tel que:

   a. ``t = [7,2,9,8,6,4,9,1,5,6]``
   b. ``t = [ i % 37 for i in range(5,100,7)]``

#. Quelle est la complexité de l'algorithme de recherche de la valeur minimale ?

Exercice 3
----------
On reprend la fonction Python ``recherche_min`` que l'on va adapter pour chacune des situations suivantes.

#. Écrire la fonction ``recherche_max`` qui renvoie la valeur maximale d'un tableau non trié.
#. Écrire la fonction ``recherche`` qui renvoie un tuple contenant à la fois la valeur minimale et la valeur maximale du tableau.
#. Écrire la fonction ``recherche_entre`` qui a 2 paramètres supplémentaires ``debut`` et ``fin``. Cette fonction renvoie la valeur minimale comprise entre les indices passés en arguments et représentés par les paramètres ``debut`` et ``fin``.

   Par exemple, pour le tableau ``t = [7,2,9,8,6,4,9,1,5,6]``, l'appel ``recherche_entre(t,3,6)`` renvoie la valeur 4. C'est la valeur minimale du sous-tableau ``[8,6,4,9]``.
