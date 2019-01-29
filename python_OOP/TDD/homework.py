# reverseList - Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.
def reverselist(arr):

    for i in range(int(len(arr)/2)):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr


reverselist([1, 3, 5])

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').


def isPalindrome(str):
    for x in range(int(len(str)/2)):
        if str[x] == str[len(str)-x-1]:
            return True
        else:
            return False


isPalindrome("racecar")

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().


def coin(num):
    arr = []
    x = int(num/25)
    y = num-(25*x)
    z = int(y/10)
    a = y-(10*z)
    b = int(a/5)
    c = a-(5*b)
    d = int(c/1)
    # print(x)
    # print(z)
    # print(b)
    # print(d)
    # print(z)

    arr.append(x)
    arr.append(z)
    arr.append(b)
    arr.append(d)
    return arr


coin(100)
# Factorial (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


factorial(5)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


recur_fibo(7)
