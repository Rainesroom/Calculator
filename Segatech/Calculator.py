while True:
    one = input("Which math type do you want to use? (1) Multiplication, (2) division, (3) addition, (4) subtraction. Enter it's corresponding number (1, 2, 3, 4). ")

    if one == "1":
        print("Multiplication is selected")
        factor1 = input("Enter the first factor: ")
        factor2 = input("Enter the second factor: ")

        factor1 = int(factor1)
        factor2 = int(factor2)

        product = factor1 * factor2

        print("The product is:", product)

    elif one == "2":
        print("Division  is selected")
        dividend = input("Enter the dividend: ")
        divisor = input("Enter the divisor: ")

        dividend = int(dividend)
        divisor = int(divisor)

        quotient = dividend / divisor

        print("The quotient is: ", quotient)

    elif one == "3":
        print("Addition is selected.")
        addend1 = input("Enter the first addend: ")
        addend2 = input("Enter the second addend: ")

        addend1 = int(addend1)
        addend2 = int(addend2)

        sum = addend1 + addend2

        print("The sum is: ", sum)

    elif one == "4":
        print("Subtraction is selected.")
        minuend = input("Enter the minuend: ")
        subtrahend = input("Enter the Subtrahend: ")

        minuend = int(minuend)
        subrahend = int(subtrahend)

        difference = minuend - subrahend

        print("The difference is: ", difference)

    else:
        print("Type of math not avaliable")
