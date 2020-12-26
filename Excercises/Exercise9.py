#Given two lists with 5 elements each
firstList=[10,11,12,13,14]
secondList=[1,2,3,4,5]

#Print the two lists
print("The first list contains: ",firstList)
print("The second list contains: ",secondList)

#Declare the third list
thirdList=[]

#Find the even numbers from firstList
for num in firstList:
    if (num%2==0):
        thirdList.append(num)


#Find the odd numbers from secondList
for num in secondList:
    if (num%2!=0):
        thirdList.append(num)


#print the result
print("The elements in the Third list are: ",thirdList)