def power2(number):
    if number <= 0:
        return False
    return (number & (number-1)) == 0

n = int(input("Enter a number: "))
if power2(n):
    print("The number is a power of 2")
else:
    print("The number isn't a power of 2")

def power4(number):
    if number <= 0:
        return False
    while number % 4 == 0:
        number//=4
    return number==1

num = int(input("Enter number: "))
if power4(num):
    print("Is Power")
else:
    print("Isn't Power")

n1 = int(input("Enter a number: "))

if power2(n1) and power4(n1):
    print("Power of 2 and 4")
elif power2(n1) == True and power4(n1) == False:
    print("Power of 2 but not power of 4")
else:
    print("Power of either")
