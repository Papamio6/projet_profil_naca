"""Ce script permet d'entrer un profil NACA 00XX pour l'afficher dans une figure"""

def menu_accueil():
    verrou = 0

    # chiffres du profil :
    while verrou < 1:
        print("Entrez les deux derniers chiffres du profil NACA00XX")
        chiffre_profil = (input('-->'))
        if(chiffre_profil.isnumeric() and len(chiffre_profil) ==2):
            verrou+=1
            chiffre_profil = int(chiffre_profil)
            print(f"Vous avez entré le profil : NACA 00{chiffre_profil}")
            epaisseur_relative = chiffre_profil/100
        else:
            print("Entrez seulement deux chiffres")



    #longueur de la corde :
    while verrou<2:
        print("Entrez la longueur de la corde :")
        corde_longueur = (input('-->'))
        if(corde_longueur.isnumeric()):
            verrou+=1
            corde_longueur=float(corde_longueur)
        else:
            print("Entrez un nombre correspondant à la longueur de la corde en mètres")


    #nombre de points pour la corde :
    while verrou<3:
        print("Entrez le nombre de points pour tracer la corde :")
        nbre_points_x = (input('-->'))
        if nbre_points_x.isnumeric():
            if int(nbre_points_x)>=2:
                verrou+=1
                nbre_points_x=int(nbre_points_x)
            else:
                print("Donnez un nombre de points au moins plus grand que 1")
        else:
            print("Entrez un nombre entier correspondant au nombre de points à utiliser pour le tracé")


    #Mode linéaire(1) ou non-uniforme(2) :
    while verrou<4:
        print("Choisissez le mode de tracé\n(1) linéaire  (2) non-uniforme  :")
        mode = (input('-->'))
        if mode.isnumeric() and 1<=int(mode)<=2:
            verrou+=1
            mode = int(mode)
        else:
            print("Entrez (1) pour mode linéaire ou (2) pour mode non-uniforme")

    return(epaisseur_relative,nbre_points_x,corde_longueur,mode)