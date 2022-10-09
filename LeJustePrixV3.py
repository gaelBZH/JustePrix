import random        # Modules : Random        # Variables :   levelfloat ; levelint ; tresor ; nombre

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
# Une fois le Trésor trouvé, le Jeu enverra un message lui confirmant le bon résultat.

# BON JEU #

print("Bienvenue dans le Jeu du Juste Prix")
print("-----------------")
print("SÉLECTIONNER LE NIVEAU")
print("1- Facile [1-100]")
print("2- Moyen [1-1000]")                                                                             # PARAGRAPHE INTRODUCTION
print("3- Difficile [1-10000]")
print("4- Très Difficile [1-100000]")
print("5- Extrême [1-1000000]")
print("x- Personalisé [1-1000000+]")
print("-----------------")  # Issue

levelint=0
while levelint<1:
    levelfloat=float(input("Niveau="))
    levelint=round(levelfloat)
    if levelfloat!=levelint and levelint<=1000:
        print('Le Niveau ""',levelfloat,'""','a été arrondi au Niveau','""',levelint,'"".')
    if levelint>=1:
        tresor=random.randint(1, (1*(10**(levelint+1)))   )        # -> Issue Paragraphe Suivant
    if levelint<1 or levelint>1000:
        print("Niveau Invalide : Veuillez réessayer.")                                                 # PARAGRAPHE LEVEL
        levelfloat=float(input("Niveau="))
        levelint=round(levelfloat)
        if levelfloat!=levelint and levelint<=1000:
            print(" Le Niveau"" ",levelfloat, '""', "a été arrondi au Niveau",'""',levelint, '""')
        if levelint>=1:
            tresor=random.randint(1, (1*(10**(levelint+1)))   )    # -> Issue Paragraphe Suivant
        if levelint<1 or levelint>1000:
          print("Niveau Invalide")
          levelint=1
          print("NIVEAU PAR DÉFAUT : 1")
          tresor=random.randint(1, 100)                            # -> Issue Paragraphe Suivant

print("-----------------")
nombre=0
if levelint==1:
    print("NIVEAU",levelint," - Facile [1-100]")
if levelint==2:
    print("NIVEAU",levelint," - Moyen [1-1000]")
if levelint==3:
      print("NIVEAU",levelint," - Difficile [1-10000]")                                                # PARAGRAPHE START
if levelint==4:
      print("NIVEAU",levelint," - Très Difficile [1-100000]")
if levelint==5:
     print("NIVEAU",levelint," - Extrême [1-1000000]")
if levelint!=1 and levelint !=2 and levelint!=3 and levelint!=4 and levelint!=5:      # Issue If/Else
     print("NIVEAU",levelint," - Personalisé [1-", (1*(10**(levelint+1))),"]")

while tresor!=nombre:   # While = Issue
     nombre=int(input("Nombre="))
     if nombre<tresor:
         print("Plus")                                                                                 # PARAGRAPHE JEU
     if nombre>tresor:
          print("Moins")

print("Bravo, la Réponse Était Bien", tresor)                                                          # PARAGRAPHE FIN