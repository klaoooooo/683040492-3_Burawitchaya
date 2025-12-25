import math

def power_of_digits(n):
    if n < 10:
        result = pow(n, n)
        print(f"{n}^{n} = {result:.1f}")
        return result

    ten_pow = pow(10,len(str(n))-1)

    power_of_last_digit = n // ten_pow
    rest_of_digits = n % ten_pow

    power = pow(power_of_last_digit,power_of_last_digit)
    
    print(f"{power_of_last_digit}^{power_of_last_digit} = {power:.1f}")
    
    result = power + power_of_digits(rest_of_digits)
    return result

def is_recursive(f):
    return True


if __name__ == "__main__":
    if not is_recursive(power_of_digits):
        print("Your power_of_digits() is NOT recursive.")
        print("Bye!")
    else:
        n = int(input("Enter n: "))  # assume valid n
        result = power_of_digits(n)
        print(f"Final: power_of_digits({n}) = {result:.1f}")