# Programme de génération de profils NACA00XX symétriques :
#### Bienvenue sur le dépôt GitHub du traceur graphique de profils NACA00XX symétriques.
## PRINCIPE DE L'ALGORITHME
Ce projet a pour objectif de permettre à un utilisateur d'entrer les données d'un profil pour obtenir le tracé graphique de ce dernier. Pour obtenir un tracé, il faut fournir : 
- Le numéro du profil NACA00XX symétrique
- La corde du profil (en mètre)
- Le nombre de points le long de la corde
- Le type de distribution des points le long de la corde : linéaire ou non-uniforme


## CONTENU DU DEPOT
  le dépôt est composé de scripts permettant la bonne exécution du programme en général. On retrouve : 
  - Un fichier README.md
  - Un script main.py
  - Un script selection.py
  - Un script calcul_profil.py 
  - Un script affichage.py


## LISTE DES FONCTIONS PRESENTES
Dans le projet entier, on retrouve un certain nombre de fonctions qui sont listées ci-dessous : 
+ affichage() est une procédure qui permet d'afficher graphiquement le profil d'aile NACA00XX spécifié en entrée
+ calcul_profil() est une fonction qui permet de calculer et de retourner les points d'abscisses composant le long de la corde, les ordonnées de l'intrados et de l'extrados pour un profil d'aile spécifié
+ menu_accueil() est une fonction qui permet de récupérer les données d'un profil NACA00XX auprès de l'utilisateur

## MANUEL D'UTILISATION 
Pour pouvoir lancer le programme, il faut télécharger le dépôt entier car tous les fichiers sont nécessaires. 
Pour lancer l'algorithme, il faut lancer le script main.py. 

Lorsque ce dernier s'exécute, l'utilisateur va devoir répondre à 4 questions permettant au script de récupérer les données du profil NACA symétrique. 
- Le numéro du profil NACA00XX symétrique : est lié à l'épaisseur relative du profil par la formule $t=XX/100$
- La corde du profil (en mètre) : définie la longueur de la corde du profil en mètres
- Le nombre de points le long de la corde : impose le nombre d'échantillons qui composeront le tracé (plus le nombre est grand, plus la qualité du tracé est bonne mais moins le programme est performant)
- Le type de distribution des points le long de la corde : linéaire ou non-uniforme 


Les indications sont claires et précises, si jamais l'utilisateur entre une réponse qui n'est pas attendue, le programme boucle et repose la question en spécifiant les points sur lesquels il est important de faire attention.

Le résultat de la saisie de toutes les informations sur le profil est la génération et le tracé du profil en question sur un graphique qui appartait dans une fenêtre externe. 
