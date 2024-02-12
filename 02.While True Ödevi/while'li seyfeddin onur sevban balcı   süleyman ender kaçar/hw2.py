sayı1 = 60 
devam=input('Devam etmek için (d) basın\n')
while sayı1 != 30 :
    print(sayı1 -1)
    sayı1 -=1
    devam=input('Devam etmek için (d) basın\n')
    if sayı1 == 30:
        print('Uyglamadan çıkıldı')