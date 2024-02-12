number1 = int(input("1. sayıyı giriniz\n"))

number2 = int(input("2. sayıyı giriniz\n"))
exit= input ('çıkabilirsin (q)')
print ('q ile çıkılır')

while number1 != ("q") or number2 != ('q'):
      print((number1 + number2 )/2)

      number1 = int(input("1. sayıyı giriniz\n"))

      number2 = int(input("2. sayıyı giriniz\n"))
      exit= input ('çıkabilirsin (q)')
      if exit == ('q') :
        print('çıkıldı')


