

input = raw_input("enter the binary numbers")
input = input.split(',')
list1 = []
for x in input:
    xd = int(x,2)
    if not xd%5:
        list1.append(x)

print ','.join(list1)

