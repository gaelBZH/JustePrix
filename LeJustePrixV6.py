import random       # Variables :   levelfloat ; levelint ; joueurfloat ; joueurint ; tour ; essais ; essaisj1 ; essaisj2 ; essaisj3 ; essaisj4 ; essaisj5 ; parties ; tresor ; nombre ; action ; choixFinDePartie ; lang
import os           # Modules : Random ; Os

# RÈGLES #

# Dans le jeu du Juste Prix, le but est de trouver une valeur aléatoire cachée appelée "Trésor".
# Cette valeur est un nombre entier et est choisie aléatoirement dans un ensemble dépendant du niveau.
# Dans le Niveau 1 (Facile), le nombre sera entre 1 et 100 inclus. Plus un niveau est elevée, plus la fourchette l'est aussi.
# Les niveaux vont de 1 à 1000. Les premiers sont Facile, Moyen, Difficile, Très Difficile et Extrême.
# Au delà du Niveau 5, les niveaux sont personalisés jusqu'à 1000 inclus. La difficulté augmente de plus en plus.
# Chaque niveau démarre de 1 et s'achève à (1(10**(x+1))), où x est le niveau. Par exemple le niveau 1 sera jusqu'à 1*10² = 100.
# Un niveau décimal (Avec Virgule), sera automatiquement arrondi à l'unité et un message de convertion s'affichera au Joueur.
# Si le niveau est invalide (Inférieur à 1 ou Supérieur à 1000), un message d'invalidité s'affichera.
# Si le niveau est encore invalide après un deuxième essai, le Niveau par défaut sera le Niveau 1- Facile (1-100).
# Une fois le niveau chosi et le Trésor attribué, le joueur doit envoyer un nombre au Jeu.
# Le Jeu lui répondra uniquement par "Plus" ou "Moins". Le Joueur devra donc envoyer un nombre Plus ou Moins grand.
# Une fois le Trésor trouvé, le Jeu enverra un message lui confirmant le bon résultat et son nombre d'essais.
# MODE MULTIJOUEUR : Il est possible de jouer jusqu'à 5 Joueurs au Jeu du Juste Prix.
# La Séléction du nombre de joueurs se fera juste après celle du niveau pour que tous les joueurs aient la même difficulté.
# Cette Séléction se déroule de la même façon que celle du niveau.
# Si le nombre de joueurs est invalide deux fois de suite, le nombre de joueurs sera de 1.
# Si le nombre de joueurs est égal à 1, alors le mode sera le Mode Solo.

# BON JEU #

os.system('cls' if os.name == 'nt' else 'clear')
lang='fr' # Langue Français par défaut
jeu=1 # Activé par défaut
print("-----------------")
print("Bienvenue dans le Jeu du Juste Prix 🎰")


