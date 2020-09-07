"""
Write a program that prompts the user to enter an integer
and displays the absolute value of that integer on one line
and then the original integer on the next line.

Enter an integer >-25
25
-25
"""

"""
Write a program that prompts the user to enter two integers, 
one per prompt. The program should then display the result of 
dividing the first number by the second number, 
using integer division so that the answer is an integer quotient, 
and a remainder.

Enter an integer >17
Enter an integer >3
17 divided by 3 is 5 remainder 2
"""
"""
Write a program that prompts the user to enter a number of degrees. 
The program should then use the sin function from the math library 
to compute and display the sin of the angle. 
Since the sin function expects its argument to be 
an angle in radians instead of degrees you must convert 
from degrees to radians before calling the sin function. 
Look in the math module for a function 
that converts an angle from degrees to radians 
and import and use that function as well.

Enter an angle in degrees >30
The sin of 30 degrees is 0.49999999999999994
"""

"""
Write a Python program that asks the user to 
input a string and a sub-string and 
outputs the number of occurrences of the sub-string in the string.

Enter a string >banana
Enter a substring >na
the substring "na" appears 2 times in "banana"

word = input('Enter a string >')
new_word = '"{}"'.format(word)
sub_str = input('Enter a substring >')
new_sub_str = '"{}"'.format(sub_str)
count = str.count(word, sub_str)
print('the substring', new_sub_str, 'appears', count, 'times in', new_word)
"""

"""
Write a Python program that asks the user to input an integer. 
If the user enters a non-negative integer, output the factorial of that value. 
If the user enters a negative integer, don't output anything.

Enter an integer >4
24

Enter an integer >-4

Write a Python program that asks the user to input a non-negative integer. 
If the user enters a non-negative integer, output two times that value. 
If the user does not enter a non-negative integer, 
output a warning message.

Enter a non-negative integer >43
43 * 2 is 86

Enter a non-negative integer >hello
hello is not a non-negative integer

number = input("Enter a non-negative integer >")
if str.isdigit(number) == True:
  new_number = int(number)
  multiply = new_number*2
  print(new_number, "* 2 is",multiply )
else:
  print(number, "is not a non-negative integer")
"""

"""
Enter an integer >-43
The negative of -43 is 43

Enter an integer >43
The negative of 43 is -43

Enter an integer >fortythree
fortythree is not an integer


number = input("Enter an integer >")
if str.isalpha(number)== False:
    if number.startswith('-', 0):
        print("The negative of", number, "is", number.strip('-'))
    else:
        print("The negative of", number, "is", '-' + number)
else:
    print(number, "is not an integer")
"""

"""
Enter a string with an e in the middle >alberta
Yes, alberta has e in the middle, at index 3

Enter a string with an e in the middle >edmontonian
No, edmontonian has t in the middle, at index 5

Enter a string with an e in the middle >keep
No, keep has no middle character

"""
"""
Write a Python program that creates 
an empty list and an empty tuple 
and then outputs them as shown in the sample run. 
The program must then input a string, 
use the append method to append the str object to the empty list 
and output the list. 
The program must then create a tuple that 
contains the same str object and output the tuple.

However, you cannot use the append method 
to append the str object to the empty tuple, 
since tuples are immutable. 
Instead you must use the tuple function, 
with the list containing the str object as an argument. 
The tuple function creates a new tuple whose elements 
are the same as the argument object, 
which in this case is your list containing the str object.

Note that it is possible to create your tuple 
using an expression list, 
instead of using the tuple function 
and it is possible to create your list using a list display:

my_tuple = (my_string)
my_list = [my_string]

[]
()
Enter a string >hello
['hello']
('hello',)

"""

"""
Write a program that uses a list display 
to create a list containing the integers from 1 to 10 
in increasing order, and outputs the list. 
Then prompt the user to enter a number between 1 and 10, 
replace this number by the str object "gone" and output the list. 
If the user enters a string that does not represent 
an integer between 1 and 10, 
instead output the appropriate message 
that indicates this situation, as shown in the sample runs:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter an integer between 1 and 10 >15
15 is not between 1 and 10

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter an integer between 1 and 10 >hello
hello is not a positive integer
"""

"""
Enter some words >The cat in the hat meets R2D2!
['The', 'cat', 'in', 'the', 'hat', 'meets', 'R2D2!']
The THE
cat CAT
in IN
the THE
hat HAT
meets MEETS
R2D2! R2D2!
"""
"""
Prompt the user to enter the Fibonacci numbers in order 
until the user either makes a mistake 
or enters the first Fibonacci number greater than 50. 
If the user makes an error, 
output a consolation message as shown in the sample run 
and end the program. If the user enters all of the 
Fibonacci numbers successfully then output a 
congratulations message as shown in the 
sample runs and end the program. 
Some people start the Fibonacci numbers 
and 0 and some people start at 1. 
In this question, we will start at 1:

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >2
Enter the next Fibonacci number >3
Enter the next Fibonacci number >5
Enter the next Fibonacci number >8
Enter the next Fibonacci number >13
Enter the next Fibonacci number >21
Enter the next Fibonacci number >34
Enter the next Fibonacci number >55
Well done

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >4
Try again

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >2
Enter the next Fibonacci number >3
Enter the next Fibonacci number >5
Enter the next Fibonacci number >8
Enter the next Fibonacci number >13
Enter the next Fibonacci number >21
Enter the next Fibonacci number >34
Enter the next Fibonacci number >60
Try again

"""
"""
Write a program that inputs words from the user, 
one per line and saves the words in a list until 
the user enters the word stop. 
The word stop should not be included in the list. 
The program should then output the list. 
It should then replace each word in the word list, 
whose index is even by its index multiplied by the length of the word. 
It should then output this modified list.

Enter a word >computer
Enter a word >science
Enter a word >university
Enter a word >alberta
Enter a word >edmonton
Enter a word >stop
['computer', 'science', 'university', 'alberta', 'edmonton']
[0, 'science', 20, 'alberta', 32]
"""

