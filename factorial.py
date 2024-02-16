# Name : Kushal Kothari
# Univ ID: N15066497

def custom_factorial(value):
    # If the value is not greater than 1, then it must be 1 or less, hence return 1
    if not (value > 1):
        return 1
    # Otherwise, continue the recursion by multiplying the current value by the factorial of the previous value
    return value * custom_factorial(value - 1)

print("The factorial of 99999 is:", custom_factorial(99999))