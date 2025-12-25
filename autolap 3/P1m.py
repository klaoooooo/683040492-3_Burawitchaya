from P1f import get_inputs,more_saving

if __name__ == "__main__":
    money = get_inputs()

    print(f"You had {money} Baht.")

    saving = more_saving(money)
    print(f"Now you have {saving} Baht.")
