"""
Burawitchaya Rongthong
683040492=3
P1
"""
r = int(input("Number of row: "))
c = int(input("Number of column: "))

for row in range(r):
    for col in range(c):
        print(f"{col+1}", end = "\t")
    print()