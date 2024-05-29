"""Ce fichier main fait le lien entre toutes les fonctions, c'est le coeur du logiciel"""
from selection import menu_accueil
from calcul_profil import calcul_profil
import matplotlib.pyplot as plt

donnees_profil = menu_accueil()

listes_points = calcul_profil(donnees_profil)

fig, ax = plt.subplots()
ax.plot(listes_points[0], listes_points[1], linewidth=2.0)
ax.plot(listes_points[0], listes_points[2], linewidth=2.0)
ax.set_ylim(bottom=max(listes_points[1])+10, top=min(listes_points[2])-10)
ax.set_xlim(right=max(listes_points[0])+10, left=min(listes_points[0])-10)

plt.show()