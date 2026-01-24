data=[]
while True:
    text=input("Enter the text: ").strip().lower()
    words=text.split()
    
    for w in words:
        s=False
        record=[w,0]
        if len(data)>0:
            for d in range(len(data)):
                if record == data[d]:
                    if s==False:
                        data[d][1]+=1
                        s=True
                    else:
                        break    
                else:
                    
                    data.append(record)
                    break   
                    
                    
        else:
            data.append(record)
    print(data)    
             
    