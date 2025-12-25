"""
Burawitchaya Rongthong
683040492-3
P3
"""
r_ph = []
num = True

ph = input("Enter your phone number: ")

print("Phone number (no special char): ", end = "")
for i in ph:
    if i == "-" or i == "(" or i == ")" or i == " ":
        pass
    else:
        print(i, end = "")
        r_ph.append(i)
print()

for i in r_ph:
    if i.isdigit() == False:
        num = False

if num == False:
    print("Not all char are numbers.")

if len(r_ph) != 10:
    print("Invalid length.")

if num == True and len(r_ph) == 10:
    print("Formatted phone number: ", end = "")
    for i in range(len(r_ph)):
        if i == 0:
            print(f"({r_ph[i]}", end = "")
        elif i == 2:
            print(f"{r_ph[i]})", end = " ")
        elif i == 5:
            print(f"{r_ph[i]}-", end = "")
        else:
            print(f"{r_ph[i]}", end = "")
