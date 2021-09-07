#all exercises are from github : https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
list1 =[]
for i in range(2000,3201):
    if i%7 ==0 and i%5!=0:
        list1.append(str(i))
print ','.join(list1)

