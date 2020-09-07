def reverse(word):
    my_list = list(word)
    my_list.reverse()
    reverse_string = ''.join(my_list)
    return reverse_string
def elaborate(word_list, word):
    reversed = reverse(word)
    word_list.insert(0, word)
    word_list.append(reversed)
def main():
    words = []
    word = input('Enter a word >')
    while word != 'stop':
        elaborate(words, word)
        word = input('Enter a word >')
    print(words)
main()

word = 'Orange'
word_list = []
my_list = list(word) # makes a list of all the letters in the word
print(my_list)
my_list.reverse() # reverses the list
reverse_string = ''.join(my_list) # joins all in the list
print(reverse_string)
word_list.insert(0, word)
print(word_list)
word_list.append(reverse_string)
print(word_list)

