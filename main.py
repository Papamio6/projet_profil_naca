"""Ce fichier main fait le lien entre toutes les fonctions, c'est le coeur du logiciel"""
from selection import menu_accueil
from calcul_profil import calcul_profil
from affichage import affichage

donnees_profil = menu_accueil()

listes_points = calcul_profil(donnees_profil)

affichage(listes_points)
