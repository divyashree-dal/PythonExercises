'''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
Hints: Use float() to convert an integer to a float'''

n = int(input("enter the number"))
sum = 0.0
for i in range(1,n+1):
    if n > 0:
        sum+= float(i) / float(i+1)
    else:
        break
print sum


