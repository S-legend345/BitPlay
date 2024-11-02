a = eval(input("Enter a set: "))
b = eval(input("Enter another set: "))
count = 0


for i in b:
    if i in a:
        count += 1

if count == len(b):
    print(b, 'is  subset of', a)


#Code for printing all subsets


def subsets(s):
    subsets = [[]]
    for e in s:
        subsets += [current + [e] for current in subsets]
    return subsets

#Example Usage
input_set = list(input("Enter set elements (in plain form): "))
print("All subsets: ", subsets(input_set))


#FlipBits

def flips(n1,n2):
    flip = 0
    while (n1>0 or n2>0):
        t1 = n1 & 1
        t2 = n2 & 2
        if t1 != t2:
            flip += 1
        n1 >>= 1
        n2 >>= 1
        return flip

n1 = int(input("Enter first number: "))
n2 = int(input("Enter another number: "))
print("Number of flips needed: ", flips(n1,n2))


#ACP - Substrings

s = input("Enter a string: ")
ss = [[]]
for i in s:
    ss += [current + [i] for current in ss]
print(ss, 'is the list of subsets')
