#User defined function to lessen lines
def getting_result (first, second, operation):
    #Response if the operation inputted is incorrect
    if operation == "SUM":
        print("Your result is", first + second, "\n")
    elif operation == "DIFFERENCE":
        print("Your result is", first - second, "\n")
    elif operation == "PRODUCT":
        print("Your result is", first * second, "\n")
    elif operation == "QUOTIENT":
        float_form = first / second
        print("Your result is", round(float_form, 2), "\n") #To control the decimals of float
response = "YES" #To start the while loop
while response == "YES": #For continuation
    try:
        wanted_result = input("What would you like to get? SUM/DIFFERENCE/PRODUCT/QUOTIENT: ") #Getting the operation
        if not (wanted_result == "SUM" or wanted_result == "DIFFERENCE" or wanted_result == "PRODUCT" or wanted_result == "QUOTIENT"):
            print("Please follow the format and input the correct response", "\n")
        else:
            #Getting the numbers
            first_num = int(input("What is your first number: "))
            second_num = int(input("What is your second number: "))
            getting_result(first_num, second_num, wanted_result)
        response = input("Do you want to try again? YES or NO: ")
    except ValueError: #If the inputted data for numbers is not digit
        print("Please type the appropriate response", "\n")
        response = input("Do you want to try again? YES or NO: ")
    except ZeroDivisionError:#If the inputted digit for second number is zero
        print("Please input appropriate number for divisor", "\n")
        response = input("Do you want to try again? YES or NO: ")
print("Thank you!")