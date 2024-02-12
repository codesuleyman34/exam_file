number1 = int(input("1. sayıyı giriniz\n"))

number2 = int(input("2. sayıyı giriniz\n"))
print ('q ile çıkılır')
exit= input ('çıkabilirsin (q)')
while number1 != ("q") or number2 != ('q'):
      print((number1 + number2 ))

      number1 = int(input("1. sayıyı giriniz\n"))

      number2 = int(input("2. sayıyı giriniz\n"))
      exit= input ('çıkabilirsin (q)')
      if number2 == ('q') or number1 == ('q'):
        print('çıkıldı')


