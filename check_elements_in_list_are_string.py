# CHeck if the elements are integers - add the elements
# if string put it into a different list as well


def main():
    user_input = input("Enter some integers >")
    list1_input = user_input.split(" ")
    list2 = ['20', 10, len, True, '-10', '0']
    as_integer_list = as_integer(list2)
    filter_ints_list = filter_ints(list1_input)
    for i in as_integer_list:
        print(i)

    sum = 0
    for i in filter_ints_list[0]:
        sum = sum+int(i)
    print("The sum of:", filter_ints_list[0], "is", sum)
    print("These words are not integers", filter_ints_list[1])



def filter_ints(word_list):
    # Return a tuple containing two lists.
    # The first list should contain an int
    # for each element of the argument list
    # that is a string that represents
    # a valid integer. The second list should
    # contain all the elements of the argument
    # list that do not represent valid integers.
    integer_list = []
    non_integer_list = []
    for item in word_list:
        if item.isdigit():
            new_item1 = int(item)
        #if isinstance(item, int):
            integer_list.append(new_item1)
        else:
            non_integer_list.append(item)

    return (integer_list, non_integer_list)

def as_integer(an_object):
    # If the argument is a string that represents
    # a valid integer return that integer.
    # Otherwise, return the NoneType object.
    type_list = []
    for item in an_object:
        if isinstance(item, str):
            type_list.append(int(item))
        else:
            type_list.append(None)
    return type_list

main()