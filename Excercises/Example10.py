#Ask the user to enter the elements
#firstList=list(input("Enter the elements seperated by comma: ").split(","))
firstList=("3","6","8")

#Print the firstList
print("The elemnts in first list are: ",firstList)

#Check if the elements in firstList are divisible by 3
print("Elements that are divisible by 3: ")
for num in firstList:
    if (num % 3 == 0):
        print(num)