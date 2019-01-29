#Countdown - Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countDown(num):
    for i in range(num,-1,-1):
         print(i)
countDown(100)
# #Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.
def printRet(x,y):
    print(x)
    return y
z=printRet(5,6)
print(z)
# #First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.
def firstPluslen(list):
         sum=list[0]+len(list)
         return sum
x=firstPluslen([1,2,3,4,5])
print(x)
#Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False
def greatersecond(list):
    new_list=[]
    for i in range(0,len(list),1):
        if list[i]>list[1]:
           print(list[i])
           new_list.append(list[i])
    print(new_list)
greatersecond([1,2,3,4,5])


#This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthVal(x,y):
    list=[]
    for val in range(0,x,1):
        list.append(y)
    print(list)
lengthVal(14,7)