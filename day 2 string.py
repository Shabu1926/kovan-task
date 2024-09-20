'''#1
name="Mark"
age=27
fav_food="Pizza"
#Using these variables, create the following string to introduce yourself:

print(f'"Hi! My name is {name}. I am {age} years old, and my favorite food is {fav_food}."')


#2
cities = ["Amsterdam", "Tokyo", "Rio de Janeiro", "Los Angeles"]
#Starting from this list, create the following string:

print(f'"I would like to visit these cities:{cities}"')

#3
You are asked to create a chatbot at work.

Create a code that asks the user for their full name.
Then it should count the number of letters in their name, ignoring spaces.
Finally,it should greet the user and inform them of the length of their name.
'''
'''
name=input("Enter FullName:")
letter=len(name)
count=0
for i in range(letter):
    if i!=" ":
        count+=1
print(f'Welcome {name}, your name count is {count}')
       
    
#4
Create a function that returns the letter of the alphabet given a numeric index. For example, an index of 1 should return "A", an index of 3 should return "C", and so on.

Numbers beyond the range of the alphabet should return an empty string.

def alpha(n):
    alphabet=('abcdefghijklmnopqrstuvwxyz')
    if n>=1 and n<=26:
        print(alphabet[n-1])
    

number=int(input("Enter num: "))

result=alpha(number)

#5
The data analyst in your company calculated the sales figures from the last quarter:

increase_sales_percent = 12.93720081
revenue_growth_percent = 18.33206078
Using these variables, create the following string:

"Sales in our company went up by 12.94%, and our revenue has grown by 18.33%."


increase_sales_percent = 12.93720081
revenue_growth_percent = 18.33206078
print(f'"Sales in our company went up by {increase_sales_percent:.2f}%, and our revenue has grown by {revenue_growth_percent:.2f}%."')
 
6
Our company has asked us to block all emails that do not come
from our company's domain.This means that all emails not
sent from the "@company.com" domain should be moved to the spam box.
emails = ['john.doe@gmail.com', 'mark.twain@company.com',
'mrwonderful@outlook.com']
create a function that decides whether a given email should be blocked or not.

def efunc(emails):
    for i in emails: 
        if "@company" in i:
            print("not valid")
        else:
            print("valid")
    
    
emails = ['john.doe@gmail.com', 'mark.twain@company.com', 'mrwonderful@outlook.com']
result=efunc(emails)

7.
You are tasked to create a simple password validator. The validation rules are as follows:

Password length of at least 8 characters.
At least one uppercase character.
At least one lowercase character.
At least one "special" character from the following set of characters: "!#$%&*+-.?~".
Create a function that acts as the password validator.

def validator(p):
    length=len(p)
    i=0
    ucount=0
    lcount=0
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    spcl="!#$%&*+-.?~"
    scount=0
    if length>=8:
        for i in p:
            if i in upper:
                ucount+=1
            elif i in lower:
                lcount+=1
            elif i in spcl:
                scount+=1
        if ucount>=1 and lcount>=1 and scount>=1:
            print("valid password") 
            
    else:
        print("enter valid password")
    
password=("Enter password:/n")
valid=validator(password)

  ''' 
## 1
name="Mark"
age=27
fav_food="Pizza"
#Using these variables, create the following string to introduce yourself:



name="Mark"
age=27
fav_food="Pizza"
print(f'"Hi! My name is {name}. I am {age} years old, and my favorite food is {fav_food}."')
#"Hi! My name is Mark. I am 27 years old, and my favorite food is Pizza."






















