from random import randint


def Generator(länge, ug, og):
    liste = []
    for i in range(länge):
        liste.append(randint(ug, og))
    return liste


zufallsliste = Generator(5, 1, 1000)
print(zufallsliste)

for element in zufallsliste:
    print(element)


def Zahlenvergleich(ug, og):
    gesuchtezahl = randint(ug, og)
    i = 0

    while i != gesuchtezahl:
        i += 1
    print(f'Die gesuchte Zahl lautet {i}')


Zahlenvergleich(0, 1000000)

def GeneriereZahl():
    ug = int(input("Gib die untere Grenze der Zahl ein."))
    og = int(input("Gib die obere Grenze der Zahl ein."))
    gesuchtezahl = randint(ug, og)
    return gesuchtezahl, ug, og

gesuchtezahl, ug, og = GeneriereZahl()
print(gesuchtezahl)


def Zahlenvergleich2():
    eingabe = int(input(f'Gib eine Zahl zwischen {ug} und {og} ein!'))
    if eingabe == gesuchtezahl:
        print(f'Du hast richtig geraten. Die Zahl war {gesuchtezahl}')
    else:
        print('Du hast leider falsch geraten. Versuch es nochmal')
        Zahlenvergleich2()


def Zahlenvergleich3():
    eingabe = int(input(f'Gib eine Zahl zwischen {ug} und {og} ein!'))
    while eingabe != gesuchtezahl:
        print('Deine Eingabe war leider falsch. Probiere es erneut')
        eingabe = int(input(f'Gib eine Zahl zwischen {ug} und {og} ein!'))
    print(f'Glückwunsch die gesuchte Zahl war {eingabe}')


Zahlenvergleich3()
