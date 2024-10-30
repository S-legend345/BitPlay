def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    print("New values:", a, b)

def swap2(a,b):
    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After swapping:", a, b)

a = int(input("Enter: "))
b = int(input("Number: "))

swap(a,b)
swap2(a,b)

#Divide without divide

def divide(dividend, divisor):
    sign = (-1 if(dividend<0) ^ (divisor<0) else 1)
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0
    for i in range(31,-1,-1):
        if (temp + (divisor<<i) <= dividend):
            temp += divisor<<i
            quotient |= 1<<i
    if sign==-1:
        quotient = -quotient
    return quotient

a=int(input("Enter dividend: "))
b=int(input("Enter divisor: "))
print("The result of division is: ", divide(a,b))

#Division Floor
def floor(a,b):
    return a//b
print(floor(3,1))