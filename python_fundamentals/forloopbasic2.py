# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggiesize(arr):
    for i in range(0,len(arr),1):
        if arr[i]< 0:
            arr[i]="big"
    print(arr)
biggiesize([-1, 3, 5, -5])
# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives(arr):
    count=0
    for i in range(0,len(arr),1):
        if arr[i]>0:
            count+=1
    print(count)
    arr.pop()
    arr.append(count)
    print(arr)
countPositives([-1,0,1,1])

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumtotal(arr):
    sum=0
    for i in range(0,len(arr),1):
        sum += arr[i]
    print(sum)
sumtotal([1,2,3,4])

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def Average(arr):
    sum=0
    for i in range(0,len(arr),1):
        sum += arr[i]
    print(sum)
    avg=sum/len(arr)
    print(avg)
Average([1,2,3,4])

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def length(arr):
    print(len(arr))
length([1,2,3,4])
# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def Minimum(arr):
    min=arr[0]
    if len(arr)==0:
        return False
    else:
        for i in range(0,len(arr),1):
            if arr[i]<arr[0]:
                min=arr[i]
        print(min)
Minimum([-1,-2,-3,4])
# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def Maximum(arr):
    max=arr[0]
    if len(arr)==0:
        return False
    else:
        for i in range(0,len(arr),1):
            if arr[i]>arr[0]:
                max=arr[i]
        print(max)
Maximum([-1,-2,-3])

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def UltimateAnalyze(arr):
    sumTotal=0
    min=arr[0]
    max=arr[0]
    print(len(arr))
    for i in range(0,len(arr),1):
        sumTotal += arr[i]
        if arr[i]<arr[0]:
            min=arr[i]
        if arr[i]>arr[0]:
            max=arr[i]        
    print(sumTotal)
    Average=sumTotal/len(arr)
    print(Average)
    print(min)
    print(max)
UltimateAnalyze([1,2,3,4])   

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def ReverseList(arr):
    arr.reverse()
    print(arr)
ReverseList([1,2,3,4])