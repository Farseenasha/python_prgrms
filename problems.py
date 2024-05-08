# l =[]
# l1 = int(input("enter 1st number"))
# l2 = int(input("enter 1st number"))
# l3 = int(input("enter 1st number"))
# l4 = int(input("enter 1st number"))
# l.append(l1)
# l.append(l2)
# l.append(l3)
# l.append(l4)
# print(l)
# lst = []
# for i in range(1,100):
#     lst.append(i)
# x = int(input("enter a number"))

# if x in l :
#     y = l.index(x)
#     print(y)
# else :
#     a = lst.index(x)
#     print(a)


list =[]           
x1 = int(input('enter a number'))
x2 = int(input('enter a number'))
x3 = int(input('enter a number'))
list.append(x1)
list.append(x2)
list.append(x3)
for i in list:
    i[:-1] = i[:-1] + 1
print(i)    

