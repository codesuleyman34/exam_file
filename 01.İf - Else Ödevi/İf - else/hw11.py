açı1 = int(input('İyi günler. Lütfen 1. açıyı giriniz. \n'))
açı2 = int(input('İyi günler. Lütfen 2. açıyı giriniz. \n'))
açı3 = int(input('İyi günler. Lütfen 3. açıyı giriniz. \n'))

if açı1 == açı2 == açı3 :
    print ('Eşkeanar Üçgen.')

elif açı1 == açı2 or açı1 == açı3 or  açı2 == açı3 :
    print ('İkizkenar Üçgen.')

else:
    print('Çeşitkenar Üçgen.')