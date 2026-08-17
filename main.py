def addtwonumbers(a, b):
    return a + b

print("Sum of numbers are " + str(addtwonumbers(5, 10)))


def factorial(number):
    if number < 0:
        return None

    result = 1
    for value in range(1, number + 1):
        result *= value

    return result


number = int(input("Enter a number: "))
factorial_result = factorial(number)

if factorial_result is None:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of " + str(number) + " is " + str(factorial_result))
