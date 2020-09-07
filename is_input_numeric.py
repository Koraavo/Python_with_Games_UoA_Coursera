print("enter a non negative integer and if the number has integers multiply it "
      "by two else print that the number is not an integer")

number = input("Enter a non-negative integer >")
if str.isdigit(number) == True:
  new_number = int(number)
  multiply = new_number*2
  print(new_number, "* 2 is",multiply )
else:
  print(number, "is not a non-negative integer")
