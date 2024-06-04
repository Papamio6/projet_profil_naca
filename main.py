# -------------------------------------------------------------------------- #
               #SCRIPT GENERATION ET TRACE PROFIL NACA00XX#
# -------------------------------------------------------------------------- #
# Emilio Scottu
# MGA-802

# Ce script permet à tout utilisateur qui l'exécute de générer et tracer le profil
# NACA00XX symétrique de son choix

# Pour tous les choix proposés au cours de l'execution, si l'utilisateur donne une
# réponse non attendue, l'algorithme revient toujours en arrière pour demander à
# l'utilisateur de rectifier sa réponse.


# -------------------------------------------------------------------------- #
                            #ZONE D'IMPORTATION#
# -------------------------------------------------------------------------- #
from selection import menu_accueil
from calcul_profil import calcul_profil
from affichage import affichage

# -------------------------------------------------------------------------- #
                              #INSTRUCTIONS#
# -------------------------------------------------------------------------- #
# On récupère les données décrivant le profil auprès de l'utilisateur
donnees_profil = menu_accueil()

# On calcule les coordonnées des points pour tracer y_up, y_down et x_c
listes_points = calcul_profil(donnees_profil)

# On lance l'affichage du graphique
affichage(listes_points, donnees_profil)
