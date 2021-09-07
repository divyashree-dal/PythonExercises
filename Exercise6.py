import math
c = 50
h = 30

x = raw_input("Enter the csv values")
items = x.split(',')
items_calc = []
print items
for i in items:
    items_calc.append(str(int(round(math.sqrt((2 * c * float(i)/h))))))

print ','.join(items_calc)
