'''Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.'''

list1 = [1,2,3,4,5,6,7,8,9,10]
even_num = filter(lambda x:x%2==0,list1)
print even_num

print "-------------------------------------------------------"

'''
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
square_num = map(lambda x:x**2,list1)
print square_num

print "-------------------------------------------------------"

'''
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
even_num = filter(lambda x:x%2==0,list1)
square_num = map(lambda x:x**2,even_num)
print square_num

print "-------------------------------------------------------"






