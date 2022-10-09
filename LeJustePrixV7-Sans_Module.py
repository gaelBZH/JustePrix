import random       # Variables :   levelfloat ; levelint ; joueurfloat ; joueurint ; tour ; essais ; essaisj1 ; essaisj2 ; essaisj3 ; essaisj4 ; essaisj5 ; parties ; tresor ; nombre ; action ; choixFinDePartie ; lang
                    # Modules : Random

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
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
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
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
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

        action=str(input("Select an Option : "))
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
                      print("DEFAULT PLAYERS : 1") 
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
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
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
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
            else:
                jeu=0


    # ENGLISH #













    # DEUTSCH #
    if lang=='de':
        print("-----------------")
        print("MENÜ 🌐")
        print("play - Starten Sie ein Spiel")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Spielregeln Anzeigen")
        print("lang - Sprache Ändern")
        print("exit - Spiel Verlassen")
        print("-----------------")

        action=str(input("Wähle eine Option : "))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Ungültige Option : Versuchen Sie es erneut.")
            action=str(input("Wähle eine Option : "))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Ungültige Option.")
                jeu=0
                print("Ende des Spiels")
                exit()
        print("AUSGEWÄHLTE OPTION :", action)
        print("-----------------")

        if action=='play': 
            print("STUFE AUSWÄHLEN")
            print("1- Leicht [1-100]")
            print("2- Mittel [1-1000]")
            print("3- Schwer [1-10000]")
            print("4- Sehr Schwer [1-100000]")
            print("5- Extrem [1-1000000]")
            print("x- Personalisiert [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Stufe="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('Die Stufe""',levelfloat,'""','wurde auf Stufe','""',levelint,'""gerundet.')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Ungültiges Stufe : Versuchen Sie es erneut.")
                    levelfloat=float(input("Stufe="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print("Die Stufe"" ",levelfloat, '""', "wurde auf Stufe",'""',levelint, '""gerundet.')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Ungültiges Stufe.")
                      levelint=1
                      print("STANDARD EBENE : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("SPIELERZAHL AUSWÄHLEN")
            print("1 bis 5 Spieler")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Spieler=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Anzahl der Spieler"',joueurfloat,'" wurde "',joueurint,'"gerundet.')
                if joueurint<1 or joueurint>5:
                    print("Ungültige Spieleranzahl : Versuchen Sie es erneut.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Spieler=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Anzahl der Spieler"',joueurfloat,'" wurde "',joueurint,'"gerundet.')
                    if joueurint<1 or joueurint>5:
                      print("Ungültige Spieleranzahl.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("STANDARDSPIELER : 1") 
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
                    print("🎮 SPIELER", tour, "🎮")
                if levelint==1:
                    print("STUFE",levelint," - Leicht [1-100]")
                if levelint==2:
                    print("STUFE",levelint," - Mittel [1-1000]")
                if levelint==3:
                      print("STUFE",levelint," - Schwer [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("STUFE",levelint," - Sehr Schwer [1-100000]")
                if levelint==5:
                     print("STUFE",levelint," - Extrem [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("STUFE",levelint," - Personalisiert [1-", (1*(10**(levelint+1))),"]")

                essais=0 
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Anzahl="))
                     if nombre<tresor:
                         print("Mehr")
                     if nombre>tresor:
                         print("Weniger")
                     essais=essais+1
                print("Gut gemacht, Die Antwort war", tresor)
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
                print("ERGEBNISSE 🏅")
                if joueurint>=2:
                    print("Prüfungen Spieler 1 :", essaisj1)
                    print("Prüfungen Spieler 2 :", essaisj2)
                if joueurint>=3:
                    print("Prüfungen Spieler 3 :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Prüfungen Spieler 4 :", essaisj4)
                if joueurint>=5:
                    print("Prüfungen Spieler 5 :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Anzahl der Versuche :", essaisj1)
        if action=='rules':
            print("REGELN")
            print(" ")
            print('Im Juste-Prix-Spiel besteht das Ziel darin, einen versteckten Zufallswert namens "Schatz" zu finden.')
            print("Dieser Wert ist eine Ganzzahl und wird zufällig aus einem stufenabhängigen Satz ausgewählt.")
            print("In Stufe 1 (Leicht) liegt die Zahl zwischen 1 und 100 einschließlich. Je höher die Stufe, desto höher die Reichweite.")
            print("Die Stufen reichen von 1 bis 1000. Die ersten sind Leicht, Mittel, Schwer, Sehr Schwer und Extrem.")
            print("Über Level 5 hinaus sind die Levels bis zu 1000 inklusive personalisiert. Die Schwierigkeit steigt immer mehr.")
            print("Jede Stufe beginnt bei 1 und endet bei (1(10**(x+1))), wobei x die Stufe ist. Zum Beispiel ist Level 1 bis zu 1*10² = 100.")
            print("Ein Dezimalwert (mit Komma) wird automatisch auf die Einheit gerundet und eine Umrechnungsmeldung wird dem Player angezeigt.")
            print("Wenn die Ebene ungültig ist (weniger als 1 oder größer als 1000), wird eine ungültige Meldung angezeigt.")
            print("Wenn die Stufe nach einem zweiten Versuch immer noch ungültig ist, ist die Standardstufe Stufe 1 – Leicht (1–100).")
            print("Sobald das Level ausgewählt und der Schatz zugewiesen wurde, muss der Spieler eine Nummer an das Spiel senden.")
            print('Das Spiel antwortet nur mit "Mehr" oder "Weniger". Der Spieler muss daher eine größere oder kleinere Zahl senden.')
            print("Sobald der Schatz gefunden wurde, sendet das Spiel eine Nachricht, die das korrekte Ergebnis und die Anzahl der Versuche bestätigt.")
            print("MEHRSPIELERMODUS: Im Juste-Prix-Spiel können bis zu 5 Spieler spielen.")
            print("Die Auswahl der Spieleranzahl erfolgt unmittelbar nach der Levelauswahl, damit alle Spieler den gleichen Schwierigkeitsgrad haben.")
            print("Diese Auswahl erfolgt auf die gleiche Weise wie die der Ebene.")
            print("Wenn die Spieleranzahl zweimal hintereinander ungültig ist, ist die Spieleranzahl 1.")
            print("Wenn die Anzahl der Spieler gleich 1 ist, ist der Modus der Solo-Modus.")
            print(" ")
            print("GUTE PARTIE")
        if action=='lang':
            print("SELECT LANGUAGE")
            print("fr - Français")
            print("en - English")
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Allemand")
                print("DEFAULT LANGUAGE: German")
                lang='de'

        if action=='exit':
            jeu=0
            print("Game Over")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
            else:
                jeu=0

    # DEUTSCH #













    # ESPAÑOL #
    if lang=='es':
        print("-----------------")
        print("MENÚ 🌐")
        print("play - Iniciar un Juego")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Mostrar Reglas del Juego")
        print("lang - Cambiar Idioma")
        print("exit - Abandonar el Juego")
        print("-----------------")

        action=str(input("Seleccione una Opción : "))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Opción no válida : Inténtalo de Nuevo.")
            action=str(input("Seleccione una Opción :"))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Opción inválida.")
                jeu=0
                print("Juego Terminado")
                exit()
        print("OPCIÓN SELECCIONADA :", action)
        print("-----------------")

        if action=='play': 
            print("SELECCIONA EL NIVEL")
            print("1- Fácil [1-100]")
            print("2- Medio [1-1000]")
            print("3- Duro [1-10000]")
            print("4- Muy Duro [1-100000]")
            print("5- Extremo [1-1000000]")
            print("x- Personalizado [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Nivel="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('El Nivel ""',levelfloat,'""','fue redondeado al Nivel','""',levelint,'"".')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Nivel no Válido : Inténtalo de Nuevo.")
                    levelfloat=float(input("Nivel="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print('El Nivel ""',levelfloat,'""','fue redondeado al Nivel','""',levelint,'"".')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Nivel no Válido")
                      levelint=1
                      print("NIVEL PREDETERMINADO : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("SELECCIONA NÚMERO DE JUGADORES")
            print("1 a 5 Jugadores")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Jugadores=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Numero de Jugadores"',joueurfloat,'" Fue redondeado a "',joueurint,'".')
                if joueurint<1 or joueurint>5:
                    print("Número Inválido de Jugadores: Inténtalo de Nuevo.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Jugadores=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Numero de Jugadores"',joueurfloat,'" Fue redondeado a "',joueurint,'".')
                    if joueurint<1 or joueurint>5:
                      print("Número Inválido de Jugadores.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("JUGADORES POR DEFECTO : 1") 
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
                    print("🎮 JUGADOR", tour, "🎮")
                if levelint==1:
                    print("NIVEL",levelint," - Fácil [1-100]")
                if levelint==2:
                    print("NIVEL",levelint," - Medio [1-1000]")
                if levelint==3:
                      print("NIVEL",levelint," - Duro [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("NIVEL",levelint," - Muy Duro [1-100000]")
                if levelint==5:
                     print("NIVEL",levelint," - Extremo [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("NIVEL",levelint," - Personalizado [1-", (1*(10**(levelint+1))),"]")

                essais=0
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Número="))
                     if nombre<tresor:
                         print("Más")
                     if nombre>tresor:
                         print("Menos")
                     essais=essais+1
                print("Bien hecho, la respuesta fue", tresor)
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
                print("RESULTADOS 🏅")
                if joueurint>=2:
                    print("Pruebas del Jugador 1 :", essaisj1)
                    print("Pruebas del Jugador 2 :", essaisj2)
                if joueurint>=3:
                    print("Pruebas del Jugador 3 :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Pruebas del Jugador 4 :", essaisj4)
                if joueurint>=5:
                    print("Pruebas del Jugador 5 :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Número de Intentos :", essaisj1)
        if action=='rules':
            print("NORMAS")
            print(" ")
            print('En el juego Juste Prix, el objetivo es encontrar un valor aleatorio oculto llamado "Tesoro".')
            print("Este valor es un número entero y se elige aleatoriamente de un conjunto dependiente del nivel.")
            print("En el Nivel 1 (Fácil), el número estará entre 1 y 100 inclusive. Cuanto mayor sea el nivel, mayor será el rango.")
            print("Los niveles van del 1 al 1000. Los primeros son Fácil, Medio, Difícil, Muy Difícil y Extremo.")
            print("Más allá del Nivel 5, los niveles se personalizan hasta 1000 incluidos. La dificultad aumenta cada vez más.")
            print("Cada nivel comienza en 1 y termina en (1(10**(x+1))), donde x es el nivel. Por ejemplo, el Nivel 1 será hasta 1*10² = 100.")
            print("Un nivel decimal (con coma), se redondeará automáticamente a la unidad y se mostrará un mensaje de conversión al jugador.")
            print("Si el nivel no es válido (menor que 1 o mayor que 1000), se mostrará un mensaje de invalidez.")
            print("Si el nivel sigue siendo inválido después de un segundo intento, el nivel predeterminado será el Nivel 1 : Fácil (1-100).")
            print("Una vez elegido el nivel y asignado el Tesoro, el jugador deberá enviar un número al Juego.")
            print('El Juego responderá solo con "Más" o "Menos". Por lo tanto, el jugador deberá enviar un número mayor o menor.')
            print("Una vez encontrado el Tesoro, el Juego enviará un mensaje confirmando el resultado correcto y el número de intentos.")
            print("MODO MULTIJUGADOR: Es posible jugar hasta 5 jugadores en el juego Juste Prix.")
            print("La selección del número de jugadores se hará justo después de la del nivel para que todos los jugadores tengan la misma dificultad.")
            print("Esta Selección se realiza de la misma forma que la del nivel.")
            print("Si el número de jugadores no es válido dos veces seguidas, el número de jugadores será 1.")
            print("Si el número de jugadores es igual a 1, entonces el modo será Modo Solo.")
            print(" ")
            print("BUEN JUEGO")
        if action=='lang':
            print("SELECCIONE EL IDIOMA")
            print("fr - Français")
            print("en - English")
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lengua="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Espagnol")
                print("DEFAULT LANGUAGE: Spanish")
                lang='es'

        if action=='exit':
            jeu=0
            print("Juego Terminado")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
            else:
                jeu=0


    # ESPAÑOL #















    # ITALIANO #
    if lang=='it':
        print("-----------------")
        print("MENÙ 🌐")
        print("play - Inizia un Gioco")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Mostra le Regole del Gioco")
        print("lang - Cambia Lingua")
        print("exit - Lascia il Gioco")
        print("-----------------")

        action=str(input("Seleziona Un'opzione : "))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Opzione Non Valida : Riprova.")
            action=str(input("Seleziona Un'opzione : "))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Opzione Non Valida.")
                jeu=0
                print("Fine del Gioco")
                exit()
        print("OPZIONE SELEZIONATA :", action)
        print("-----------------")

        if action=='play': 
            print("SELEZIONA LIVELLO")
            print("1- Facile [1-100]")
            print("2- Medio [1-1000]")
            print("3- Difficile [1-10000]")
            print("4- Molto Difficile [1-100000]")
            print("5- Estremo [1-1000000]")
            print("x- Personalizzato [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Livello="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('Il Livello ""',levelfloat,'""','è stato arrotondato al livello','""',levelint,'"".')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Livello Non Valido : Riprova.")
                    levelfloat=float(input("Level="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print('Il Livello ""',levelfloat,'""','è stato arrotondato al livello','""',levelint,'"".')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Livello Non Valido.")
                      levelint=1
                      print("LIVELLO PREDEFINITO : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("SELEZIONA NUMERO DI GIOCATORI")
            print("Da 1 a 5 Giocatori")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Giocatori=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Numero di Giocatori"',joueurfloat,'" è stato arrotondato a "',joueurint,'".')
                if joueurint<1 or joueurint>5:
                    print("Numero di Giocatori Non Valido : Riprova.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Players=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Numero di Giocatori"',joueurfloat,'" è stato arrotondato a "',joueurint,'".')
                    if joueurint<1 or joueurint>5:
                      print("Numero di Giocatori Non Valido.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("GIOCATORI PREDEFINITI : 1") 
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
                    print("🎮 GIOCATORE", tour, "🎮")
                if levelint==1:
                    print("LIVELLO",levelint," - Facile [1-100]")
                if levelint==2:
                    print("LIVELLO",levelint," - Medio [1-1000]")
                if levelint==3:
                      print("LIVELLO",levelint," - Difficile [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("LIVELLO",levelint," - Molto Difficile [1-100000]")
                if levelint==5:
                     print("LIVELLO",levelint," - Estremo [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("LIVELLO",levelint," - Personalizzato [1-", (1*(10**(levelint+1))),"]")

                essais=0   
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Numero="))
                     if nombre<tresor:
                         print("Di Più")
                     if nombre>tresor:
                         print("Meno")
                     essais=essais+1
                print("Ben Fatto, la Risposta era", tresor)
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
                print("RISULTATI 🏅")
                if joueurint>=2:
                    print("Prove del Giocatore 1 :", essaisj1)
                    print("Prove del Giocatore 2 :", essaisj2)
                if joueurint>=3:
                    print("Prove del Giocatore 3 :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Prove del Giocatore 4 :", essaisj4)
                if joueurint>=5:
                    print("Prove del Giocatore 5 :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Numero di Tentativi:", essaisj1)
        if action=='rules':
            print("REGOLE")
            print(" ")
            print('Nel Juste Prix Game, l\'obiettivo è trovare un valore casuale nascosto chiamato "Treasure".')
            print("Questo valore è un numero intero e viene scelto casualmente da un insieme dipendente dal livello.")
            print("Nel Livello 1 (Facile), il numero sarà compreso tra 1 e 100 inclusi. Più alto è il livello, maggiore è l'intervallo.")
            print("I livelli vanno da 1 a 1000. I primi sono Facile, Medio, Difficile, Molto Difficile ed Estremo.")
            print("Oltre il livello 5, i livelli sono personalizzati fino a 1000 inclusi. La difficoltà aumenta sempre di più.")
            print("Ogni livello inizia a 1 e termina a (1(10**(x+1))), dove x è il livello. Ad esempio, il livello 1 sarà fino a 1*10² = 100.")
            print("Un livello decimale (Con Virgola), verrà automaticamente arrotondato all'unità e verrà visualizzato un messaggio di conversione al giocatore.")
            print("Se il livello non è valido (Inferiore a 1 o Maggiore di 1000), verrà visualizzato un messaggio non valido.")
            print("Se il livello non è ancora valido dopo un secondo tentativo, il livello predefinito sarà Livello 1- Facile (1-100).")
            print("Once the level has been chosen and the Treasure assigned, the player must send a number to the Game.")
            print('Il gioco risponderà solo con "Più" o "Meno". Il Giocatore dovrà quindi inviare un numero Maggiore o Minore.')
            print("Una volta trovato il Tesoro, il Gioco invierà un messaggio di conferma del risultato corretto e del numero di tentativi.")
            print("MODALITÀ MULTIGIOCATORE: è possibile giocare fino a 5 giocatori nel gioco Juste Prix.")
            print("La selezione del numero di giocatori verrà effettuata subito dopo quella del livello in modo che tutti i giocatori abbiano la stessa difficoltà.")
            print("Questa selezione avviene allo stesso modo di quella del livello.")
            print("Se il numero di giocatori non è valido due volte di seguito, il numero di giocatori sarà 1.")
            print("Se il numero di giocatori è uguale a 1, la modalità sarà Solo Mode.")
            print(" ")
            print("BEL GIOCO")
        if action=='lang':
            print("SELECT LANGUAGE")
            print("fr - Français")
            print("en - English")
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Italien")
                print("DEFAULT LANGUAGE: Italian")
                lang='it'

        if action=='exit':
            jeu=0
            print("Fine del Gioco")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
            else:
                jeu=0

    # ITALIANO #















    # Русский #
    if lang=='ru':
        print("-----------------")
        print("МЕНЮ 🌐")
        print("play - Начать игру")                                                             # PARAGRAPHE INTRODUCTION
        print("rules - Показать правила игры")
        print("lang - Изменить язык")
        print("exit - Выйти из игры")
        print("-----------------")

        action=str(input("Выберите вариант :"))
        if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
            action=str("play")
        if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
            action=str("rules")
        if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
            action=str("lang")
        if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':        # PARAGRAPHE ACTION
            action=str("exit")
        if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
            print("Неверный вариант: попробуйте еще раз.")
            action=str(input("Выберите вариант:"))
            if action=='play' or action=='p' or action=='start' or action=='démarrer' or action=='jouer' or action=='Play':
                action=str("play")
            if action=='rules' or action=='r' or action=='rule' or action=='règle' or action=='règles' or action=='Rules':
                action=str("rules")
            if action=='lang' or action=='l' or action=='language' or action=='languages' or action=='langage' or action=='langages' or action=='Lang':
                action=str("lang")
            if action=='exit' or action=='e' or action=='quitter' or action=='quitte' or action=='Exit':
                action=str("exit")
            if action!='play' and action!='p' and action!='start' and action!='démarrer' and action!='jouer' and action!='Play' and action!='rules' and action!='r' and action!='rule' and action!='règle' and action!='règles' and action!='Rules' and action!='lang' and action!='l' and action!='language' and action!='languages' and action!='langage' and action!='langages' and action!='Lang' and action!='exit' and action!='e' and action!='quitter' and action!='quitte' and action!='Exit':
                print("Неверный вариант.")
                jeu=0
                print("Игра завершена")
                exit()
        print("ВЫБРАН ВАРИАНТ:", action)
        print("-----------------")

        if action=='play': 
            print("ВЫБЕРИТЕ УРОВЕНЬ")
            print("1- Легко [1-100]")
            print("2- Середина [1-1000]")
            print("3- Жесткий [1-10000]")
            print("4- Очень тяжело [1-100000]")
            print("5- Экстрим [1-1000000]")
            print("x- Персонализированный [1-1000000+]")
            print("-----------------") # -> Issue Paragraphe Suivant
            levelint=0
            while levelint<1:
                levelfloat=float(input("Уровень="))
                levelint=round(levelfloat)
                if levelfloat!=levelint and levelint<=1000:
                    print('Уровень ""',levelfloat,'""','было округлено до уровня','""',levelint,'"".')          # PARAGRAPHE LEVEL
                if levelint>=1:
                    tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                if levelint<1 or levelint>1000:
                    print("Недопустимый уровень : попробуйте еще раз.")
                    levelfloat=float(input("Уровень="))
                    levelint=round(levelfloat)
                    if levelfloat!=levelint and levelint<=1000:
                        print('Уровень ""',levelfloat,'""','было округлено до уровня','""',levelint,'"".')
                    if levelint>=1:
                        tresor=random.randint(1, (1*(10**(levelint+1)))   ) # -> Issue Paragraphe Suivant
                    if levelint<1 or levelint>1000:
                      print("Недопустимый уровень")
                      levelint=1
                      print("УРОВЕНЬ ПО УМОЛЧАНИЮ : 1")
                      tresor=random.randint(1, 100) # -> Issue Paragraphe Suivant
            print("-----------------")

            joueurint=0
            print("ВЫБЕРИТЕ КОЛИЧЕСТВО ИГРОКОВ")
            print("от 1 до 5 игроков")
            while joueurint>5 or joueurint<1:
                joueurfloat=float(input("Игроки=")) # -> Issue Paragraphe Suivant
                joueurint=round(joueurfloat)
                if joueurint!=joueurfloat:
                    print('Количество игроков"',joueurfloat,'" был округлен до "',joueurint,'".')
                if joueurint<1 or joueurint>5:
                    print("Неверное количество игроков: попробуйте еще раз.")                                   # PARAGRAPHE JOUEURS             
                    joueurfloat=float(input("Players=")) # -> Issue Paragraphe Suivant
                    joueurint=round(joueurfloat)
                    if joueurfloat!=joueurint and joueurint<=5:
                        print('Количество игроков"',joueurfloat,'" был округлен до "',joueurint,'".')
                    if joueurint<1 or joueurint>5:
                      print("Неверное количество игроков.")
                      joueurint=1 # -> Issue Paragraphe Suivant
                      print("ИГРОКИ ПО УМОЛЧАНИЮ : 1") 
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
                    print("🎮 ИГРОК", tour, "🎮")
                if levelint==1:
                    print("УРОВЕНЬ",levelint," - Легко [1-100]")
                if levelint==2:
                    print("УРОВЕНЬ",levelint," - Середина [1-1000]")
                if levelint==3:
                      print("УРОВЕНЬ",levelint," - Жесткий [1-10000]")                                         # PARAGRAPHE START
                if levelint==4:
                      print("УРОВЕНЬ",levelint," - Очень тяжело [1-100000]")
                if levelint==5:
                     print("УРОВЕНЬ",levelint," - Экстрим [1-1000000]")
                if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5: # Issue If/Else
                     print("УРОВЕНЬ",levelint," - Персонализированный [1-", (1*(10**(levelint+1))),"]")

                essais=0   
                while tresor!=nombre:   # While = Issue
                     nombre=float(input("Количество="))
                     if nombre<tresor:
                         print("Более")
                     if nombre>tresor:
                         print("Меньше")
                     essais=essais+1
                print("Молодец, ответ был", tresor)
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
                print("ПОЛУЧЕННЫЕ РЕЗУЛЬТАТЫ 🏅")
                if joueurint>=2:
                    print("Испытания игрока 1 :", essaisj1)
                    print("Испытания игрока 2 :", essaisj2)
                if joueurint>=3:
                    print("Испытания игрока 3 :", essaisj3)                                                        # PARAGRAPHE RÉSULTATS
                if joueurint>=4:
                    print("Испытания игрока 4 :", essaisj4)
                if joueurint>=5:
                    print("Испытания игрока 5 :", essaisj5)
            if joueurint==1:
                print("-----------------")
                print("Количество попыток :", essaisj1)
        if action=='rules':
            print("ПРАВИЛА")
            print(" ")
            print('В игре Juste Prix цель состоит в том, чтобы найти скрытое случайное значение под названием "Сокровище".')
            print("Это значение является целым числом и выбирается случайным образом из набора, зависящего от уровня.")
            print("На уровне 1 (легкий) число будет от 1 до 100 включительно. Чем выше уровень, тем выше диапазон.")
            print("Уровни варьируются от 1 до 1000. Первые - это легкий, средний, сложный, очень сложный и экстремальный.")
            print("Помимо уровня 5, уровни персонализируются до 1000 включительно. Сложность возрастает все больше и больше.")
            print("Каждый уровень начинается с 1 и заканчивается на (1(10**(x+1))), где x — уровень. Например, уровень 1 будет до 1*10² = 100.")
            print("Десятичный уровень (с запятой) будет автоматически округлен до единицы, и игроку будет показано сообщение о преобразовании.")
            print("Если уровень недействителен (меньше 1 или больше 1000), будет отображаться недопустимое сообщение.")
            print("Если уровень по-прежнему недействителен после второй попытки, уровень по умолчанию будет Уровень 1-Легкий (1-100).")
            print("После того, как уровень выбран и сокровище назначено, игрок должен отправить номер в игру.")
            print('Игра ответит только «Больше» или «Меньше». Таким образом, Игрок должен будет отправить большее или меньшее число.')
            print("Как только Сокровище будет найдено, Игра отправит сообщение, подтверждающее правильный результат и количество попыток.")
            print("МНОГОПОЛЬЗОВАТЕЛЬСКИЙ РЕЖИМ: в Juste Prix Game могут играть до 5 игроков.")
            print("Выбор количества игроков будет сделан сразу после уровня, чтобы все игроки имели одинаковую сложность.")
            print("Этот Выбор происходит так же, как и на уровне.")
            print("Если число игроков неверно дважды подряд, количество игроков будет равно 1.")
            print("Если количество игроков равно 1, то режим будет Solo Mode.")
            print(" ")
            print("БОН ЖЕУ")
        if action=='lang':
            print("SELECT LANGUAGE")
            print("fr - Français")
            print("en - English")
            print("de - Deutsch")
            print("es - Español")
            print("it - Italiano")
            print("ru - Русский")
            lang=str(input("Lang="))
            if lang=='fr' or lang=='Fr' or lang=='FR' or lang=='French' or lang=='Français' or lang=='Francais' or lang=='french' or lang=='français' or lang=='francais' or lang=='f' or lang=='F':
                lang='fr'
            elif lang=='en' or lang=='En' or lang=='EN' or lang=='English' or lang=='Anglais' or lang=='english' or lang=='anglais' or lang=='e' or lang=='E':
                lang='en'
            elif lang=='de' or lang=='De' or lang=='DE' or lang=='Deutsch' or lang=='Allemand' or lang=='allemand' or lang=='German' or lang=='german' or lang=='ge' or lang=='d' or lang=='GE':
                lang='de'
            elif lang=='es' or lang=='Es' or lang=='ES' or lang=='Español' or lang=='Espagnol' or lang=='espagnol' or lang=='Spanish' or lang=='spanish' or lang=='sp' or lang=='s' or lang=='SP':
                lang='es'
            elif lang=='it' or lang=='It' or lang=='IT' or lang=='Italiano' or lang=='italiano' or lang=='italien' or lang=='Italian' or lang=='italian' or lang=='I' or lang=='i':
                lang='it'
            elif lang=='ru' or lang=='Ru' or lang=='RU' or lang=='Russian' or lang=='russian' or lang=='Русский' or lang=='русский' or lang=='р' or lang=='Р' or lang=='Ру' or lang=='ру' or lang=='r' or lang=='R':
                lang='ru'
            else:
                print("Langage Incorrect/Incorrect Language")
                print("LANGAGE PAR DÉFAUT : Russe")
                print("DEFAULT LANGUAGE: Russian")
                lang='ru'

        if action=='exit':
            jeu=0
            print("Игра завершена")
            exit()
        print("-----------------")

        if lang=='fr':
            choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
            if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
                jeu=1
            else:
                jeu=0
        if lang=='en':
            choixFinDePartie=str(input("Return to Menu ? [Yes/No] : "))
            if choixFinDePartie=='YES' or choixFinDePartie=='Y' or choixFinDePartie=='Yes' or choixFinDePartie=='yes' or choixFinDePartie=='y':
                jeu=1
            else:
                jeu=0
        if lang=='de':
            choixFinDePartie=str(input("Zurück zum Menü ? [Ja/Nein] : "))
            if choixFinDePartie=='JA' or choixFinDePartie=='J' or choixFinDePartie=='Ja' or choixFinDePartie=='ja' or choixFinDePartie=='j':
                jeu=1
            else:
                jeu=0
        if lang=='es':
            choixFinDePartie=str(input("¿ Volver al Menú ? [Sí/No] : "))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='it':
            choixFinDePartie=str(input("Torna al menu ? [Sí/No]"))
            if choixFinDePartie=='SÍ' or choixFinDePartie=='S' or choixFinDePartie=='Sí' or choixFinDePartie=='si' or choixFinDePartie=='s' or choixFinDePartie=='SI' or choixFinDePartie=='Si' or choixFinDePartie=='si':
                jeu=1
            else:
                jeu=0
        if lang=='ru':
            choixFinDePartie=str(input("Вернуться в меню? [Да/нет]"))
            if choixFinDePartie=='Да' or choixFinDePartie=='Д' or choixFinDePartie=='ДА' or choixFinDePartie=='да' or choixFinDePartie=='d' or choixFinDePartie=='D' or choixFinDePartie=='da' or choixFinDePartie=='DA' or choixFinDePartie=='Da':
                jeu=1
            else:
                jeu=0


    # Русский #





if lang=='fr':
    print("Fin du Jeu")
if lang=='en':
    print("Game Over")
if lang=='de':
    print("Ende des Spiels")
if lang=='es':
    print("Juego Terminado")
if lang=='it':
    print("Fine del Gioco")
if lang=='ru':
    print("Игра завершена")

