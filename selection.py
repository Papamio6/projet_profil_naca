"""Ce script permet d'entrer un profil NACA 00XX pour l'afficher dans une figure"""

def menu_accueil():
    # chiffres du profil :
    print("entrer les deux derniers chiffres du profil")
    chiffre_profil = int(input('-->'))
    print(f"vous avez entré le profil : NACA 00{chiffre_profil}")

    epaisseur_relative = chiffre_profil/100

    #longueur de la corde :
    print("entrer la longueur de la corde :")
    corde_longueur = float(input('-->'))


    #nombre de points pour la corde :
    print("entrer le nombre de points pour tracer la corde :")
    nbre_points_x = int(input('-->'))


    #Mode linéaire(1) ou non-uniforme(2) :
    print("entrer le nombre de points pour tracer la corde :")
    mode = int(input('-->'))


    return(epaisseur_relative,nbre_points_x,corde_longueur,mode)