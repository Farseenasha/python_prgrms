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


# list =[]           
# x1 = int(input('enter a number'))
# x2 = int(input('enter a number'))
# x3 = int(input('enter a number'))
# list.append(x1)
# list.append(x2)
# list.append(x3)
# for i in list:
#     i[:-1] = i[:-1] + 1
# print(i)    


# a = input('enter a sentence:')
# b = a.split()
# c = b[-1]
# d = len(c)
# print(d)

# 

# l = [1,2,3,4,5]
# b = 0
# for i in l:
#     b = i
#     b = i+b
# print(b)   
#  


# a = [1,2,3]
# b =[]
# c=[]
# sum = ''
# for i in a:
#     i = str(i)
#     sum= sum+i
# b.append(sum)
# for j in b:
#     j = int(j)
#     j = j+1
#     j = str(j) 
#     for k in j:
#         k = int(k)
#         c.append(k) 
# print(c)  






# for i in range(1,6):
#     for j in range(i):
#         print(i+j,end=" ")
#     print()        



# a = input("enter a word")
# rev = " "
# for i in a:
#     rev = i + rev
# print(rev)    



# a = int(input("enter elements for list"))
# l = []
# list=[]
# for i in range(a):
#     b = int(input("enter elements one by one"))
#     l.append(b)
# print(l)
# tar = int(input("enter target value"))
# for i in l:
#     for j in l:
#         if tar == i+j:
#             x = l.index(i)
#             y = l.index(j)
# list.append(y)
# list.append(x)
# print(list)



# a = int(input("enter elements for list"))
# l = []
# list1=[]
# list2=[]
# for i in range(a):
#     b = int(input("enter elements one by one"))
#     l.append(b)
# print(l)
# for i in l:
#     if i == 0:
#         list1.append(i)
#     if i !=0:
#         list2.append(i)
# print(list2+list1)
            
# a = int(input("enter elements for list"))
# l = []
# list1=[0]
# list2=[]
# n = 0
# for i in range(a):
#     b = int(input("enter elements one by one"))
#     l.append(b)
# print(l)
# for i in l:
#     if i == 0:
#         n = n+1
#         l.remove(i)        
# for j in range(n):
#     l.append(0)
# print(l)
            

        
# a = input("entar a sentence")
# n = int(input("enter how many words needed"))
# word = ''
# splt = a.split()
# z = splt[0:n]
# for i in z:
#     word = word+i+' '
# print(word) 
   


# n = 0
# a = int(input("enter elements for list"))
# l = []
# m = []
# for i in range(a):
#     b = int(input("enter elements one by one"))
#     l.append(b)
# print(l)
# l.sort()
# sl = l[-1]
# for i in range(1,sl+2):
#     if i not in l:
#         m.append(i)
# print(m[0])                    


# dict = {"apple":4,"banana":2,"cherry":5}
# dict2= {}
# s = 0
# word = dict.keys()
# print(word)
# num = dict.values()
# for i in num:
#     if i > s:
#         s = i
# print(s)
# for i in dict:
#     if dict[i] == s:
#         print(i)


# l = [[1,2,3],[4,5,6],[7,8,9]]
# list=[]
# l1=[]
# l2=[]
# l3=[]
# word=0
# for i in l:
#     for j in i:
#         if j == i[0]:
#             l1.append(j)
# list.append(l1[::-1])
# for i in l:
#     for j in i:
#         if j == i[1]:
#             l2.append(j)
# list.append(l2[::-1])            
# for i in l:
#     for j in i:
#         if j == i[2]:
#             l3.append(j) 
# list.append(l3[::-1])
# print(list)                       


# a = input("enter a word:")
# b = "aeiou"
# rev = ""
# l = []
# f = []
# for i in a:
#     if i in b:
#         rev = i + rev
# s = str(rev)
# for i in s:
#     l.append(i)

# for j in a:
#     if j in rev:
#         p = a.index(j)
#         for k in l:
#             a[p] = k
            
#     else:
#         f.append(j)
# print(f)                    
# l[1]=""           

# a = int(input("enter a number"))
# b = str(a)
# l = []
# sum = 0
# lngth=0
# for i in b:
#     l.append(i)     
# for i in l:
#     i = int(i)
#     lngth = lngth + 1
#     s = i**lngth
#     sum = sum+s
# print(sum)
# if sum == a:
#     print(a,"is a disarium number")
# else:
#     print(a,"is not a disarium number")    
        

a = "string"
l= []
for i in a:
    l.append(i)
    print(l)




          

          



            


        


            

   
       
