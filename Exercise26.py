'''Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n
input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
500 '''

n = int(input("enter the number"))
def func(n):
    if n == 0:
        return 0
    else:
        return func(n-1)+100

print func(5)

''' The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example: If the following n is given as input to the program:
7
Then, the output1 of the program should be:
13
Hints: We can define recursive function in Python.
Then, the output2 of the program should be:
0,1,1,2,3,5,8,13
'''

n = int(input("enter the number"))
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

print fibo(7)
list_fibo =[]
for i in range(0,n+1):
    list_fibo.append(str(fibo(i)))

print ','.join(list_fibo)