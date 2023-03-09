string1 = "This is a string."
string2 = " This is another string."
print(string1.upper())
d = "qwerty"
ch = d[1:6:2]
print(ch)
# d[2] = 'o'
a = 5
b = 2
c = a / b
print(c)
c = a % b
print(c)
c = a ** b
print(c)
param = "string" + str(15)
print(param)
# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# n3 = float(n1) + float(n2)
# print(n1 + " plus " + n2 + " = {:9.1f}".format(n3))
a = 1 / 3
print("{:7.3f}".format(a))
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))
help(list.insert)
help(list.append)
help(list.remove)
help(list.reverse)
list1[0] = 99
print(list1)
list1.append(25)
print(list1)
list1.insert(2, 25)
print(list1)
list1.remove(25)
print(list1)
list1.pop(2)
print(list1)
list1.reverse()
list1.pop(1)
print(list1)
list1.sort(reverse=True)
print(list1)
list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print(list2)
print(lis)
print(dir(tuple))
help(tuple.index)
help(tuple.count)
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(listseq))
print(listseq)
print(sorted(listseq))
listseq.reverse()
print(listseq)
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D['quantity'])
'''
dp = {}
while True:
    key = input('Input name: ')
    if key == 'stop':
        break
    value = input('Input age: ')

    dp[key] = value
print(dp)
'''
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}
print(rec['name'])
print((rec['name'])['firstname'])
print(rec['job'])
rec['job'].append('director')
print(rec)