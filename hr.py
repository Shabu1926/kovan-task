i=0
for i in range(10):
    print("enter")
    input1=input()
    if len(input1)>0:
        if input1.isnumeric()==True:
            print(input1)
    else:
        break