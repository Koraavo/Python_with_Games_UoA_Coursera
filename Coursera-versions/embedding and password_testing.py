from random import randint, choice, sample
size = 13
fill = '!@#$%^*()-+=~[]{}'
embedding = ''
split_index = randint(0, size - 7)
for i in range(0, split_index):
    embedding = embedding + choice(fill)

embedding = embedding + password_list[0]

for i in range(split_index+7, 13):
    embedding = embedding + choice(fill)
print(embedding)

password = 'HUNTING'
guess = 'SURVIVE'
list1 = []
for i in range(len(password)):
    if password[i] == input[i]:
        list1.append(input[i])
print(list1)
print(f'{len(list1)}/{len(password)} IN MATCHING POSITIONS')