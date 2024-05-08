list = []
def add_vehicles():
    name = input("enter the vehicle name")
    price = int(input("enter the price"))
    wheels = int(input('enter number of wheels'))
    l1 = []
    l1.append(name)
    l1.append(price)
    l1.append(wheels)
    list.append(l1)
    print(list)

def display_vehicles():
   
    while True:
        print("1.Two wheels\n2.Three wheels\n3.four wheels\n4.break")
        y = int(input("select the option"))
        if y == 1 :
            for i in list:
                if i[2] == 2:
                    print(i)
        if y == 2:
            for i in list:
                if i[2] == 3:
                    print(i)
        if y == 3:
            for i in list:
                if i[2] == 4:
                    print(i)
        if y == 4:
            break
        else:
            print("no vehicles")
                                    
    
while True:
    print("1.Add vehicle \n 2.Display vehicle \n 3.Break")
    x = int(input("select an option"))
    if x == 1:
        add_vehicles()
    if x == 2:
        display_vehicles()
    if x == 3:
        break     
            
                    
                       