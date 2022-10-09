import random       # Variables :   levelfloat ; levelint ; joueurfloat ; joueurint ; tour ; essais ; essaisj1 ; essaisj2 ; essaisj3 ; essaisj4 ; essaisj5 ; parties ; tresor ; nombre ; action ; choixFinDePartie
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
jeu=1 # Activé par défaut
print("-----------------")
print("Bienvenue dans le Jeu du Juste Prix 🎰")
while jeu==1: # Jeu==0 : Fin   Jeu==1 : En Route
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
        print("Au delà du Niveau 5, les niveaux sont personalisés jusqu'à 1000 inclus. La difficulté augmente de plus en plus.")
        print("Chaque niveau démarre de 1 et s'achève à (1(10**(x+1))), où x est le niveau. Par exemple le niveau 1 sera jusqu'à 1*10² = 100.")
        print("Un niveau décimal (Avec Virgule), sera automatiquement arrondi à l'unité et un message de convertion s'affichera au Joueur.")
        print("Si le niveau est invalide (Inférieur à 1 ou Supérieur à 1000), un message d'invalidité s'affichera.")
        print("Si le niveau est encore invalide après un deuxième essai, le Niveau par défaut sera le Niveau 1- Facile (1-100).")
        print("Une fois le niveau chosi et le Trésor attribué, le joueur doit envoyer un nombre au Jeu.")
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
        print("LA FONCTION LANGUAGE N'EST PAS DISPONIBLE")
    if action=='exit':
        jeu=0
        print("Fin du Jeu")
        exit()
    print("-----------------")
    choixFinDePartie=str(input("Retourner au Menu ? [Oui/Non] : "))
    if choixFinDePartie=='OUI' or choixFinDePartie=='O' or choixFinDePartie=='Oui' or choixFinDePartie=='oui' or choixFinDePartie=='o':
        jeu=1
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        jeu=0
print("Fin du Jeu")