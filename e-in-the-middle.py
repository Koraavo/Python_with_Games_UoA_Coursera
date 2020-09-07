'''
Sample program test required:

Enter a string with an e in the middle >alberta
Yes, alberta has e in the middle, at index 3

Enter a string with an e in the middle >edmontonian
No, edmontonian has t in the middle, at index 5

Enter a string with an e in the middle >keep
No, keep has no middle character

'''
name = input("Enter a string with an e in the middle >")
len1 = len(name)
if len1 % 2 == 1:
    centre = (len1 // 2)
    if name[centre] == 'e':
        print("Yes,", name, "has e in the middle, at index", centre)
    else:
        print('No,', name, "has", name[centre], "in the middle, at index", centre)
else:
    print("No,", name, "has no middle character")

