from P2f import water_fee,get_inputs,elec_fee

if __name__ == "__main__":
    w, e = get_inputs()

    print("---------------------------")

    print("This month's utility bills:")

    wf = water_fee(w)
    ef = elec_fee(e)
    print(f"Water: usage = {w:.2f} units")
    print(f"fee = {wf:.2f} Baht")

    print(f"Electricity: usage = {e:.2f} units")
    print(f"fee = {ef:.2f} Baht")
