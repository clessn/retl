# Template de projet R

## Features
* réutilisable
* reproductible
* dockerizable

## Concept d'environnement
On utilise ici le package `renv`, qui permet d'installer localement les packages nécessaires et de noter les versions exactes pour  (du mieux qu'on peut) la reproductibilité sur un autre environnement. Il s'agit donc d'une habitude de travail à prendre, soit de "repartir à zéro" pour chaque projet et de déterminer les packages minimaux nécessaires. En partageant nos projets et le fichier `renv.lock`, un autre utilisateur peut installer une version locale de chaque package R de la même version que vous afin de s'assurer que l'exécution du code est similaire. C'est aussi une belle façon de s'assurer que tous ont les bons packages avant de tomber sur une erreur.


## Comment m'utiliser
* s'assurer d'avoir installé `renv` avec `install.packages("renv")`
* déterminer les packages R qui seront nécessaires
* s'assurer que RStudio détecte l'environnement renv plutôt que l'environnement global
  * RStudio devrait n'afficher que renv comme package installé.
  * Si vous trouvez vos packages comme dplyr ou autre, c'est que l'environnement ne fonctionne pas, redémarrez RStudio
* dans la console R, installer les packages nécessaires un après l'autre
* taper `renv::snapshot()`; renv stockera les packages et les versions que vous avez installé
* développer votre projet. À chaque fois que vous devez installer un nouveau package ou en retirer un, assurez vous de `renv::snapshot()` pour mettre à jour renv.lock
* Tester votre projet final en roulant `Rscript main.R`, ce qui roulera votre script en entier (l'équivalent de sourcer). Si votre script fonctionne, on pourra dockeriser et le publier.

## Tester la version dockerizée
```sh
docker build -t my-project .
docker run my-project
```

## Aide-mémoire
```R
renv::init() # créer un environnement renv de toute pièce, insi que le .Rprofile
# ce n'Est pas nécessaire si un renv.lock et un .Rprofile sont déjà présent

# .Rprofile est un fichier qui est détecté par R (et RStudio) et qui exécute le code à chaque démarrage de RStudio (ou d'une console R)

renv::snapshot()
# j'ai installé plusieurs packages et je veux mettre à jour renv.lock

renv::restore()
# j'ai téléchargé un repo avec un renv.lock et un .Rprofile, et j'aimerais avoir un environnement renv identique à celui du développeur

renv::restore()
# s'applique ausi si j'ai installé un package sans faire snapshot(), mais que j'aimerais rapidement revenir à l'état précédent

# si on vous a fourni un renv.lock et rien d'autre (pas de .Rprofile, par exemple), vous pouvez renv::init(), puis remplacer le renv.lock par le vôtre.
```
