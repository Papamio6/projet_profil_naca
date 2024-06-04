# -------------------------------------------------------------------------- #
            #SCRIPT D'AFFICHAGE DU PROFIL NACA00XX#
# -------------------------------------------------------------------------- #
# Emilio Scottu
# MGA-802

# Ce script est composé d'une procédure permettant d'afficher graphiquement
# le profil d'aile NACA00XX spécifié en entrée


# -------------------------------------------------------------------------- #
                              #IMPORTATION#
# -------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

# -------------------------------------------------------------------------- #
                              #INSTRUCTIONS#
# -------------------------------------------------------------------------- #

def affichage(listes_points,donnees_profil):
    # On crée notre figure ainsi que notre zone de tracé :
    fig, ax = plt.subplots()
    # On y trace l'extrados puis l'intrados :
    ax.plot(listes_points[0], listes_points[1], linewidth=2.0, label="Extrados")
    ax.plot(listes_points[0], listes_points[2], linewidth=2.0, label="Intrados")
    # On ajoute une méthode de centrage graphique :
    ax.set_ylim(top=max(listes_points[1]) + 10, bottom=min(listes_points[2]) - 10)
    ax.set_xlim(right=max(listes_points[0]) + 10, left=min(listes_points[0]) - 10)
    # On active les légendes et la grille du graphique
    ax.legend()
    ax.grid()
    # On ajoute les noms des axes
    ax.set_xlabel("x en mètres")
    ax.set_ylabel("y en mètres")

    # On indique la méthode utilisée et indiquée par l'utilisateur
    if(donnees_profil[3]==1):
        plt.title(f"Tracé du profil NACA00{int(donnees_profil[0]*100)} avec la méthode linéaire")
    else:
        plt.title(f"Tracé du profil NACA00{int(donnees_profil[0]*100)} avec la méthode non-uniforme")

    # On affiche la figure contenant le graphique
    plt.show()
