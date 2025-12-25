"""
Burawitchaya Rongthong
683040492=3
P4f
"""
def get_inputs():
    w = float(input("Water usage: "))
    while w < 0:
        if w < 0:
            print("Usage value must be positive.")
            w = float(input("Water usage: "))
        else:
            break
    e = float(input("Electricity usage: "))
    while e < 0:
        if e < 0:
            print("Usage value must be positive.") 
            e = float(input("Electricity usage: "))
        else:
            break
    return w,e

def water_fee(w):
    if w <= 30:
        total_w = 30 + w*10
    else:
        total_w = 30 + w*20
    return total_w

def elec_fee(e):
    if e <= 150:
        total_e = 10 + e*3
    else:
        total_e = 10 + e*5
    return total_e
