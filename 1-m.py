matritsa = [
    [1, 2, 3, 9, 6],
    [4, 5, 6, 7, 8]
]
yigindi = 0
for i in matritsa:
    for son in i:
        yigindi += son
print(f"Yig'indi: {yigindi}")