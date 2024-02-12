number1 = int(input('1.sayıyı giriniz'))
number2 = int(input('2.sayıyı giriniz'))
number3 = int(input('3.sayıyı giriniz'))

if number1 > number2 and number1 >number3 :
    print (number1,'bu sayı daha büyük')
elif number2 > number1 and number2 >number3 :
    print (number2,'bu sayı daha büyük')

if number3 > number2 and number3 >number1 :
    print (number3,'bu sayı daha büyük')