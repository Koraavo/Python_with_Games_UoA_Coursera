def string_lengths(string_list):
    # Create a new list that contains the
    # lengths of the strings in the argument
    # list or an empty list if the argument list
    # is empty. Output the original list and the
    # length list.
    length_list = []
    for i in range(len(string_list)):
        word = string_list[i]
        if word == '':
            string_list.clear()
            length_list.clear()
        else:
            length = len(word)
            length_list.append(length)
    print(string_list)
    print(length_list)


def main():
    # Input a list of words, output them as a
    # list, and output a list that contains
    # their lengths
    strings = input("Enter some words >")
    split_string = strings.split(' ')
    string_lengths(split_string)

main()
