açı1 = int(input("1.Açıyı girin: \n"))

açı2 = int(input("2.Açıyı girin: \n"))

açı3 = int(input("3.Açıyı girin: \n"))

toplamı = açı1 + açı2 + açı3

if toplamı == 180:
    print("Bu bir üçgendir.")

if toplamı != 180:
    print("Bu bir üçgen değildir.")