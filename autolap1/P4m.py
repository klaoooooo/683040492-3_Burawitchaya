"""
Burawitchaya Rongthong
683040492=3
P4m
"""
from P4f import get_inputs,water_fee,elec_fee
if __name__ == "__main__":
    w,e = get_inputs()
    print("---------------------------")
    print("This month's utility bills:")
    total_w = water_fee(w)
    print(f"Water: usage = {w:.2f} units")
    print(f"fee = {total_w:.2f} Baht")
    total_e = elec_fee(e)
    print(f"Electricity: usage = {e:.2f} units")
    print(f"fee = {total_e:.2f} Baht")
