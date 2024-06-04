"""Ce script permet d'entrer un profil NACA00XX pour l'afficher dans une figure"""

def menu_accueil():
    verrou = 0
    print(" _______________________________________")
    print("|              Bonjour,                 |")
    print("|                                       |")
    print("|   cet algorithme permet de générer    |")
    print("|       et de tracer des profils        |")
    print("|         NACA00XX symétriques          |")
    print("|_______________________________________|")

    # chiffres du profil :
    while verrou < 1:
        print("\n _______________________________________")
        print("|      Entrez les deux derniers         |")
        print("|     chiffres du profil NACA00XX       |")
        print("|_______________________________________|")
        chiffre_profil = (input('-->'))
        if(chiffre_profil.isnumeric() and len(chiffre_profil) ==2):
            verrou+=1
            chiffre_profil = int(chiffre_profil)
            print(" _______________________________________")
            print(f"|      Vous avez entré le profil :      |")
            print(f"|             NACA 00{chiffre_profil}                 |")
            print("|_______________________________________|")

            epaisseur_relative = chiffre_profil/100
        else:
            print(" _______________________________________")
            print("|     Entrez seulement deux chiffres    |")
            print("|          comme 25 pour NACA0025       |")
            print("|_______________________________________|")


    #longueur de la corde :
    while verrou<2:
        print("\n _______________________________________")
        print("|     Entrez la longueur de la corde    |")
        print("|               en mètres               |")
        print("|_______________________________________|")
        corde_longueur = (input('-->'))
        if(corde_longueur.isnumeric()):
            verrou+=1
            corde_longueur=float(corde_longueur)
        else:
            print(" _______________________________________")
            print("|    Entrez un nombre correspondant     |")
            print("|  à la longueur de la corde en mètres  |")
            print("|_______________________________________|")


    #nombre de points pour la corde :
    while verrou<3:
        print("\n _______________________________________")
        print("|      Entrez le nombre de points       |")
        print("|    pour tracer la corde (entier):     |")
        print("|_______________________________________|")
        nbre_points_x = (input('-->'))
        if nbre_points_x.isnumeric():
            if int(nbre_points_x)>=2:
                verrou+=1
                nbre_points_x=int(nbre_points_x)
            else:
                print(" _______________________________________")
                print("|      Donnez un nombre de points       |")
                print("|            plus grand que 1           |")
                print("|_______________________________________|")

        else:
            print(" _______________________________________")
            print("| Entrez un nombre entier correspondant |")
            print("|          au nombre de points          |")
            print("|       à utiliser pour le tracé        |")
            print("|_______________________________________|")


    #Mode linéaire(1) ou non-uniforme(2) :
    while verrou<4:
        print("\n _______________________________________")
        print("|      Choisissez le mode de tracé      |")
        print("|    (1) linéaire  (2) non-uniforme :   |")
        print("|_______________________________________|")

        mode = (input('-->'))
        if mode.isnumeric() and 1<=int(mode)<=2:
            verrou+=1
            mode = int(mode)
        else:
            print(" _______________________________________")
            print("|     Entrez (1) pour mode linéaire     |")
            print("|      (2) pour mode non-uniforme       |")
            print("|_______________________________________|")

    return(epaisseur_relative,nbre_points_x,corde_longueur,mode)