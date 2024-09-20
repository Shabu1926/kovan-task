# GUESSIG GAME 
import random
bye=0
crct=0
while True:
    if bye==1:
        break
    elif bye==0:
        print("welcome to guessing game"),
        print(''' BASIC RULES
              1.ONLY ENTER NUMERIC VALUES
              2.NUMBERS VALID FROM 1 TO 100
            ''')
     
        guess_key=random.randrange(1,101)
        print("guess_key is",guess_key)

        print("The guess number is set")
        i=1
        while True: #1
            if crct==1:
                break
            elif crct==0:
                print("Enter ur guess:")
                user_input=int(input())
                if type(user_input)==int: #true
                    print("The input is numeric ..... Proceed")
                    if user_input<=100 and user_input>=1:
                        while i>0: #1
                            
                            if  user_input==guess_key:
                                print("congrats u guessed it")
                                break
                                crct=1
                                
                            elif user_input>guess_key:
                                print("too high")
                                crct=0
                                break
                            else:
                                print("too low")
                                crct=0
                                break
                    else:
                        print("range exceeded.Please enter a number between 1 and 100")
                else:
                    print("Invalid input. Please enter a number")
                    crct=0
    else:
        print("game over")
        bye=1
    
   
 