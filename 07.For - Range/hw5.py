number1 = int(input("Lütfen 1.sayıyı giriniz: \n"))

number2 = int(input("Lütfen 2.sayıyı giriniz: \n"))

toplam = 0

for numbers in range(number1+1,number2):
    toplam += numbers

print("İki sayının arasındaki sayıların toplamı:  ",toplam) 