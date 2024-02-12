Bagaj_Kilosu = int(input("Bagaj kilonuzu söyleyiniz: \n"))

if Bagaj_Kilosu <= 20:
    print("Ücret ödemenize gerek yoktur.")

elif Bagaj_Kilosu > 20:
    print((Bagaj_Kilosu - 20 )*10,'TL ödeyeceksiniz.')
