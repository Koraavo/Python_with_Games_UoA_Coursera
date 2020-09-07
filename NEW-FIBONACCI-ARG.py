'''
Write user-defined functions with these function headers:

def append_fibonacci(integer_list):
    # Modify the argument list of integers by
    # appending a new integer that is the sum
    # of the last two integers in the list.
    # If the list has fewer than two elements
    # add the int object 1 to the list.

def fibonacci(max):
    # Return a list that contains all Fibonacci
    # numbers that are less than or equal
    # to the argument integer.

def main():
    # Input a non-negative integer, n. Output
    # the Fibonacci numbers that are less than
    # or equal to that number, in order. If the
    # input is not a valid non-negative integer,
    # output a warning message.

The main function must input a string.
If the string does not represent a non-negative integer, then it should print a warning message.
If it does represent a non-negative integer,
then it should call the fibonacci function to create the list of Fibonacci numbers
that are less than or equal to the non-negative integer and output this list.
The fibonacci function should call the append_fibonacci function multiple times to create the Fibonacci list.

Enter a non-negative integer >23
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13, 21]

Enter a non-negative integer >13
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13]

Enter a non-negative integer >0
The Fibonacci series starts with: []

Enter a non-negative integer >ten
ten is not a non-negative integer



'''

'''
def main():
    list = [3, 5, 8]
    final_list = append_fibonacci(list)
    print(final_list)


def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        res = 1
    else:
        res = sum(integer_list[-2:])
        integer_list.append(res)
    return integer_list

main()
'''
## Part 2
# def append_fibonacci(integer_list):
#     if len(integer_list) < 2:
#         res = 1
#     else:
#         res = sum(integer_list[-2:])
#     integer_list.append(res)
#     return integer_list

# def main():
#     user_input = input("Enter a non-negative integer >")
#     if str.isdigit(user_input) == True:
#         int_user_input = int(user_input)
#         fibonacci_list = fibonacci(int_user_input)
#         print("The Fibonacci series starts with:", fibonacci_list)
#     else:
#         print(user_input, "is not a non-negative integer")
#
#
# def fibonacci(max):
#     integer_list = []
#     while True:
#         integer_list = append_fibonacci(integer_list)
#         res = integer_list[-1]
#         if res > max:
#             integer_list.pop()
#             return integer_list


# Part 1:
def main():
    list1 = [3, 5, 8]
    append_fibonacci(list1)
    print(list1)

def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        res = 1
    else:
        res = sum(integer_list[-2:])
    integer_list.append(res)

main()
