ürün1_fiyat = int(input("1. ürünün fiyatını girin: \n"))

ürün2_fiyat = int(input("2. ürünün fiyatını girin: \n"))

toplam = ürün1_fiyat + ürün2_fiyat

if toplam <= 200:
    print("Ücret: ",toplam)

elif toplam > 200:
    print("Ücret: ",toplam / 4)