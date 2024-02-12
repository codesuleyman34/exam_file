kilo =float(input('İyi günler. Lütfen kilonuzu giriniz.\n'))
boy = float(input('İyi günler. Lütfen boyunuz giriniz.\n'))

vki= kilo/(boy*boy)

if vki > 17 and vki < 26:
    print ('Normal')
elif vki > 24 and vki < 30:
    print ('Kilolu')
elif vki > 29 and vki<35:
    print('Obez')
elif vki > 34 :
    print('Ciddi obez')