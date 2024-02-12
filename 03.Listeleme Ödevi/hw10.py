tek =[5,7,9,11,13,15]
cift  =[6,8,10,12,14,16]
tek1=tek.copy()
tek.insert(1,6)
tek.insert(3,8)
tek.insert(5,10)
tek.insert(7,12)
tek.insert(9,14)
tek.insert(11,16)
print(tek)

tek.remove(5)
tek.remove(6)
tek.remove(8)
tek.remove(9)
tek.remove(10)
tek.remove(11)
tek.remove(12)
tek.remove(13)
tek.remove(15)
tek.remove(16)
print(tek)


cift.remove(6 and 8 and 14 and 16)
tek1.remove(5 and 9 and 11 and 13  and 15)
print('Tek : ', tek)
print('Çift : ',cift)