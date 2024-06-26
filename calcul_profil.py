# -------------------------------------------------------------------------- #
            #SCRIPT DE CALCUL DES COURBES DU PROFIL NACA00XX#
# -------------------------------------------------------------------------- #
# Emilio Scottu
# MGA-802

# Ce code est composé d'une fonction permettant de calculer et de retourner
# les points composant la corde, l'intrados et l'extrados d'un profil d'aile spécifié


# -------------------------------------------------------------------------- #
                              #IMPORTATION#
# -------------------------------------------------------------------------- #
import numpy as np


# -------------------------------------------------------------------------- #
                              #INSTRUCTIONS#
# -------------------------------------------------------------------------- #

# datas composées de t, nbre de points et c
def calcul_profil(datas):
    # on récupère la thickness, le nombre de points, la longueur de la corde et le mode via
    # le paramètre d'entrée datas
    t= datas[0]
    nbre_points_x = datas[1]
    c = datas[2]
    mode = datas[3]

    # Si l'utilisateur a choisi le mode linéaire :
    # on crée le vecteur vect_x_c composé des valeurs des points le long de la corde
    if mode ==1:
        vect_x_c = np.linspace(0,1, nbre_points_x)
    
    # Si l'utilisateur a choisi le mode non-uniforme :
    else:
       theta = np.linspace(0, np.pi, nbre_points_x)
       vect_x_c = 0.5*(1-np.cos(theta))

    # Ici, on va créer les tableaux à une dimension vect_y_up et vect_y_down en utilisant la formule donnée
    # dans le sujet pour chaque point du vecteur vect_x_c.
    # On dénormalise tous les tableaux à une dimension en multipliant les valeurs par la corde
    vect_y_up = 5*t*(0.2969*np.sqrt(vect_x_c)-0.1260*vect_x_c-0.3516*vect_x_c**2+0.2843*vect_x_c**3-0.1036*vect_x_c**4)*c
    vect_y_down = -vect_y_up
    vect_x_c = vect_x_c*c

    # On retourne les tableaux à une dimension contenant les points de la corde, l'extrados et l'intrados
    return (vect_x_c, vect_y_up, vect_y_down)

