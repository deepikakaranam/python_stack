# Basic - Print all the numbers/integers from 0 to 150.
for num in range(0, 151):
    print(num)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for num in range(5, 1000001, 5):
    print(num)
# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for i in range(1, 101):
    print("Coding"*(i % 5 == 0) + "Dojo"*(i % 10 == 0) or i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for num in range(1, 500000, 2):
    sum = sum+num
    print(sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for num in range(2017, 0, -4):
    print(num)


# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult,
# print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexiblecountdown(low_num, high_num, mult):
    for i in range(low_num, high_num+1, 1):
        if i % mult == 0:
            print(i)


flexiblecountdown(2, 9, 3)
