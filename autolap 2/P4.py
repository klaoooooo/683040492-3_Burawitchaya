"""
Burawitchaya Rongthong
683040492-3
P4
"""

t = 0

n = input("Enter 5 temps in Celcius: ").split()

if len(n) != 5:
    print("Please input exactly 5 numbers")
else:
    for i in n:
        try:
            i = float(i)
            t += i
        except ValueError as e:
            t = 0
            print(f"Catch ValueError: {e}")
            break
try:
    avg = t/len(n)
except:
    print("Please input exactly 5 numbers")

if t != 0:
    print(f"Average temperature = {avg:.2f} Celsius")


