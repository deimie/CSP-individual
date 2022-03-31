# defines num1 and num2 based on user input
num1 = input('Input first number: ')
num2 = input('Input second number: ')

# makes a list with num1 and num2 and sorts it by least to greatest
myList = [num1, num2]
myList.sort()

# prints the 0th and 1st index of the list, which is now sorted
print(myList[0] + ', ' + myList[1])