"""Ce script permet d'entrer un profil NACA 00XX pour l'afficher dans une figure"""

import numpy as np

# chiffres du profil :
print("entrer les deux derniers chiffres du profil")
code_profil = input('-->')
print(f"vous avez entré le profil : NACA 00{code_profil}")

epaisseur_relative = code_profil/100

#longueur de la corde :
print("entrer la longueur de la corde :")
corde_longueur = input('-->')


#nombre de points pour la corde :
print("entrer le nombre de points pour tracer la corde :")
nbre_points_x = input('-->')