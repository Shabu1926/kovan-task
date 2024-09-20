'''
*
**
***
****
*****
'''
#create a pattern 
num=5

for i in range(0,num+1): #1
    for j in range(i): #5
        print("*",end=" ")
    print("\n")

    
    
f=open("s.txt","r")
x=f.read()
A=x.replace("schedule", "scheduling")
print(A)


f.close()


fil=open("s.txt","w")
y=fil.write(A)


print(y)

