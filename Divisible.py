def divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

def divisible_by_7(number):
    if number % 7 == 0:
        return True
    else:
        return False

def divisible_by_9(number):
    if number % 9 == 0:
        return True
    else:
        return False

def divisible_by_10(number):
    if number % 10 == 0:
        return True
    else:
        return False

if __name__ =="__main__":
    number1 = int(input("Enter num1:"))

    divisibleBy5 = divisible_by_5(number1)
    print(divisibleBy5)

    divisibleBy7 = divisible_by_7(number1)
    print(divisibleBy7)

    divisibleBy9 = divisible_by_9(number1)
    print(divisibleBy9)

    divisibleBy10 = divisible_by_10(number1)
    print(divisibleBy10)

