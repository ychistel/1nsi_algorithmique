Comment trier un tableau ?
==========================

Le langage Python possède une méthode de tri pour les listes: la méthode ``sort``. Lorsque les listes contiennent des valeur simples comme des nombres ou des chaines de caractères, l'utilisation de la méthode est simple.

On a vu avec le problème du **sac à dos** que l'utilisation de cette méthode est plus complexe et nécessite l'usage d'une fonction anonyme ``lambda``. Est-il possible de trier un tableau de valeurs sans utiliser la méthode de Python ?

Il existe de nombreux algorithmes de tri de tableaux. Nous allons en étudier 2 en particulier. Mais d'abord, interrogeons-nous sur l'algorithme de tri ?

#. Quelles méthodes utilisez-vous pour trier un jeu de cartes ?

   .. image:: ../img/cartes.svg
      :alt: cartes à jouer
      :align: center
      :width: 480

#. Donner les différentes étapes nécessaires pour trier les tableaux dans les cas suivants:

   a. ``t=[1,3,7,11,8]``
   b. ``t=[1,3,7,11,8,9]``
   c. ``t=[1,3,7,14,11,8,9]``
   d. ``t=[1,3,7,10,14,17,9,12,8]``

#. Écrire un algorithme en pseudo-code ou langage naturel mettant en oeuvre les tris effectués précédemment.

#. On applique l'algorithme sur le tableau de nombres suivants : ``t=[1,3,5,7,2]``.

   a. Trouvez-vous l'algorithme précédent adapté à ce cas de figure?
   b. Quelle méthode semblerait plus adaptée pour trier le tableau?
   c. Cet algorithme peut-il s'appliquer à tout tableau?

#. Écrire un algorithme en pseudo-code ou langage naturel mettant en oeuvre la remarque précédente.
#. Ces algorithmes se terminent-ils dans tous les cas ? Justifier.
#. Quel est la complexité des 2 algorithmes de tris?
