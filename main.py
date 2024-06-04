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
donnees_profil = menu_accueil()

listes_points = calcul_profil(donnees_profil)

affichage(listes_points, donnees_profil)
