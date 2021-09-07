'''Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints:
Consider use yield
'''

def genNumbers(n):
    for i in range(0,n):
        if i%7==0:
            yield i

for j in genNumbers(45):
    print j