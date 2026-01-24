contacts=[]

while True:
    print("1 Add contact")
    print("2 List contacts")
    print("3 Search contact by name")
    print("4 Delete contact")
    print("5 Update contact")
    print("6 Exit")
    choice=input("Enter the choice")
    if choice=="1":
        info=input("Enter Name Phone Email")
        info=info.strip()
        name,phone,email= info.split()
        record=[name,phone,email]
        contacts.append(record)
    elif choice=="2":
        for c in range(len(contacts)):
            print(c,contacts[c])   
    elif choice=="3":
        ask=input("Enter the name")
        for c in range(len(contacts)):
            if contacts[c][0]==ask:
                print(contacts[c])
    elif choice=="4":
        ask=input("Enter the index")
        if 0<=int(ask)<len(contacts):
            contacts.pop(int(ask))
        else:
            print("invalid index")
    elif choice=="5":
        ask=input("Enter the index") 
        if 0<=int(ask)<len(contacts):
            update=input("Enter the update")
            update=update.strip()
            name,phone,email= update.split()
            record=[name,phone,email]
            contacts[int(ask)]=record
        else:
            print("invalid index")
                            
    elif choice=="6":
        break
    
     
     