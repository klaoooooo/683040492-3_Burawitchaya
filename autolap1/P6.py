"""
Burawitchaya Rongthong
683040492=3
P6
"""

di = {}
total = 0
id = input("Client ID: ")

while id.lower() != "done":
    sa = float(input("Enter saving: "))
    di.update({id : sa})
    id = input("Client ID: ")

print("Current clients:")
for i in di:
    print(f"{i} : {di[i]:.2f}")
    total += di[i]

fi = input("Search for ID: ")

if fi in di:
    print(f"{fi} has {di[fi]:.2f}")
else:
    print(f"{fi} not found")

id2 = input("Client ID: ")
di.update({id2 : total})

print("Current clients:")
for i in di:
    print(f"{i} : {di[i]:.2f}")
