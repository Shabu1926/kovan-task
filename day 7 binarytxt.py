#write 
import pickle
'''
l=eval(input("enter the list value:"))
d={"A":"apple","B":"banana","C":"cherry"}
x=open("bt.dat","wb")
pickle.dump(l,x)
print("Data Successfully written onto file")
x.close()

#read
x=open("bt.dat","rb")
y=pickle.load(x)
print(y)

#write and read
l=eval(input("enter the list value:"))
x=open("bt.dat","w+b")
pickle.dump(l,x)
print("Data Successfully written onto file")
x.seek(0)
y=pickle.load(x)
print(y)
x.close()

#image  processing
from PIL import Image
img  = Image.open("thread.png")     
print("success")
try: 
    img  = Image.open("thread.png") 
except IOError:
    pass



#Retrieve size of image
from PIL import Image

f = "thread.png"
with Image.open(f) as image:
    width, height = image.size

img = img.rotate(180) 

#from PIL import Image

def main():
    try:
       
        img = Image.open("thread.jpg")
        width, height = img.size
        
        area = (0, 0, width/2, height/2)
        img = img.crop(area)
        
      
       
    except IOError:
        pass

if __name__ == "__main__":
    main()

from PIL import Image

def main():
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open("picture.jpg") 
        
        #Relative Path
        #Image which we want to paste
        img2 = Image.open("picture2.jpg") 
        img.paste(img2, (50, 50))
        
        #Saved in the same relative location
        img.save("pasted_picture.jpg")
        
    except IOError:
        pass

if __name__ == "__main__":
    main()
'''

from PIL import Image

def main():
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open("thread.png") 
        
        #Relative Path
        #Image which we want to paste
        img2 = Image.open("thread2.jpeg") 
        img.paste(img2, (50, 50))
        print("success")
        #Saved in the same relative location
        img.save("pasted_picture.jpg")
        
    except IOError:
        pass

if __name__ == "__main__":
    main()

