input = raw_input("Enter the csv values")
input = input.split(',')
input.sort()
print ','.join(input)

print "----------------------------------------"

list1 = []
while True:
    s = raw_input("enter the line")
    if s:
        list1.append(s.upper())
    else:
        break

for sentence in list1:
    print sentence

print "----------------------------------------"


