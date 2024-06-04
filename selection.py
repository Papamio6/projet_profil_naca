# -------------------------------------------------------------------------- #
            #SCRIPT DE RECUPERATION DE DONNEES PROFIL NACA00XX#
# -------------------------------------------------------------------------- #
# Emilio Scottu
# MGA-802

# Ce script permet de récupérer les données d'un profil NACA00XX auprès
# de l'utilisateur


# -------------------------------------------------------------------------- #
                              #INSTRUCTIONS#
# -------------------------------------------------------------------------- #
def menu_accueil():
    # Utilisation d'un verrou permettant de mettre en place une sécurité pour chacune des
    # étapes de récupération de données
    verrou = 0 # étape 1
    print(" _______________________________________")
    print("|              Bonjour,                 |")
    print("|                                       |")
    print("|   cet algorithme permet de générer    |")
    print("|       et de tracer des profils        |")
    print("|         NACA00XX symétriques          |")
    print("|_______________________________________|")

# Récupération des deux derniers chiffres du profil NACA00XX :
    while verrou < 1:
        print("\n _______________________________________")
        print("|      Entrez les deux derniers         |")
        print("|     chiffres du profil NACA00XX       |")
        print("|_______________________________________|")
        chiffre_profil = (input('-->'))
        # On passe le verrou à l'étape 2 seulement si l'entrée est bien un nombre de deux caractères
        if(chiffre_profil.isnumeric() and len(chiffre_profil) ==2):
            verrou+=1
            print(" _______________________________________")
            print(f"|      Vous avez entré le profil :      |")
            print(f"|             NACA 00{chiffre_profil}                 |")
            print("|_______________________________________|")
            chiffre_profil = int(chiffre_profil)
            epaisseur_relative = chiffre_profil/100
        # Sinon, on demande à l'utilisateur de mieux saisir sa réponse
        else:
            print(" _______________________________________")
            print("|     Entrez seulement deux chiffres    |")
            print("|          comme 25 pour NACA0025       |")
            print("|_______________________________________|")


    # Récupération de la longueur de la corde en mètres :
    while verrou<2:
        print("\n _______________________________________")
        print("|     Entrez la longueur de la corde    |")
        print("|               en mètres               |")
        print("|_______________________________________|")
        corde_longueur = (input('-->'))
        # On passe le verrou à l'étape 3 seulement si l'entrée est bien un nombre
        if(corde_longueur.isnumeric()):
            verrou+=1
            corde_longueur=float(corde_longueur)

        # Sinon, on demande à l'utilisateur de mieux saisir sa réponse
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

        # On passe le verrou à l'étape 4 seulement si l'entrée est bien un nombre supérieur à 2 (pour le tracé futur)
        if nbre_points_x.isnumeric():
            if int(nbre_points_x)>=2:
                verrou+=1
                nbre_points_x=int(nbre_points_x)

            # Sinon, on demande à l'utilisateur de mieux saisir sa réponse
            else:
                print(" _______________________________________")
                print("|      Donnez un nombre de points       |")
                print("|            plus grand que 1           |")
                print("|_______________________________________|")

        # Sinon, on demande à l'utilisateur de mieux saisir sa réponse
        else:
            print(" _______________________________________")
            print("| Entrez un nombre entier correspondant |")
            print("|          au nombre de points          |")
            print("|       à utiliser pour le tracé        |")
            print("|_______________________________________|")


    # Choix du mode linéaire(1) ou non-uniforme(2) :
    while verrou<4:
        print("\n _______________________________________")
        print("|      Choisissez le mode de tracé      |")
        print("|    (1) linéaire  (2) non-uniforme :   |")
        print("|_______________________________________|")
        mode = (input('-->'))

        # On passe le verrou à l'étape 5 seulement si l'entrée est bien 1 ou 2
        if mode.isnumeric() and 1<=int(mode)<=2:
            verrou+=1
            mode = int(mode)

        # Sinon, on demande à l'utilisateur de mieux saisir sa réponse
        else:
            print(" _______________________________________")
            print("|     Entrez (1) pour mode linéaire     |")
            print("|      (2) pour mode non-uniforme       |")
            print("|_______________________________________|")

    return(epaisseur_relative,nbre_points_x,corde_longueur,mode)