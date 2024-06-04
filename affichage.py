import matplotlib.pyplot as plt


def affichage(listes_points,donnees_profil):
    fig, ax = plt.subplots()
    ax.plot(listes_points[0], listes_points[1], linewidth=2.0, label="Extrados")
    ax.plot(listes_points[0], listes_points[2], linewidth=2.0, label="Intrados")
    ax.set_ylim(top=max(listes_points[1]) + 10, bottom=min(listes_points[2]) - 10)
    ax.set_xlim(right=max(listes_points[0]) + 10, left=min(listes_points[0]) - 10)
    ax.legend()
    ax.grid()
    ax.set_xlabel("abscisses en mètres")
    ax.set_ylabel("ordonnées en mètres")

    if(donnees_profil[3]==1):
        plt.title(f"Tracé du profil NACA00{int(donnees_profil[0]*100)} avec la méthode linéaire")
    else:
        plt.title(f"Tracé du profil NACA00{int(donnees_profil[0]*100)} avec la méthode non-uniforme")

    plt.show()
