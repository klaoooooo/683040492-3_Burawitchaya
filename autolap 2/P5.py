"""
Burawitchaya Rongthong
683040492-3
P5
"""
try:
    file = input("Enter input filename: ")
    o_file = open(file, "r")
            
except FileNotFoundError as e:
    print(f"\tError: {file} not found")
    exit()

for line in o_file:

    print("-----")

    li = line.strip()
    print(f"Processing: {li}")

    i = li.split()

    if len(i) == 3:

        a, op, b  =  i

        try:
            if '.' in a:
                a = float(a) 
            else:
                a = int(a)
        except ValueError:
            a = str(a)
        try:
            if '.' in b:
                b = float(b) 
            else: 
                b = int(b)
        except ValueError:
            b = str(b)

        print(f"{a} is {type(a)}, {b} is {type(b)}")

        if isinstance(a, str) or isinstance(b, str):
            print("\tError: Cannot operate with strings")

        else:
            if isinstance(a, float) and op == "%":
                print("\tError: Doesn't make any sense to mod with float.")
            elif isinstance(b, float) and op == "%":
                print("\tError: Doesn't make any sense to mod with float.")
            else:
                try:
                    try:
                        if op == "+":
                            to = a + b
                        elif op == "-":
                            to = a - b
                        elif op == "*":
                            to = a * b
                        elif op == "**":
                            to = a ** b
                        elif op == "/":
                            to = a / b
                        elif op == "//":
                            to = a // b
                        elif op == "%":
                            to = a % b
                        print(f"{a} {op} {b} = {to}")

                    except ZeroDivisionError:
                        print("\tError: divided by zero")
                    
                except TypeError:
                    print("\tError: Cannot operate with strings")
    else:
        print(f"\tError: Skipped {li}: not 3 terms")




        
