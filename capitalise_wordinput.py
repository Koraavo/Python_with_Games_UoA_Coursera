word_list = []
word = input("Enter a word: ")


print("Word is indexed and capitalised")

while word != " ":
    word_list.append(word)
    word = input("Enter a word: ")
print(word_list)

for index in range(0, len(word_list)):
    item = word_list[index]
    word_list[index] = item.upper()
print(word_list)