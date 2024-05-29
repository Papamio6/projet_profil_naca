"""Ce code permet de calculer et de retourner
les points composant la corde, l'intrados et l'extrados d'un profil d'aile spécifié"""

import numpy as np


def calcul_profil(t,nbre_points_x,c):

    X_c = np.linspace(0,1,nbre_points_x)
    Y_c_up = []
    for x_c in X_c:
        y_c = 5*t*(0.2969*np.sqrt(x_c)-0.1260*x_c-0.3516*x_c**2+0.2843*x_c**3-0.1036*x_c**4)
        Y_c_up.append(y_c)
    Y_c_up = [y_c*c for y_c in Y_c_up]
    Y_c_down = [-y_c for y_c in Y_c_up]
    X_c = [x_c*c for x_c in X_c]

    return (X_c, Y_c_up, Y_c_down)

