habits=[]
while True:
     print("1 Add habit ")
     print("2 List habits ")
     print("3 Mark habit completed ")
     print("4 Show statistics ")
     print("5 Delete habit ")
     print("6 Exit ")
     
     choice = input("Enter your choice ")
     if choice=="1":
         nameh = input("Enter the habit ").strip()
         record = [nameh,0]
         habits.append(record)
     elif choice =="2":
         for h in range(len(habits)):
             print(h,habits[h][0]," - completed ",habits[h][1]," times")
     elif choice == "3":
         ask = int(input("Enter the index "))
         if 0<=ask<len(habits):
             habits[ask][1]+=1
         else:
             print("There is no entry which has that index")
     elif choice =="4":
         if len(habits)==0:
             print("No habits yet")
             continue 
         else:    
             print("Total habits count is ",len(habits))
             s=0
             maximum = habits[0][1]
             for h in range(len(habits)):
                 s+=habits[h][1]
                 if habits[h][1] > maximum:
                     maximum = habits[h][1]
             print("Sum of all completions is ",s)        
             for h in range(len(habits)):
                 if habits[h][1] == maximum:
                     print(h,habits[h][0]," - completed",habits[h][1]," times")
     elif choice=="5":
             ask=int(input("Enter the index "))
             if 0<=ask<len(habits):
                 habits.pop(ask)      
             else:
                 print("There is no entry which has that index")     
     elif choice=="6":
         break
     else:
         print("there is no option like that")    