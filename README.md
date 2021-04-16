# PROJET PYTHON BATTLE PUNCHLINERS

Bonjour, voici notre petit projet sur pygame et python, dans lequel nous devions mettre en place un jeu d'insultes. Nous allons vous expliquer en détails le jeu, et son fonctionnement.

##Comment lancer le jeu ?

Après avoir cloné le repo, vous allez lancer à l'aide de python le jeu avec la commande `py ./main.py` ou `python ./main.py` si vous utiliser python. Vous pouvez également utiliser un compilateur avec le logiciel IDLE, ou Anaconda.

## Comment se déroule le jeu ?

Une fois le programme lancé, vous devriez tomber sur une proposition. En effet, selon vos goûts et désirs il est possible de lancer le jeu via la console, ou en graphique. Il sera toutefois nécessaire de disposer du framework Pygame.
Le jeu nécessite **deux joueurs**, chacun pourra choisir son personnage. Il y a au total 5 personnages. Le but **est de faire l'insulte la plus percutante et la plus intelligente**.

Voici un exemple du visuel **en console :**

```PS C:\Users\utilisateur\Desktop\Rayane\Cours\Bachelor 1\Développement\Python\Projet Python\V2> py .\main.py
Bienvenue sur Battle punchliners ! Voulez vous jouer en graphique (tapez 1), ou en console (tapez 2), ou quitter (tapez 3) ? 2
Il y a 7 personnages disponibles, veuillez choisir le votre, en selectionnant un nombre de 1 à 7. Voici les personnages :
- Granma
- Baby
- Criminel
- IronMan
- B2OBiatch
Joueur 1 choisissez votre joueur :
```

Et **en graphique** :

**Inserer une image**

## Comment se déroule la partie ?

La partie se déroule tour à tour, chacun ayant une panoplie de verbes, sujets, compléments à utiliser. Les points d'attaques sont calculés en fonction de la cohérence de la phrase (accord sujet-verbe-complément), des points d'attaques du joueurs, ainsi qu'un multiplicateur au cas où on a dit un mot qui represente un point faible de l'adversaire. On peut mulptiplier l'attaque de base jusqu'à **15 fois !**
Le premier joueur qui n'a plus de pv perds la partie !

Voici un exemple d'une attaque en **console :**

```
C'est partie pour le combat....

 Chargement en cours.........


C'est PARTIE !
Au tour du joueur  1
Voici vos sujets :  ['ton visage', 'Ta soeur', 'Tu', 'En toute honneteté tu', 'Pour moi tu', 'Tu']
Voici vos verbe :  ['me balade', 'es', 'es', 'être', 'me balade', 'être']
Voici vos compléments :  ['dans une vitrine à Amsterdam', 'tes grands morts', 'ta mère', 'ton honneur', 'pour toi', 'le meilleur']
Veuillez choisir, en commençant par le sujet, verbe, compléments, votre séléction : 111
PUNCHLINE DE baby  :  Ton visage me balade dans une vitrine à Amsterdam


VOTRE SCORE D'ATTACK EST DE :  80
VOTRE SCORE DE COHERENCE EST DE :  2
PPPWWWWAAAAAA


IronMan  a encore  170 pv

Au tour du joueur 2...
```

**Et en graphique :**

**Inserer une img**

**NOTE :** La méthode de séléction (personnages, attaques...) se portera essentiellement sur la séléction des chiffres. Par exemple, pour choisir le joueur 1, on écrira "1" lorsque l'on demandera de séléctionner le joueur que l'on veut prendre. Il en est de même pour les punchlines. Si l'on souhaite utiliser le premier sujet, second verbe et troixième sujet, il suffira d'entrer le nombre 123. On validera grâce à la touche **Entrer**.

**ATTENTION !** Une valeur qui n'est pas bien rentrée (caractère incorrect, nombre trop grand, etc...) vous fais perdre votre tour !

## Un jeu de stratégie !

Dans ce jeu, place à la stratégie ! Chaque personnage possède plus ou moins de faiblesses, d'attaque, et de points de vie. Choisir un joueur avec beaucoup de pv mais avec pas mal de faiblesses ? Ou un joueur moins défensif mais plus offensif ? Voici la liste des personnages, et leurs stats respectives. A vous les punchlines !

| Nom et numéro personnages | Point de vie | Attaque | Nombres de faiblesses |
| ------------------------- | ------------ | ------- | --------------------- |
| 1 - Granma                | 380          | 15      | Normal                |
| 2 - Baby                  | 250          | 20      | Normal                |
| 3 -Criminal               | 70           | 70      | Très peu              |
| 4 - IronMan               | 900          | 11      | Légèrement importante |
| 5 - B20Biatch             | 1500         | 9       | Assez importante      |
