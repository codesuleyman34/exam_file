mekan = input('Sinemaya mı gideceksiniz yoksa tiyatroya mı? \n')
nesin = input('Öğrenci misiniz yoksa tam mısınız? \n ')

if mekan == 'sinema' and nesin == 'öğrenci':
    print(15/2,'TL ödeyeceksiniz.')
elif mekan == 'sinema' and nesin == 'tam':
    print(15,'TL ödeyeceksiniz.')
elif mekan == 'tiyatro' and nesin == 'öğrenci':
    print(10/2,'TL ödeyeceksiniz.')
elif mekan == 'tiyatro' and nesin == 'tam':
    print(10,'TL ödeyeceksiniz.')