"""
Burawitchaya Rongthong
683040492=3
P7
"""
ra = open("animals.txt", "r")
out = open("upper.txt", "a")

for i in ra:
    i = i.strip()
    if i == "":
        continue
    print(f"{i} upgraded to {i.upper()}")
    out.write(i.upper() + "\n")