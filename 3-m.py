mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

mahsulot = input("Mahsulot nomi: ")

if mahsulot in mahsulotlar:
    narx = int(input("Yangi narx: "))
    mahsulotlar[mahsulot] = narx
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi.")