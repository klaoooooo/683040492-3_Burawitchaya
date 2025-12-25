"""
Burawitchaya Rongthong
683040492=3
P2
"""
r = int(input("Number of row: "))
c = int(input("Number of column: "))

for row in range(r):
    for col in range(c):
        if row == 0 or row == r-1 or col == 0 or col == c-1:
            print("*", end = " ")
        elif row == r // 2 and col == c // 2:
            print(f"x", end = " ")
        else:
            print(f"A", end = " ")
    print()
