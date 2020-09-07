words = ('red', 'purple', 'blue', 'green', 'yellow', 'orange')
target_letter = input('Enter a letter to count >')
count = 0
for word in words:
  for letter in word:
    if letter == target_letter:
      count = count + 1
print(count)