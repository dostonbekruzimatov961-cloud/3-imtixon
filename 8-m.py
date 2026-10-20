import json

with open('products.json', 'r', encoding='UTF-8') as f:
    products = json.load(f)

mahsulot = input("Mahsulotni kiriting: ").title()
soni = int(input("Mahsulot sonini kiriting: ")) 

topildi = False

for i in products:
    if i["nom"] == mahsulot:
        i["miqdor"] = soni
        topildi = True
        break

if topildi:
    with open('products.json', 'w', encoding='UTF-8') as f:
        json.dump(products, f, indent=4)
    print(f"{mahsulot} miqdori yangilandi!")
else:
    print(f"{mahsulot} bunday mahsulot topilmadi!")