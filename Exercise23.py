'''Write a function to compute 5/0 and use try/except to catch the exceptions.
Use try/except to catch exceptions.'''

def divisionbyZero():
    return 5/0

try:
    divisionbyZero()
except ZeroDivisionError:
    print "Division by zero"
except Exception,err:
    print "Caught an exception"
finally:
    print "In finally block for cleanup"

'''
Define a custom exception class which takes a string message as attribute.
Hints:
To define a custom exception, we need to define a class inherited from Exception.'''

class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message

myError = MyCustomException("Custom error")

