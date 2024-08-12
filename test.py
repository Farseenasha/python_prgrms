#### CUMULATIVE SUM ####

# l = [1,2,3,4,5]     ### 1+2+3+4+5 
# l1 =[]
# b = 0
# for i in l:
#     b = i+b
#     l1.append(b)
# print(l1)  


#### PAIR ELEMENTS WITH  REAR ELEMENT IN MATRIX ROW ####

# l = [[1,2,3],[4,5,6],[7,8,9]] 
# l1=[]
# for i in l :                    ##(len(i) - 1)=2...(loop will stop when it reach on 2nd position)
#     a = []
#     for j in i:
#         if j == i[-1]:
#             break
#         x = str(j)
#         y = str(i[-1])
#         z = x + ' ' + y
#         a.append(z)
#     l1.append(a)
# print(l1)        
        
    
r = 5
for i in range(r):
    for j in range(r):
        if i == 0 or i == r-1:
                print("*",end="")
        if   j == 0 :
            print("*",end="")
        print()



    
      




       