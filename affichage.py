import matplotlib.pyplot as plt


def affichage(listes_points):
    fig, ax = plt.subplots()
    ax.plot(listes_points[0], listes_points[1], linewidth=2.0, label="Extrados")
    ax.plot(listes_points[0], listes_points[2], linewidth=2.0, label="Intrados")
    ax.legend()
    ax.set_ylim(top=max(listes_points[1]) + 10, bottom=min(listes_points[2]) - 10)
    ax.set_xlim(right=max(listes_points[0]) + 10, left=min(listes_points[0]) - 10)

    plt.show()
