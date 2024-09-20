#open fruit.txt file

f = open("fruits.txt","a")

#The above code will throw an error because the file does not exist.
#read the file
#content=f.read()
#print(content)
#print(f.read())
#to write
#w=f.write()
f.write("\napple") 
#print(f) #error cannot write
f.write(" grapes")

f.close()
f = open("fruits.txt","r+")
print(f.read())
#print(f.readline())#read line by line

'''
w-write
r- read
a-append
r+ read after write'''

