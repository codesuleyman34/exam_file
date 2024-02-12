sayı1 = 1
devam=input('Devam etmek için (d) basın\n')
while sayı1 != 29 :
    print(sayı1 +2)
    sayı1 +=2
    devam=input('Devam etmek için (d) basın\n')
    if sayı1 == 29:
        print('Uyglamadan çıkıldı')