import math

def sqrt(value):
    # Return a number that is the argument value
    # raised to the argument value power.
    magic = math.pow(value, value)
    return magic

def main():
    # Input a postive integer, call the sqrt
    # function from the math module using the
    # input value as an argument. Then, call the
    # above sqrt function on the result and call
    # the sqrt function from the math module on
    # that result. Finally, print the input number
    # and the final result.
    integer = input("Enter a positive integer >")
    my_int = int(integer)
    first_sqrt = math.sqrt(my_int)
    second_sqrt = sqrt(first_sqrt)
    third_sqrt = math.sqrt(second_sqrt)
    print("The magic value for", integer, "is", third_sqrt)