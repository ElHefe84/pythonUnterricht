# variable
print("Variablen")
variable = 0
variable = variable + 2

print(variable)

variable -= 2

print(variable)

variable = str(variable)
print(variable)

# wirft Fehler da jetzt ein String
# variable += 2

variable = variable + " Hallo"
print(variable)


# list
print("Listen")
liste = [variable, 1, 'a', 0.2]
for element in liste:
    print(type(element))

# tuple
print("Tupel")
tupel = (variable, 1, 'y', 0.2)
for element in tupel:
    print(element)

# set
print("Mengen")
menge_a = set(liste)
menge_b = {0, 3, 4, variable}
for element in menge_a:
    print(element)

menge_a.union(menge_b)

# dictionary
print("Dictionary")
dictionary = {'a': 0, 'b': 1, 'c': variable}
for element in dictionary.keys():
    print(element)
for element in dictionary.values():
    print(element)
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")
for item in dictionary.items():
    print(item)

namensliste = ['Peter', 'Klaus', 'Hans', 'Heinz']
for name in namensliste:
    print(name)

name = namensliste[1]
print(name)

namensliste[1] = 'Tobias'
print(namensliste)

namensliste.append('Adam')
namensliste.insert(1, 'Dieter')
print(namensliste)

aElement = dictionary['a']
dictionary['a'] = 5
dictionary['d'] = 4

print(dictionary)

boolean1 = True
boolean2 = False

boolean3 = boolean1 and boolean2
boolean4 = boolean1 or boolean2
boolean5 = not boolean1
boolean6 = boolean1 != boolean2

zahl1 = 0
zahl2 = 2
boolean7 = zahl1 == zahl2 # < <= > >=
boolean8 = zahl1 != zahl2

if zahl1 != zahl2:
    print("Zahlen sind ungleich")
    # ...
else:
    print("Zahlen sind gleich")

if zahl1 == 2:
    print("Zahl == 2")
elif zahl1 == 0:
    print("Zahl == 0")
else:
    print("Zahl ist anders")

while zahl1 != zahl2:
    print("Test")
    zahl1 += 1

for element in liste:
    print(element)

for i in range(10):
    print(i)
