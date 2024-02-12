hava_sıcaklığı = int(input("İyi günler. Lütfen hava sıcaklığı girin. \n"))

if hava_sıcaklığı <= 5 :
    print("Hava soğuk.")

elif hava_sıcaklığı >5 and hava_sıcaklığı <15:
    print("Hava ılık.")

elif hava_sıcaklığı >14 :
    print("Hava sıcak.")