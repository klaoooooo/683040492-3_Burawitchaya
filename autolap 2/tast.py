"""
Burawitchaya Rongthong
683040492-3
P5
"""

try:
    fi = input("Enter input filename: ")
    o_file = open(fi, "r")
except FileNotFoundError:
    print(f"\tError: {fi} not found")
    exit()

for line in o_file:
    print("-----")
    li = line.strip()
    print(f"Processing: {li}")

    parts = li.split()
    
    if len(parts) != 3:
        print("\tError: Skipped")
        continue

    a, op, b = parts

    # แปลงตัวเลข
    try:
        a_val = float(a) if '.' in a else int(a)
        b_val = float(b) if '.' in b else int(b)
    except:
        print("\tError: Non-numeric operand")
        continue

    # ตรวจ operator
    if op != "+":
        print(f"\tError: Unsupported operator {op}")
        continue

    print(f"{a} is {type(a_val)}, {b} is {type(b_val)}")
    print(f"{a} + {b} = {a_val + b_val}")