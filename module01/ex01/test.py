from game import GotCharacter, Stark, Lannister, Targaryen


# Création des personnages Stark
arya = Stark("Arya")
ned = Stark("Ned", False)


# Création des personnages Lannister
jaime = Lannister("Jaime")
cersei = Lannister("Cersei")


# Création des personnages Targaryen
daenerys = Targaryen("Daenerys")
viserys = Targaryen("Viserys", False)


# Stockage dans une liste pour tester de manière générique
characters = [
    arya,
    ned,
    jaime,
    cersei,
    daenerys,
    viserys
]


# Affichage des informations de chaque personnage
for character in characters:
    print("--------------------")
    print(f"Name: {character.first_name}")
    print(f"House: {character.family_name}")
    print(f"House words: {character.house_words}")
    print(f"Alive: {character.is_alive}")


# Vérifications de type (héritage)
print("--------------------")
print("Inheritance tests:")

print(f"Arya is Stark: {isinstance(arya, Stark)}")
print(f"Arya is GotCharacter: {isinstance(arya, GotCharacter)}")

print(f"Jaime is Lannister: {isinstance(jaime, Lannister)}")
print(f"Daenerys is Targaryen: {isinstance(daenerys, Targaryen)}")

# Vérification négative
print(f"Arya is Lannister: {isinstance(arya, Lannister)}")
print ("---------42AI SUBJECT TESTS----------")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__init__.__doc__)
print(daenerys.__doc__)