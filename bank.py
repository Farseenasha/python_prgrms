bank = []
def creation():
    account = int(input('enter a/c number'))
    amount = int(input("enter amount"))
    while amount < 1000:
        print("minimum amount is 1000")
        amount = int(input("enter proper amount"))
    name = input("enter name")
    phn = input("enter phone number")
    mail = input("enter mail id")
    b1 = []
    b1.append(account)
    b1.append(amount)
    b1.append(name)
    b1.append(phn)
    b1.append(mail)
    bank.append(b1)
    print(bank)
    
def withdrawal():
    x = int(input("enter a/c number"))
    for i in bank:
        if x == i[0]:
            if i[1] == 1000:
                print("minimum balance required 1000.Can't withdraw amount")    
            if i[1] > 1000:
                withdraw = int(input("enter amount for withdrawal"))
                w = i[1] - withdraw
                if w < 1000:
                    print("a/c balance will be:",w)
                    print("minimum balance required 1000.Can't withdraw amount")
                else:
                    i[1] = w 
                    print("current balance=",i[1])    
                

def deposite():
    y = int(input("enter a/c number"))
    for i in bank:
        if y == i[0] :
            deposite = int(input("enter amout for deposite"))
            i[1] = i[1] + deposite
            print("current balance=",i[1])

while True:
    print("1.creating an account\n2.withdrawal\n3.deposite\n4.break")
    x = int(input("select the option"))
    if x == 1 :
        creation()
    if x == 2 :
        withdrawal()
    if x == 3 :
        deposite()
    if x == 4 :
        break


               

         

