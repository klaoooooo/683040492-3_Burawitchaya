"""
Burawitchaya Rongthong
683040492-3
P1
"""
n = input("Enter a birth year: ")
try:
    n = int(n)
    age = 2024 - n
    print(f"Your age is {age}")
    if age < 0 or age > 120:
        print("Invalid age.")
    else:
        if  age < 18:
            print("Sorry kid.")
        else:
            print("You are good to go.")
            if age >= 85:
                print("Please be extra careful when driving!")
except ValueError as e:
    print(f"Catch ValueError: {e}")

