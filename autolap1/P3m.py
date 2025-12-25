"""
Burawitchaya Rongthong
683040492=3
P3m
"""
''' --------------------------
Do not change anything here 
------------------------------'''
from P3f import get_inputs,more_saving

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    money = get_inputs()
    print(f"You had {money:.2f} Baht.")
    total = more_saving(money)
    print(f"Now you have {total:.2f} Baht.")