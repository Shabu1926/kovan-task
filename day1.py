"""
#EX2
Name =str(input("What is your name? "))
Clr=str(input("What is your fav color? "))
print(Name +" likes "+ Clr)

#type conversion

#Birth_yr=input('Birth year: ')   provides error due to not mentioning type
birth_yr=int(input('Birth year: ')) #input 2004
age=2024-birth_yr
print(age)  # output 20

#or

birth_yr=input('Birth year: ') #input 2004
print(type(birth_yr))
age=2024-int(birth_yr)
print(type(age))
print(age)  # output 20

#ex3; lbs to kg
pounds=int(input('Enter pounds: '))
kilogram=pounds/2.2046
print(kilogram)

#string

course="Python"
print(course[0])  #P
print(course[-1]) #n
print(course[1:5]) # ytho
print(course[-3:-1]) #ho
print(course[1:])  #ython
print(course[:5])  #pytho
print(course[:]) #python
another=course[:]
print(another) #python
print(course[1:-1]) #ytho


#formated string

fname="John"
lname="Smith"
#msg=fname + ' [' + lname +'] is a coder' #John [Smith] is a coder
msg= f'{fname} [{lname}] is a coder' #John [Smith] is a coder
print(msg)

#String methods

course='Python'
print(len(course)) # 6->length of python
print(course.upper()) # PYTHON
print(course.lower())#python
print(course.find('P')) #return first occurence of index of P
print(course.find('thon')) #returns 2
print(course.replace('thon','thonize'))  #Pythonize

print('thon' in course) #True
print(course.title()) #Python


#Arithmatic operation


x=10
x=x+3 #  x+=3
print(x) #13
x-=5
print(x) #8


#Operator Precedence

x=10+2*3
p rint(x) #  (2*3=6)+10 =16


x=10+3*2**2
print(x)  # 2**2=4 ,4*3=12,12+10=22

x=(2+3)*10-3

print(x)


#Math Fumction

x=2.9
print(round(x)) #3

print(abs(-2.9)) #2.9

import math #importing math func

print(math.ceil(2.9))#3

print(math.floor(2.9))#2

#If Statements ->conditions

#cond in notes

is_hot=None

if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_hot==False:
    print("Its a cold day")
    print("Wear warmer clothes")
else:
    print("Enjoy ur day")
    

#ex 5:
price=1000000
dpay=0
is_goodcredit=True 
if is_goodcredit:
    dpay=price*10/100
else:
    dpay=price*20/100
# if True =100000  if False =200000
print("Down payment: ",int(dpay))#Down payment:  100000
print(f"Down payment: ${dpay}")#Down payment: $100000.0

#Logical operators

has_highincome=True 
has_goodcredit=True 
if has_goodcredit and has_highincome: #both condition must be true
    print("Eligible")
else:
    print("Not Eligible")

has_highincome=True 
has_goodcredit=False   
if has_goodcredit or has_highincome: #atleast one condition must be true
    print("Eligible")
else:
    print("Not Eligible")    

has_highincome=True 
has_goodcredit=True
criminal_record=False
if has_goodcredit and not criminal_record: #not condition should not be satisfied
    print("Eligible")
else:
    print("Not Eligible") # Eligible


#Comparison operator

temp=int(input("Enter temp: "))
if temp>30:
    print("Its hot")
elif temp<10:
    print("Its cold")
else:
    print("Its neither hot nor cold")


#ex6:

name=str(input("enter name: "))
length=len(name)
if length<3:
    print("Name must be greater than 3")
elif length>50:
    print("Name must be lesser than 50")
else:
    print("Name looks good")

#Project :Weigh Convertor



W=int(input('Weight: '))
Kilo_Lbs=str(input('(L)bs or (K)g: '))

if Kilo_Lbs.upper()=='L':
    unit=W*0.45
    print(f"Your weight in kilograms is: {unit}")
else:
    unit=W/0.45
    print(f"Your weight in pounds is: {unit}")


#Loops

num=int(input("Enter num less than 5: "))
while num<=5:
    print("*"*num)
    num=num+1
print("Done") # 4 ****
               #  *****

i=1
while i<=5:
    print("*"*i)
    i=i+1
print("Done") 
*
**
***
****
*****
Done

#Guess game

secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess==secret_number:
        print('You won')
        break
else:
    print("Sorry ,you failed")
 


#Car game
command=""
started=False
while True:
    command=input("> ")
    if command=="start":
        if started:
            print("Car already started!")
        else:
            started=True
            print("Car started...")
    elif command=="stop":
        if not started:
            print("Car is already stopped!")
        
        else:
            Started=False
            print("Car stopped.")
    elif command=="help":
        print('''
             start -to start the car
             stop- to stop the car
             quit-to quit the car 
             ''')  #here  is used to print in the same alignment
    elif command=="quit":
        break
    else:
        print("I dont understand")



#for loops

for item in 'Python' :
    #item -->variable item hold each character of Python in iteration
    print(item)# P y t  h o n (vertically)

for item in ['Mish','john'] :
        print(item)#Mish
               #john

for item in [1,4,3] :
        print(item)#1
                   #4
                   #3
for i in range(10):
        print(i) # print from 0 to 9

for i in range(5,10):
        print(i) # print from 5 to 9

for i in range(1,10,2):
        print(i) # print 1 3 5 7 9


# ex 7:

prices=[10,20,30]
to_pay=0
for i in prices:
    to_pay+=i
print("Total cost:",to_pay)

#nested loop

for x in range(4): #0 1 2 3
    for y in range(3): # 0 1 2
        print(f'({x},{y})')#00 01 02 / 10 11 12 / 20 21 22 / 30 31 32

num=[5,2,5,2,2]
for i in num: #5
    
        print('x'*i)
#xxxxx
#xx
#xxxxx
#xx
#xx
# or
 
num=[5,2,5,2,2]
for i in num: #5 2
    out=" " #0
    for j in range(i): # 0,1,2,3,4 - 0 1
        out+='x'  #0-1-3-6-10 ,0-1
    print(out) # 5 2 
#xxxxx
#xx
#xxxxx
#xx
#xx   
   
#Lists
name=['James','Kala','chasma']
print(name)

#to access elements in list -name
print(name[1])#kala
print(name[0])#James
print(name[-1])#Chasma

#to access values in range in list
print(name[0:2])#['James','Kala']


#ex 9:largest number in the list
num=[10,100,410,60]
max=num[0] #10  100 410 60
for i in num: #10 100 410 60
    if i>max: #10>10 100>10 410>100 60>410
        max=i
 
print(max)  #410

#Matrix

matrix=[
    [1,2,3], #0th row index 0 1 2
    [4,5,6], #1st row index 0 1 2
    [7,8,9]  #2nd row index 0 1 2
]
#to access elements in matrix
print(matrix[0][1]) # 0th row index 1 element -->returns 2

#to update

matrix[0][1]=20
print(matrix[0][1])# returns -->20

#to print all items
for row in matrix: #oth row
    for item in row: #1 2 3
        print(item)

#List methods
num=[1,2,3,5,8]
num.append(20)#added atlast
print(num)
num.insert(0,10)#position,value added at the position
print(num)
num.remove(5)#remove particular element
print(num)
num.pop()#remove last element in the list
print(num)
print(num.index(1))#returns  index of first occurence of 5
num.clear()#delete values in the list
print(num)

nums=[1,2,3,5,8]
#to check   existence of value or char in the list
print(20 in nums) #returns false becox no value 20 is found

#occurence of value
nums.append(1)
print(nums.count(1))

#to sort
nums.sort()
print(nums)

#to reverse
nums.reverse()
print(nums)

#copy nums to num

num=nums.copy()
print(num)

#ex  10:
nums=[1,6,1,7,6]
uniques=[]
for num in nums: #1 6 1 7 6
    if  num not in uniques:#1 6 7
        uniques.append(num)#1 6 7
print(uniques)

#TUPLE
num=(1,2,3,2)
print(num[0])#1
#2 methods index and count
print(num.index(1)) #0
print(num.count(2)) #2

#Unpacking-powerful feature of python
coord=(1,2,3)
#coord[0]*coord[1]*coord[2]
#to us the above in many places of a program
x=coord[0]
y=coord[1]
z=coord[2]
print(y)

x1,y1,z1=coord
print(y1)

#Dictionaries
#key value pairs {Name:'John '}
customer={
    "name":"John",
    "age":30,
    "is_verified":True
    }
print(customer.get("name"))#John
print(customer.get("birthdate"))#None
print(customer.get("birthdate","1 Jan 1982"))#1 Jan 1982

#setting new value for a key
customer["Place"]="California"
print(customer["Place"])#California

#ex11:

digit=(input("Phone: "))#1
dic={"1":"One","2":"Two","3":"Three","4":"four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
out=""
for i in digit:
    out+=dic.get(i)+" " 
print(out)
#Phone: 76435
#Seven Six four Three Five 

#Emoji Convertor

msg=input(">")
wrds=msg.split(" ")#seprate multiple words
emojis={":)":"\U0001F642",":(":"\U0001F612"}
out=" "
for wrd in wrds:
    out+=emojis.get(wrd,wrd)+" " 
print(out)  

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 
#functions
#basic func 
def greet(): # ------ 2
    print("Hello! Welcome") #-------3
# 2 line break after func is important
start=greet()          # -----1
print("Finish")  #-----4

#parameters in func

def greet(name):
    
    print(f"Hello! Welcome {name}") #Hello! Welcome John
    
print("Start")
greet("John")
print("Finish")

#or

def greet():
    name="John"
    print(f"Hello! Welcome {name}") #Hello! Welcome John   #-------3
    
print("Start")# -----1
start=greet()  # ------ 2
print("Finish")  #-----4

#benefit of defining function example
def greet(name):
    
    print(f"Hello! Welcome {name}") #Hello! Welcome John   #-------3  Hello! Welcome Mary ----5
    
print("Start")# -----1
greet("John")# ------ 2
greet("Mary")   #-----4
print("Finish")  #-----6

#2 parameters
def greet(fname,lname):
    
    print(f"Hello! Welcome {fname} {lname}") #Hello! Welcome John Smith
 #-------3  Hello! Welcome Mary Smith  ----5
    
print("Start")# -----1
greet("John","Smith")# ------ 2
greet("Mary","Smith")   #-----4
print("Finish")  #-----

#key arguments(if no lname giving in 2 or 3 it shows error in 3 and 5 due to missing argument
#because they are positional arguments

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx




#stack in ds
stack=[]
#to add
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)   #o/p  [10, 20, 30]

#to delete
stack.pop()
stack.pop()
print(stack) #o/p [10]

#stack empty or not
#stack=[]
#len(stack)==0
#o/p  True

#not stack
#True

#to access the top element in stack
stack=[10,20,30]
r=stack[-1]
print(r)  # o/p 30


stack=[]
def push():
    p=input("Enter the value:")
    stack.append(p)
    print("The element added is :"+p)
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("The element deleted is :"+e)
    
    
while True:
    print("Select the operation 1.push 2.pop")
    Enter=int(input())
    if Enter==1:
        result= push()
        
    elif Enter==2:
        result= pop()
        
    else:
        print("Enter the valid option.")
    print(stack)


# o/p
Select the operation 1.push 2.pop
1
Enter the value:10
The element added is :10
['10']
Select the operation 1.push 2.pop
1
Enter the value:10
The element added is :10
['10', '10']
Select the operation 1.push 2.pop
1
Enter the value:20
The element added is :20
['10', '10', '20']
Select the operation 1.push 2.pop
2
The element deleted is :20
['10', '10']
Select the operation 1.push 2.pop
2
The element deleted is :10
['10']
Select the operation 1.push 2.pop
2
The element deleted is :10
[]
Select the operation 1.push 2.pop
2
Stack is empty
[]
Select the operation 1.push 2.pop


### stack using modules(collections)


import collections
stack=collections.deque()
print(stack)  #o/p deque([])

#to add
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#o/p
deque([])
deque([1, 2, 3])
deque([1, 2])
deque([1])
deque([])

#2. using queue method

import queue
stack=queue.LifoQueue() # can add limit like queue.LifoQueue(3)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack)
stack.get()
print(stack)  #30

#if stack is empty and the stack.get() is used
#use timeout func to reducethe waiting time period

stack.get(timeout=1)
 """
#Queue


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("* ")
    
for i in range(1,11):
    x=i*2
    print(i,"x2=",x)
























