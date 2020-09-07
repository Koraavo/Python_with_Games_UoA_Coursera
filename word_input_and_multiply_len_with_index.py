'''

Inputs words from the user,
one per line and saves the words in a list until the user enters the word stop.
The word stop should not be included in the list.
The program should then output the list. It should then replace each word in the word list,
whose index is even by its index multiplied by the length of the word. It should then output this modified list.

Enter a word >computer
Enter a word >science
Enter a word >university
Enter a word >alberta
Enter a word >edmonton
Enter a word >stop
['computer', 'science', 'university', 'alberta', 'edmonton']
[0, 'science', 20, 'alberta', 32]
'''

word_list = []
word = input("Enter a word >")
while word != 'stop':
    word_list.append(word)
    word = input("Enter a word >")
print(word_list)

for index in range(len(word_list)):
    word_index = word_list[index]
    if index % 2 == 0:
        word_list[index] = index*len(word_index)
print(word_list)

