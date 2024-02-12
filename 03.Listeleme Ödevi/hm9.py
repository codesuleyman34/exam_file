liste = [35, 26, 81, 64]
liste1 = liste.copy()
liste.sort()
liste.reverse()
print(liste)

liste1.reverse()
print(liste1)

a = liste1.count(21)
print(a)

liste1.remove(81)
print(liste1)

liste1.clear()
print(liste1)

liste = [35, 26, 81, 64]
print(liste.index(64))


liste = [35, 26, 81, 64]
liste.append(1.4)
liste.append(6.8)
print(liste)