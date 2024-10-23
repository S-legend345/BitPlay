#Check if Equal
def CheckifEqual(n1,n2):
    if ((n1 ^ n2)!=0):
        print("Numbers aren't equal")
    else:
        print("Numbers are equal")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another: "))
CheckifEqual(n1,n2)

#Odd Occuring

def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n -= 1
print("Odd occuring number is: ", OddOccuring(arr))

#TwoOdd

def TwoOdd(arr,size):
    xorof2 = arr[0]
    x = 0
    y = 0
    SetBit = 0
    for i in range(1,size):

        xorof2 = xorof2 ^ arr[i]
    SetBit = xorof2 & ~(xorof2-1)
    for i in range(size):
        if(arr[i]&SetBit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("TwoOddElements are",x,',',y)

arr = []
arr_size = int(input("Enter the size of the array: "))
for i in range(0,arr_size):
    z = int(input("Enter array elements: "))
    arr.append(z)

TwoOdd(arr,arr_size)


#After Class Project - Write a Program to reverse all bits present in a number and print a newly formed number.

def reverseNum(n):
    binaryNum = bin(n)[2:]
    revBin = binaryNum[::-1]
    return int(revBin, 2)
n = int(input("Enter a number: "))
print("It's binary reverse is: ", reverseNum(n))
