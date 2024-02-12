otopark_saat = int(input("İyi günler. Lütfen kaç saat kaldınız? \n" ))

if otopark_saat == 1 :  
        print("Borcunuz 5TL.")
    
elif otopark_saat > 1 and  otopark_saat < 5 :
        print("Borcunuz : " , otopark_saat * 4)
    
elif otopark_saat > 5 :
        print("Borcunuz :" ,  otopark_saat * 3)
