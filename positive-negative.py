print("Write a Python program that asks the user to input an integer." 
"If the user enters an integer, output the negative of that integer." 
"If the user does not enter an integer, output a warning message." 
"For this question a valid integer consists of one or more digits (0-9) with an optional leading minus sign (-).")

number = input("Enter an integer >")
if str.isdigit(number[1]):
    if number.startswith('-', 0):
        print("The negative of", number, "is", number.strip('-'))
    else:
        print("The negative of", number, "is", '-' + number)
else:
    print(number, "is not an integer")