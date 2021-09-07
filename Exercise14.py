'''Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

list_transactions = []

while True:
    transactions = raw_input("enter deposit with amount")
    if transactions:
        list_transactions.append(transactions)
    else:
        break

print list_transactions

dict= {'D':0,'W':0}
deposit_amount =0
withdrawal_amount = 0
net_amount = 0
for value in list_transactions:
    value_split = value.split(' ')
    print value_split
    if 'D' in value:
        dict['D']+=int(value_split[1])
    elif 'W' in value:
        dict['W']+=int(value_split[1])
    else:
        continue

net_amount += dict['D'] - dict['W']

print net_amount