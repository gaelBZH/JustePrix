import random

print("Bienvenue dans le Jeu du Juste Prix")
print("-----------------")
print("SÉLECTIONNER LE NIVEAU")
print("1- Facile [1-100]")
print("2- Moyen [1-1000]")
print("3- Difficile [1-10000]")
print("4- Très Difficile [1-100000]")
print("5- Extrême [1-1000000]")
print("-----------------")

level=int(input("Niveau="))
if level==1:
    tresor=random.randint(1,100)
if level==2:
    tresor=random.randint(1, 1000)
if level==3:
    tresor=random.randint(1,10000)
if level==4:
    tresor=random.randint(1,100000)
if level==5:
    tresor=random.randint(1,1000000)
if level!=1 and level !=2 and level!=3 and level!=4 and level!=5:
    print("Niveau Invalide")
    tresor=random.randint(1, 100)
    print("NIVEAU PAR DÉFAUT : 1")
    level=1
print("-----------------")
nombre=0
if level==1:
    print("NIVEAU",level," - Facile [1-100]")
if level==2:
    print("NIVEAU",level," - Moyen [1-1000]")
if level==3:
    print("NIVEAU",level," - Difficile [1-10000]")
if level==4:
    print("NIVEAU",level," - Très Difficile [1-100000]")
if level==5:
    print("NIVEAU",level," - Extrême [1-1000000]")
while tresor!=nombre:
    nombre=int(input("Nombre="))
    if nombre<tresor:
        print("Plus")
    if nombre>tresor:
        print("Moins")
print("Bravo, la Réponse Était Bien", tresor)