"""
def stats():
  # Output the list that the global idenfifier
  # my_list is bound to and the mean and
  # the population standard deviation of the
  # numbers in the list, rounded to two decimal
  # places.
  
[2, 4, 6, 8, 10, 12]
mean is 7.0
population standard deviation is 3.42

Hint:

There is a built-in function that rounds float objects to a particular number 
of digits after the decimal point and a function in the math module that computes 
the square root of a number.

You can look up the definitions of 
mean and population standard deviation on the internet. 
You should compute the population standard deviation, 
not the sample population deviation.
"""

"""
def largest_two(target_list):
  # Output the argument list, the largest
  # element in the list and the second largest
  # element in the list
  
The largest and second largest elements in the list 
['computer', 'science', 'university', 'alberta', 'edmonton'] 
are university and science

The largest and second largest elements in the list 
[4, 2, 8, 7, 8] are 8 and 8

Hint:

You can use a built-in function to find the maximum element in a list. 
Then you can use a method to make a copy of your list 
(the Python documentation calls this a shallow copy). 
Then you can apply a different method to remove 
this largest element from this list copy. 
Then you can use the same built-in function 
you used before to find the maximum element 
of this shorter list, which will be the second largest element 
of the original list. 
You need to make a copy since if you remove the largest element 
from your original list, it won't be there when you output 
the original list.

def largest_two(target_list):

    # check the highest occurrence for the word/element and print the word
    new_list = list(target_list)
    highest_occurrences = max(new_list)

    new_list.remove(highest_occurrences)
    second_highest_occurrence = max(new_list)

    print("The largest and second largest elements in the list", new_list, 
    "are", highest_occurrences, "and", second_highest_occurrence)
"""
"""
def string_lengths(string_list):
    # Create a new list that contains the
    # lengths of the strings in the argument
    # list or an empty list if the argument list
    # is empty. Output the original list and the
    # length list.

def main():
    # Input a list of words, output them as a
    # list, and output a list that contains
    # their lengths
    
Enter some words >edmonton, science, computer, alberta
['edmonton,', 'science,', 'computer,', 'alberta']
[9, 8, 9, 7]

Enter some words >
[]
[]

"""

"""
def as_integer(an_object):
  # If the argument is a string that represents
  # a valid integer return that integer.
  # Otherwise, return the NoneType object.
  
def main():
  # Call the as_integer function for each
  # element in the list: ['20', 10, len, True, '-10', '0']
  # and output the result object on its own line

Here is a sample run of a main program that just calls the main function.  
20
None
None
None
-10
0
  
Use the user-defined function, as_integer, 
that you wrote in the previous question. In addition, 
write user-defined functions with these function headers:

def filter_ints(word_list):
  # Return a tuple containing two lists.
  # The first list should contain an int
  # for each element of the argument list
  # that is a string that represents
  # a valid integer. The second list should
  # contain all the elements of the argument
  # list that do not represent valid integers.
  
def main():
  # Prompt the user to enter some integers,
  # separated by blanks. Output a list of the
  # valid integers and the sum of these
  # integers. If the list contains some
  # "words" that are not valid integers, then
  # output a list of these "error words".
  
Enter some integers >2 4 six 8 ten 12 14
The sum of: [2, 4, 8, 12, 14] is 40
These words are not integers: ['six', 'ten']

Enter some integers >1 3 5
The sum of: [1, 3, 5] is 9

"""

"""
def append_fibonacci(integer_list):
  # Modify the argument list of integers by
  # appending a new integer that is the sum
  # of the last two integers in the list.
  # If the list has fewer than two elements
  # add the int object 1 to the list.
  
def main():
  # Call the append_fibonacci function on this
  # list: [3, 5, 8] and output the result object
  
[3, 5, 8, 13]
Hint:

Use subscription to access the last two elements of the list 
and the append method to add a new element at the end.

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
    
Hint:

Each time you call the append_fibonacci function 
it appends one more element to the list. 
You can keep calling it from the fibonacci function 
while its last element is less than or equal to the 
non-negative integer that was input and then remove 
the last element from the list.
    
Enter a non-negative integer >23
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13, 21]

Enter a non-negative integer >13
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13]

Enter a non-negative integer >0
The Fibonacci series starts with: []

Enter a non-negative integer >ten
ten is not a non-negative integer

def main():
    user_input = input("Enter a non-negative integer >")
    if str.isdigit(user_input) == True:
        int_user_input = int(user_input)
        fibonacci_list = fibonacci(int_user_input)
        print("The Fibonacci series starts with:", fibonacci_list)
    else:
        print(user_input, "is not a non-negative integer")


def fibonacci(max):
    integer_list = []
    while True:
        integer_list = append_fibonacci(integer_list)
        res = integer_list[-1]
        if res > max:
            integer_list.pop()
            return integer_list


def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        res = 1
    else:
        res = sum(integer_list[-2:])
    integer_list.append(res)
    return integer_list


"""
def main():
    list1 = []
    test = append_fibonacci(list1)
    print(test)

def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        res = 1
    else:
        res = sum(integer_list[-2:])
    integer_list.append(res)
    return integer_list

main()
