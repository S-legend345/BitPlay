# a = eval(input("Enter a set: "))
# b = eval(input("Enter another set: "))
# count = 0


# for i in b:
#     if i in a:
#         count += 1

# if count == len(b):
#     print(b, 'is  subset of', a)


#Code for printing all subsets

def subsets(s):
    subsets = [[]]
    for e in s:
        subsets += [current + [e] for current in subsets]
    return subsets

#Example Usage
input_set = [1,2,3]
print("All subsets: ", subsets(input_set))