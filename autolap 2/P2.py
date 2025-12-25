"""
Burawitchaya Rongthong
683040492-3
P2
"""
sp = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
up = False
num = False
s = False

p = input("Enter your password: ")

if len(p) < 8:
    print("- Password must be at least 8 characters long")

for i in p:
    if i.isupper() == True:
        up = True
    if i.isdigit() == True:
        num = True
    if i in sp:
        s = True

if up == False:
    print("- Password must contain at least one uppercase letter")

if num == False:
    print("- Password must contain at least one number")

if s == False:
    print("- Password must contain at least one special character (!@#$%^&*?)")

if len(p) >= 8 and up == True and num == True and s == True:
    print("There you go! The password is valid.")