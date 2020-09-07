def largest_two(target_list):
    list1 = []

    # create lists of elements with first element and second element like a multiplication table

    for i in range(len(target_list)):
        for j in range(len(target_list)):
            word1 = target_list[i]
            word2 = target_list[j]
        #print(word1,"x", word2)

            # check if the word/element is bigger than the other element and add the bigger to the list
            if word1 > word2:
                list1.append(word1)
    #print(list1)

    # check the highest occurrence for the word/element and print the word
    highest_occurrences = max(list1)

    # second highest occurrence calculation
    # new element list (shallow duplicate)
    # remove highest occurrence in a new list
    new_list = list1[:]
    print(new_list)

    while highest_occurrences in new_list:
        new_list.remove(highest_occurrences)

    second_highest_occurrence = max(new_list)
    print("The largest and second largest elements in the list", target_list, "are", highest_occurrences, "and", second_highest_occurrence)

largest_two(['computer', 'science', 'university', 'alberta', 'edmonton'])
largest_two([4, 2, 8, 7, 8])

# SIMPLIFIED VERSION:

def largest_two(target_list):

    # check the highest occurrence for the word/element and print the word
    new_list = list(target_list)
    highest_occurrences = max(new_list)

    new_list.remove(highest_occurrences)
    second_highest_occurrence = max(new_list)

    print("The largest and second largest elements in the list", new_list, "are", highest_occurrences, "and", second_highest_occurrence)

largest_two(['computer', 'science', 'university', 'alberta', 'edmonton'])

largest_two([4, 2, 8, 7, 8])