def get_inputs():
    w = float(input("Water usage: "))
    while w < 0:
        print("Usage value must be positive.")
        w = float(input("Water usage: "))

    e = float(input("Electricity usage: "))
    while e < 0:
        print("Usage value must be positive.")
        e = float(input("Electricity usage: "))
    return w,e

def water_fee(w):
    if w <= 30:
        wf = w*10 + 30
    else:
        wf = w*20 + 30
    return wf

def elec_fee(e):
    if e <= 150:
        ef = e*3 + 10
    else:
        ef = e*5 + 10
    return ef