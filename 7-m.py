import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["nom", "narx", "soni"])
    writer.writerows(mahsulotlar)

print("Ma'lumot saqlandi!")