def noofBitZeroes(n):
    zeroes = 0
    ones = 0
    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("Number of ones = ", ones, "\nNumber of zeroes = ", zeroes)

num = int(input("Enter any number: "))
noofBitZeroes(num)

#2

def setOrNot(number, n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n -1)):
            print("Set")
        else:
            print("Not Set")


number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)

#3

def right(n):
    num = bin(n)[2:]
    righmost = num[::-1]
    rightmostn = int(rightmost, 2)
    return rightmostn

n = int(input("Enter a digit: "))
rightmostn = right(n)
print("Originial number: {}".format(n))
print("Reversed Number: {}".format(rightmostn))
