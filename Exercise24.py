'''Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
Hints: Use \w to match letters. '''

import re
emailAddress = raw_input("Enter the email Id")
match = re.search("(\w+)@(\w+)\.(com)",emailAddress)
print match.group(1)
print match.group(2)

'''Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example: If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']'''

import re
words = raw_input("Enter the words")
digits = re.findall("\d+",words)
print digits

'''Print a unicode string "hello world".
Hints:
Use u'strings' format to define unicode string.'''

unicode_string = unicode("Hello World")
print unicode_string

