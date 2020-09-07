'''
Prompt the user to enter the Fibonacci numbers in order until the user either makes a mistake
or enters the first Fibonacci number greater than 50.
If the user makes an error, output a consolation message as shown in the sample run and end the program.
If the user enters all of the Fibonacci numbers successfully then output a congratulations message
as shown in the sample runs and end the program.
Some people start the Fibonacci numbers at 0 and some people start at 1. In this question, we will start at 1:

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

Hint:

You could check the user's entries against a list you construct using a list display,
or you can use the formula that
every number is the sum of the previous two numbers to check whether the user is correct.

If you use the second approach you can compare the guess to the sum of the previous number
and the current number every time a new guess is entered
and then update previous number to be the current_number
and the current number to be the guess.
However, if you do this, you will need to use a "trick" at the start,
by binding previous number to 1 and current number to 0,
instead of the more obvious binding of previous number to 0 and
current number to 1. This is necessary to "get started correctly".


'''


mx = 55
if int(input("Enter the next Fibonacci number >")) == 1 and \
        int(input("Enter the next Fibonacci number >")) == 1:  # short circuit
    lst, cur = 1, 1
    while True:
        nxt = lst + cur
        if nxt >= mx:
            print("Well done")
            break
        if nxt != int(input("Enter the next Fibonacci number >")):
            print("Try again")
            break
        lst = cur
        cur = nxt

else:
    print("Try again")

'''
pass1 = True
number1 = int(input("Enter the next Fibonacci number >"))
if number1 == 1:
    number2 = int(input("Enter the next Fibonacci number >"))
    if number2 == 1:
        pass1
        while True:
            number3 = number1 + number2

            if number3 == int(input("Enter the next Fibonacci number >")):
                number1 = number2
                number2 = number3
            else:
                pass1 = False
                break
            if number2 == 55:
                pass1
                break

            if number2 > 55:
                pass1 = False
                break
    else:
        pass1 = False
else:
    pass1 = False


if pass1:
    print("Well done")
else:
    print("Try again")
'''

'''
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
pass1 = True
for i in range(0, len(list1)):
    number = int(input("Enter the next FIBO number >"))
    if number == list1[i]:
        continue
    else:
        pass1 = False
        break

if pass1 == False:
    print("Try Again")
else:
    print("Well Done")

'''

'''
from functools import reduce


def fib(m=2):
    a, b = 1, 1
    while a <= m and b <= m:
        yield a
        yield b
        a += b
        b += a


def guess():
    for n in fib():
        if n != int(input("Enter the next Fibonacci number >")):
            print("Try again")
            yield False
            return
        yield True


if reduce(lambda a, b: a and b, guess()):
    print("Well done")
'''

def fibonacci(integer_list):
    # your code here
    a = 1
    b = 1
    for i in range(integer_list):
        print(a, "\t", b)
        a = a + b
        b = b + a


fibonacci(10)