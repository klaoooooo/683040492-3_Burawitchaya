"""
Burawitchaya Rongthong
683040492=3
P8
"""
fi = open("equations.txt", "r")
out = open("results.txt", "w")
for i in fi:
    i.strip()
    x = i.split()

    if x[1] == "+":
        total = float(x[0]) + float(x[2])
    elif x[1] == "-":
        total = float(x[0]) - float(x[2])
    elif x[1] == "*":
        total = float(x[0]) * float(x[2])
    elif x[1] == "/":
        total = float(x[0]) / float(x[2])
    elif x[1] == "//":
        total = float(x[0]) // float(x[2])

    print(f"{x[0]} {x[1]} {x[2]} {x[3]} {x[4]}")
    if float(x[4]) == total:
        print("Correct")
    else:
        print("Wrong")
        out.write(f"{x[0]} {x[1]} {x[2]} {x[3]} {total}\n")