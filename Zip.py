'''Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string.'''

import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

print "----------------------------------------------------"
'''Please write a program to print the running time of execution of "1+1" for 100 times.
Hints: Use timeit() function to measure the running time. '''

from timeit import Timer
t = Timer("for i in range(100):1+1").timeit()
print t

print "----------------------------------------------------"

'''Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
Hints: Use list[index] notation to get a element from a list.
'''

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = subjects[i] + verbs[j] + objects[k]

            print sentence

print "----------------------------------------------------"

'''By using list comprehension, please write a program to print the list 
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
Hints: Use list comprehension to delete a bunch of element from a list. 
Use enumerate() to get (index, value) tuple.
'''

list1 = [12,24,35,70,88,120,155]
list2 = []
for (index,value) in enumerate(list1):
    if index%2==0:
        continue
    else:
        list2.append(value)

print list2

print "----------------------------------------------------"

'''With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
Hints: Use set() and "&=" to do set intersection operation.'''

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
list3_intersect = []
set1 = set(list1)
set2 = set(list2)
set3 = set()
set3 = set1.intersection(set2)
list3_intersect = list(set3)
print list3_intersect

print "----------------------------------------------------"

'''####Importnt: With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
Hints: Use set() to store a number of values without duplicate.'''

def remove_duplicate_order_reserved(list_dup):
    new_list1=[]
    set1=set()
    for item in list_dup:
        if item not in set1:
            set1.add(item)
            new_list1.append(item)
    return new_list1

print remove_duplicate_order_reserved([12,24,35,24,88,120,155,88,120,155])

print "----------------------------------------------------"

'''Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2 c,2 b,2 e,1 d,1 g,1 f,1
'''

dict= dict()
input = 'abcdefgabc'
count = 0
for i in input:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]+=1
print dict

print "----------------------------------------------------"

'''Please write a program which prints all permutations of [1,2,3]
Hints: Use itertools.permutations() to get permutations of list.
'''

import itertools
print(list(itertools.permutations([1,2,3])))

print "----------------------------------------------------"

'''Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
Hint: Use for loop to iterate all possible solutions.
'''

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)













