#Custom function to calculate the Sum
def calculateSum(numbers):
    sum=0
    for number in numbers:
        sum += number
    return sum
    
   

#Declare the list
numberList=[10,20,30,40]

#Call the function calculateSum with numbers as a argument
result=calculateSum(numberList)

#Print the result
print(result)           

