ifade = input("Bir ifade giriniz: ") 
harf = input("Aranacak harf giriniz: ") 
sayac = 0 
for karakter in ifade: 
    if karakter == harf: 
        sayac = sayac + 1 
print(f"Girilen ifadede {sayac} tane {harf} harfi vardır.")