import random 
sayi = random.randint(0, 20) 
tahmin = -1 
while tahmin != sayi: 
    tahmin = int(input("Bir sayı tahmin ediniz: ")) 
    if tahmin < sayi: 
        print("Daha büyük bir sayı giriniz.") 
    elif tahmin > sayi: 
        print("Daha küçük bir sayı giriniz.") 
print("Tebrikler! Doğru sayıyı buldunuz.")