while jeu==1: # Jeu==0 : Fin   Jeu==1 : En Route

    # FRANCAIS #
    if lang=='fr':
        print("-----------------")
        print("MENU 🌐")
        print("play - Démarrer une Partie")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Afficher les Règles du Jeu")
        print("lang - Changer la Langue")
        print("exit - Quitter le Jeu")
        print("-----------------")

        action=str(input("Séléctionner une Option : "))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Option Invalide : Veuillez réessayer.")
            action=str(input("Séléctionner une option : "))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Option Invalide.")
                jeu=0
                print("Fin du Jeu")
                exit()
        print("OPTION SÉLECTIONNÉE :", action)
        print("-----------------")

        if action=='play': 
            print("SÉLECTIONNER LE NIVEAU")
            print("1- Facile [1-100]")
            print("2- Moyen [1-1000]")
            print("3- Difficile [1-10000]")
            print("4- Très Difficile [1-100000]")
            print("5- Extrême [1-1000000]")
            print("x- Personalisé [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Niveau="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('Le Niveau ""',levelfloat,'""','a été arrondi au Niveau','""',levelint,'"".')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Niveau Invalide : Veuillez réessayer.")
                    levelfloat=float(input("Niveau="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print(" Le Niveau"" ",levelfloat, '""', "a été arrondi au Niveau",'""',levelint, '"".')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Niveau Invalide")
                      levelint=1
                      print("NIVEAU PAR DÉFAUT : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("SÉLECTIONNER LE NOMBRE DE JOUEURS")
            print("1 à 5 Joueurs")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Joueurs=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Nombre de joueur "',joueurfloat,'" arrondi en "',joueurint,'".')
                if joueurint<1 or joueurint>5:
                    print("Nombre de Joueurs Invalide : Veuillez réessayer.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Joueurs=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Nombre de joueur "',joueurfloat,'" arrondi en "',joueurint,'".')
                    if joueurint<1 or joueurint>5:
                      print("Nombre de Joueurs Invalide.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("JOUEURS PAR DÉFAUT : 1") 
            print("-----------------")

            tour=0
            essaisj1=0
            essaisj2=0
            essaisj3=0
            essaisj4=0
            essaisj5=0
            for parties in range(joueurint):
                nombre=0
                tour=tour+1
                if tour>1:
                    print("-----------------")
                if joueurint>1:
                    print("🎮 JOUEUR", tour, "🎮")
                if levelint==1:
                    print("NIVEAU",levelint," - Facile [1-100]")
                if levelint==2:
                    print("NIVEAU",levelint," - Moyen [1-1000]")
                if levelint==3:
                      print("NIVEAU",levelint," - Difficile [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("NIVEAU",levelint," - Très Difficile [1-100000]")
                if levelint==5:
                     print("NIVEAU",levelint," - Extrême [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("NIVEAU",levelint," - Personalisé [1-", (1*(10**(levelint+1))),"]")

                essais=0
                os.system('cls' if os.name == 'nt' else 'clear')   
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Nombre="))
                     if nombre<tresor:
                         print("Plus")
                     if nombre>tresor:
                         print("Moins")
                     essais=essais+1
                print("Bravo, la Réponse Était Bien", tresor)
                if tour<joueurint:                                                                              
                    tresor=random.randint(1, (1*(10**(levelint+1)))   )                                         # PARAGRAPHE JEU
                if tour==1:
                    essaisj1=essais
                if tour==2:
                    essaisj2=essais
                if tour==3:
                    essaisj3=essais
                if tour==4:
                    essaisj4=essais
                if tour==5:
                    essaisj5=essais
            if joueurint>1:
                print("-----------------")

            if joueurint>1:
                print("RÉSULTATS 🏅")
                if joueurint>=2:
                    print("Essais Joueur 1 :", essaisj1)
                    print("Essais Joueur 2 :", essaisj2)
                if joueurint>=3:
                    print("Essais Joueur 3 :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Essais Joueur 4 :", essaisj4)
                if joueurint>=5:
                    print("Essais Joueur 5 :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Nombre d'Essais :", essaisj1)
        if action=='rules':
            print("RÈGLES")
            print(" ")
            print('Dans le jeu du Juste Prix, le but est de trouver une valeur aléatoire cachée appelée "Trésor".')
            print("Cette valeur est un nombre entier et est choisie aléatoirement dans un ensemble dépendant du niveau.")
            print("Dans le Niveau 1 (Facile), le nombre sera entre 1 et 100 inclus. Plus un niveau est elevée, plus la fourchette l'est aussi.")
            print("Les niveaux vont de 1 à 1000. Les premiers sont Facile, Moyen, Difficile, Très Difficile et Extrême.")
            print("Au delà du Niveau 5, les niveaux sont personnalisés jusqu'à 1000 inclus. La difficulté augmente de plus en plus.")
            print("Chaque niveau démarre de 1 et s'achève à (1(10**(x+1))), où x est le niveau. Par exemple le niveau 1 sera jusqu'à 1*10² = 100.")
            print("Un niveau décimal (Avec Virgule), sera automatiquement arrondi à l'unité et un message de convertion s'affichera au Joueur.")
            print("Si le niveau est invalide (Inférieur à 1 ou Supérieur à 1000), un message d'invalidité s'affichera.")
            print("Si le niveau est encore invalide après un deuxième essai, le Niveau par défaut sera le Niveau 1- Facile (1-100).")
            print("Une fois le niveau choisi et le Trésor attribué, le joueur doit envoyer un nombre au Jeu.")
            print('Le Jeu lui répondra uniquement par "Plus" ou "Moins". Le Joueur devra donc envoyer un nombre Plus ou Moins grand.')
            print("Une fois le Trésor trouvé, le Jeu enverra un message lui confirmant le bon résultat et son nombre d'essais.")
            print("MODE MULTIJOUEUR : Il est possible de jouer jusqu'à 5 Joueurs au Jeu du Juste Prix.")
            print("La Séléction du nombre de joueurs se fera juste après celle du niveau pour que tous les joueurs aient la même difficulté.")
            print("Cette Séléction se déroule de la même façon que celle du niveau.")
            print("Si le nombre de joueurs est invalide deux fois de suite, le nombre de joueurs sera de 1.")
            print("Si le nombre de joueurs est égal à 1, alors le mode sera le Mode Solo.")
            print(" ")
            print("BON JEU")
        if action=='lang':
            print("SÉLECTIONNER LE LANGAGE / SELECT LANGUAGE")
            print("fr - Français")
            print("en - English")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            if lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            if lang!='fr' and lang!='Fr' and lang!='FR' and lang!='French' and lang!='Français' and lang!='Francais' and lang!='french' and lang!='français' and lang!='francais' and lang!='en' and lang!='En' and lang!='EN' and lang!='English' and lang!='Anglais' and lang!='english' and lang!='anglais' and lang!='E' and lang!='e' and lang!='F' and lang!='f':
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Français")
                print("DEFAULT LANGUAGE: French")
                lang='fr'

        if action=='exit':
            jeu=0
            print("Fin du Jeu")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                jeu=0

    # FRANCAIS #















    # ENGLISH #
    if lang=='en':
        print("-----------------")
        print("MENU 🌐")
        print("play - Start a Game")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Show Game Rules")
        print("lang - Change Language")
        print("exit - Leave the Game")
        print("-----------------")

        action=str(input("Select an Option :  : "))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Invalid Option : Try Again.")
            action=str(input("Select an Option : "))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Invalid Option.")
                jeu=0
                print("Game Over")
                exit()
        print("OPTION SELECTED :", action)
        print("-----------------")

        if action=='play': 
            print("SELECT LEVEL")
            print("1- Easy [1-100]")
            print("2- Medium [1-1000]")
            print("3- Hard [1-10000]")
            print("4- Very Hard [1-100000]")
            print("5- Extreme [1-1000000]")
            print("x- Personalized [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Level="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('The Level ""',levelfloat,'""','was Rounded to Level','""',levelint,'"".')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Invalid Level : Try Again.")
                    levelfloat=float(input("Level="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print("The Level"" ",levelfloat, '""', "was Rounded to Level",'""',levelint, '"".')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Invalid Level")
                      levelint=1
                      print("DEFAULT LEVEL : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("SELECT NUMBER OF PLAYERS")
            print("1 to 5 Players")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Players=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Number of Players"',joueurfloat,'" was Rounded to "',joueurint,'".')
                if joueurint<1 or joueurint>5:
                    print("Invalid Number of Players : Try Again.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Players=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Number of Players "',joueurfloat,'" was Rounded to "',joueurint,'".')
                    if joueurint<1 or joueurint>5:
                      print("Invalid Number of Players.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("FEFAULT PLAYERS : 1") 
            print("-----------------")

            tour=0
            essaisj1=0
            essaisj2=0
            essaisj3=0
            essaisj4=0
            essaisj5=0
            for parties in range(joueurint):
                nombre=0
                tour=tour+1
                if tour>1:
                    print("-----------------")
                if joueurint>1:
                    print("🎮 PLAYER", tour, "🎮")
                if levelint==1:
                    print("LEVEL",levelint," - Easy [1-100]")
                if levelint==2:
                    print("LEVEL",levelint," - Medium [1-1000]")
                if levelint==3:
                      print("LEVEL",levelint," - Hard [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("LEVEL",levelint," - Very Hard [1-100000]")
                if levelint==5:
                     print("LEVEL",levelint," - Extreme [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("LEVEL",levelint," - Personalized [1-", (1*(10**(levelint+1))),"]")

                essais=0
                os.system('cls' if os.name == 'nt' else 'clear')   
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Number="))
                     if nombre<tresor:
                         print("More")
                     if nombre>tresor:
                         print("Less")
                     essais=essais+1
                print("Well Done, The Answer was", tresor)
                if tour<joueurint:                                                                              
                    tresor=random.randint(1, (1*(10**(levelint+1)))   )                                         # PARAGRAPHE JEU
                if tour==1:
                    essaisj1=essais
                if tour==2:
                    essaisj2=essais
                if tour==3:
                    essaisj3=essais
                if tour==4:
                    essaisj4=essais
                if tour==5:
                    essaisj5=essais
            if joueurint>1:
                print("-----------------")

            if joueurint>1:
                print("RESULTS 🏅")
                if joueurint>=2:
                    print("Player 1 Trials :", essaisj1)
                    print("Player 2 Trials :", essaisj2)
                if joueurint>=3:
                    print("Player 3 Trials :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Player 4 Trials :", essaisj4)
                if joueurint>=5:
                    print("Player 5 Trials :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Number of Tries :", essaisj1)
        if action=='rules':
            print("RULES")
            print(" ")
            print('In the Juste Prix Game, the Goal is to find an hidden Random Value Called "Treasure".')
            print("This value is an integer and is chosen randomly from a Level-Dependent set.")
            print("In Level 1 (Easy), the number will be between 1 and 100 inclusive. The higher the level, the higher the range.")
            print("The levels range from 1 to 1000. The first are Easy, Medium, Hard, Very Hard and Extreme.")
            print("Beyond Level 5, the levels are personalized up to 1000 included. The difficulty increases more and more.")
            print("Each level starts at 1 and ends at (1(10**(x+1))), where x is the level. For example level 1 will be up to 1*10² = 100.")
            print("A decimal level (With Comma), will be automatically rounded to the unit and a conversion message will be displayed to the Player.")
            print("If the level is invalid (Less than 1 or Greater than 1000), an invalid message will be displayed.")
            print("If the level is still invalid after a second try, the default Level will be Level 1- Easy (1-100).")
            print("Once the level has been chosen and the Treasure assigned, the player must send a number to the Game.")
            print('The Game will respond only with "More" or "Less". The Player will therefore have to send a Greater or Lesser number.')
            print("Once the Treasure has been found, the Game will send a message confirming the correct result and the number of tries.")
            print("MULTIPLAYER MODE: It is possible to play up to 5 Players in the Juste Prix Game.")
            print("The selection of the number of players will be done just after that of the level so that all players have the same difficulty.")
            print("This Selection takes place in the same way as that of the level.")
            print("If the number of players is invalid twice in a row, the number of players will be 1.")
            print("If the number of players is equal to 1, then the mode will be Solo Mode.")
            print(" ")
            print("GOOD GAME")
        if action=='lang':
            print("SELECT LANGUAGE")
            print("fr - Français")
            print("en - English")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            if lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            if lang!='fr' and lang!='Fr' and lang!='FR' and lang!='French' and lang!='Français' and lang!='Francais' and lang!='french' and lang!='français' and lang!='francais' and lang!='en' and lang!='En' and lang!='EN' and lang!='English' and lang!='Anglais' and lang!='english' and lang!='anglais' and lang!='E' and lang!='e' and lang!='F' and lang!='f':
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Anglais")
                print("DEFAULT LANGUAGE: English")
                lang='en'

        if action=='exit':
            jeu=0
            print("Game Over")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                jeu=0

    # ENGLISH #


if lang=='fr':
    print("Fin du Jeu")
if lang=='en':
    print("Game Over")