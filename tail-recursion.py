# Name: Kushal Kothari
# Uni ID: N15066497

def custom_tail_factorial(number, accumulator=1):
    # Check if the number is not greater than 1
    if not (number > 1):
        return accumulator
    else:
        # Perform the tail recursion with the updated accumulator
        return custom_tail_factorial(number - 1, number * accumulator)

print("The factorial of 99999 is:", custom_tail_factorial(99999))