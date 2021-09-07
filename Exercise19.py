'''
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

input = raw_input("Enter sentence").split(' ')
dict1 = dict()
for i in input:
    if i not in dict1.keys():
        dict1[i]=1
    else:
        dict1[i]+=1
print dict1
print "-----------------------------------"

keys = dict1.keys()
keys.sort()

for key in keys:
    print key, dict1[key]