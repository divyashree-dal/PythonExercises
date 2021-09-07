
dict1 = {}
input = raw_input("enter the sentence")
lcount = 0
dcount = 0
for i in input:
    if i.isdigit():
        dcount+=1
    elif i.isalpha():
        lcount+=1
    else:
        continue
    dict1["LETTERS"] = lcount
    dict1["DIGITS"] = dcount
print dict1
print "LETTERS", dict1["LETTERS"]
print "DIGITS", dict1["DIGITS"]