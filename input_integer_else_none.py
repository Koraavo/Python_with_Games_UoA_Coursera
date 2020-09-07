'''
def main():
    # Call the as_integer function for each
    # element in the list: ['20', 10, len, True, '-10', '0']
    # and output the result object on its own line
    list1 = ['20', 10, len, True, '-10', '0']
    for i in list1:
        new_list = as_integer(i)
        print(new_list)


def as_integer(an_object):
    # If the argument is a string that represents
    # a valid integer return that integer.
    # Otherwise, return the NoneType object.
    type_list = []
    if isinstance(an_object, str):
        return int(an_object)
    else:
        return None

main()
'''

def main():
    user_input = input("Enter some integers >")
    list1_input = user_input.split(" ")
    filter_ints_list = filter_ints(list1_input)
    sum = 0
    for i in filter_ints_list[0]:
        sum = sum + int(i)
    print("The sum of:", filter_ints_list[0], "is", sum)
    print("These words are not integers:", filter_ints_list[1])


def filter_ints(word_list):
    # Return a tuple containing two lists.
    # The first list should contain an int
    # for each element of the argument list
    # that is a string that represents
    # a valid integer. The second list should
    # contain all the elements of the argument
    # list that do not represent valid integers.
    first_list = []
    second_list = []
    combined_list = []
    for elements in word_list:
        check = as_integer(elements)
        combined_list.append(check)

    for item in combined_list:
        if isinstance(item, int):
            first_list.append(item)
        else:
            second_list.append(item)
    return (first_list, second_list)


def as_integer(an_object):
    if an_object.isdigit():
        return int(an_object)
    else:
        return an_object


main()