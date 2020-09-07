print("input of a word is made into a list and split with a space and new list is capitalised")

words = input("Enter some words >")
list1 = []
new_list = words.split(" ")
print(new_list)
for word in new_list:
    print(word, word.upper())