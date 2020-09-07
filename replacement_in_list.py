list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)
number = input("Enter an integer between 1 and 10 >")

if str.isdigit(number):
    number_int = int(number)
    if number_int in list1:
        new_index = list1.index(number_int)
        list1[new_index] = 'gone'
        print(list1)
    else:
        print(number, "is not between 1 and 10")
else:
    print(number, "is not a positive integer")

