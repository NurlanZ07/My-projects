#Project 1 — Text List Cleaner
#Situation
#We collect short text messages from users. These messages are messy: extra spaces, random uppercase/lowercase, and unwanted words. Before we use them, they must be cleaned and organized.
#Your Job
#Make a program that:
#Lets the user enter several text messages.
#For each message:
#Removes extra spaces at the beginning and end.
#Fixes the letter case in a consistent way.
#Replaces certain unwanted words or parts of words.
#Stores all cleaned messages in a list.
#Lets the user delete any message by giving its number in the list.
#Sorts the final list alphabetically.
#Prints a final summary:
#How many messages were entered.
#How many remain after cleaning and deleting.
#The final cleaned list.
#If the user types something invalid, the program must not crash.
#Result Needed
#A console program that cleans text messages and prints a clear final report.

data=[]
index=[]
i=0
s=0
while True:
    try:
        num_of_sent=int(input("Enter the number of sentences you want to enter: "))
        if num_of_sent>0:
            break
        else:
            print(num_of_sent, "is not a natural number")
            continue
    except ValueError:
        print("The input is not int")


for _ in range(num_of_sent):
    sent=input("Enter the sentence: ").strip().lower()
    index.append(i)
    i+=1
    unwanted=input("Enter the word or the part of a word you want to delete: ").strip().lower()
    unwanted=unwanted.split()
    for delete in unwanted:
        if delete in sent:
            sent=sent.replace(delete,"")
    data.append(sent)
    

my_dict=dict(zip(index, data))   
print(my_dict)
while True:
    try:
        n_of_removs=int(input("Enter the number of sentences you want to remove: ")) 
        if n_of_removs<=0:
           print("The index you enter is not a natural number")
        else:
           break   
    except ValueError:
        print("The input is not int")


for _ in range(n_of_removs):
    try:
        removal=int(input("Enter the index of the sentence you want to remove: "))
        if 0<=removal<len(data):
            new_dict = {k: v for k, v in my_dict.items() if k != removal}
            my_dict=new_dict
            
        else:
            print("There is no entry with such index") 
    except ValueError:
        print("The input is not int")       
            

print("How many messages were entered: ",num_of_sent)
print("How many remain after cleaning and deleting: ",len(my_dict))
print("The final cleaned list: ", my_dict.sort())
