num1 = int(input("Enter a digit: "))
num2 = int(input("Enter another digit: "))

print("num1 & num2: ", num1, num2)
print("num1 | num2: ", num1 | num2)
print("num1 ^ num2: ", num1^num2)
print("num1 << num2: ", num1<<num2)
print("num1 >> num2: ", num1>>num2)
print("~num1: ", ~num1)
print("~num2: ", ~num2)

#Program to verify whether user input is odd or even

def isOddorEven(n):
    if (n^1 == n+1):
        return True
    else:
        return False

num = int(input("Enter some number: "))

if isOddorEven(num):
    print(num, 'is even')
else:
    print(num, 'is odd')

#Checking the number of bits of a number

def bitCount(n):
    count = 0
    while(n):
        count += 1
        n >>= 1
    return count

number = int(input("Enter a number: "))
print('Number of bits: ', bitCount(number))



#ACP - Binary Conversion

def binary_convert(n):
    return int(n, 2)
num = input("Enter the binary number: ")
print("The original number is: ", binary_convert(num))