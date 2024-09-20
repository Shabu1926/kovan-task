'''import schedule
import time


def print_message():
    print("Task executed at:", time.strftime("%H:%M:%S"))


# Schedule task to run every 5 seconds
schedule.every(1).seconds.do(print_message)

# Keep the program running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
    



# Schedule Library imported
import schedule
import time
 
# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")
 
def good_luck():
    print("Good Luck for Test")
 
def work():
    print("Study and work hard")
 
def bedtime():
    print("It is bed time go rest")
     
def geeks():
    print("Shaurya says Geeksforgeeks")
 
# Task scheduling
# After every 10mins geeks() is called. 
schedule.every(10).minutes.do(geeks)
 
# After every hour geeks() is called.
schedule.every(1).hour.do(geeks)
 
# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("12:00").do(bedtime)
 
# After every 5 to 10mins in between run work()
schedule.every(5).to(10).seconds.do(work)
 
# Every monday good_luck() is called
#schedule.every().monday.do(good_luck)
 
# Every tuesday at 18:00 sudo_placement() is called
#schedule.every().tuesday.at("18:00").do(sudo_placement)
 
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
  

#schedule at specific time
import schedule
import time

# Define a function to print a message


def print_message():
    print("Hello! It's time to code on GFG")


# Schedule the task to run every day at 7:00 AM
schedule.every().day.at("15:44").do(print_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    


#Schedule Task at Intervals

import schedule
import time


def print_message():
    print("Task executed at:", time.strftime("%H:%M:%S"))


# Schedule task to run every 5 seconds
schedule.every(5).seconds.do(print_message)

# Keep the program running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
    
#Python Automated Email Scheduler
''' 
import schedule
import time

# Define a function to send email
def send_email():
    print("Email sent at:", time.strftime("%H:%M:%S"))

# Schedule the task to run every day at 11:53 pm
schedule.every().at(11.53).do(send_email)

# Keep the program running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
    


    
schedule.every().wednesday.at(10.00).do()

