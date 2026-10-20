mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

mahsulot = input("Mahsulot nomi: ")
narx = int(input("Yangi narx: "))

if mahsulot in mahsulotlar:
    mahsulotlar[mahsulot] = narx
    print("Narx yangilandi.")
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi.")