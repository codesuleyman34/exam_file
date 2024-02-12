passaword=input('Şifre giriniz\n')
exam = 0
while passaword!= ('python'):
    print('Şifre yanlış\n')
    exam += 1
    passaword=input('Şifre giriniz\n')
    if passaword== 'python':
        print(exam,('Kerede girdiniz'))
        print('Şifre doğru\n')