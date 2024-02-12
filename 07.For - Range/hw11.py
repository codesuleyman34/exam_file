import random 
sayilar = [] 
while len(sayilar) < 6:
    sayi = random.randint(1, 100) 
    if sayi not in sayilar: 
        sayilar.append(sayi) 
print(sayilar) 