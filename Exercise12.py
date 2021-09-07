'''Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

import math
a = int(input("Enter the number"))
n1 = int(a)
n2 = int(str(a) + str(a))
n3 = int(str(a) + str(a) + str(a))
n4 = int(str(a) + str(a) + str(a) + str(a))

print n1+n2+n3+n4