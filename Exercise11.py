'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

dict1 = {'UPPER CASE': 0, 'LOWERCASE': 0}
input = raw_input("enter the sentence")
for x in input:
    if x.isupper():
        dict1['UPPER CASE']+=1
    elif x.islower():
        dict1['LOWERCASE']+=1
    else:
        continue
print 'UPPER CASE', dict1['UPPER CASE']
print 'LOWER CASE', dict1['LOWERCASE']



