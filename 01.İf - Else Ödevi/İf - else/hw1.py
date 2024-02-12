def slmn():
    note1 = int(input("1.Notunuzu girin: \n"))
    note2 = int(input("2.Notunuzu girin: \n"))
    performance = int(input("Performan notunuzu girin: \n"))
    ortalama = (note1 + note2 + performance) / 3
    print(ortalama)
slmn()
def slmn1():
    if slmn <= 50:
        print("Başarısız oldun.")

    elif slmn >= 50 :
        print("Başarılı oldun.")
slmn1()