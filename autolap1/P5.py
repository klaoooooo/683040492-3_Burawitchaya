"""
Burawitchaya Rongthong
683040492=3
P5
"""
li = []
co = input("Enter a color: ")
while co.lower() != "done":
    li.append(co)
    co = input("Enter a color: ")

print("Color in order:")
for i in li:
    print(f"{i}", end = " ")
print()

a = len(li)
print("Color in reverse:")
for i in range(a):
    print(f"{li[a-i-1]}", end = " ")
print()

n = int(input("Enter color number: "))
print(f"{li[n]}")
