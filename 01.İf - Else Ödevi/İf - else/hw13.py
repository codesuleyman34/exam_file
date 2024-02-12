maas =int(input('İyi günler. Lütfen maşınız giriniz . \n'))
kac_çaliştim = int(input('kaç yıl çalıştınız . \n'))

if kac_çaliştim> 0 and kac_çaliştim <  6:
    print ('Sayın',  'Çalışanımız ','Zamlı maaşınız : ', (maas/10)+maas)
elif kac_çaliştim > 5 and kac_çaliştim < 11:
       print ('Sayın',  'Çalışanımız ','Zamlı maaşınız : ' , (maas * (15 / 100))+maas)
elif kac_çaliştim >11 :
         print ('Sayın',  'Çalışanımız ','Zamlı maaşınız : ', (maas/5)+maas)