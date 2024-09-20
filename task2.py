import threading

def print_square(num):
    t=threading.Thread(target=print_cube,args=(10,))
    t.start()
    t.join()
    print("square:{}".format(num*num))
    
def print_cube(num):
    print("Cube of number is:{}".format(num ** 3))
       

t1=print_square(10)
print("done")
print("\n")  
'''
#deamon thread exits befpre main thread
import threading
import time

# Function to simulate a long-running background task
def background_task():
    while True:
        print("Logging system events in the background...")
        time.sleep(2)

if __name__ == "__main__":
    # Creating a daemon thread
    thread = threading.Thread(target=background_task)
    thread.setDaemon(True)  # Mark the thread as a daemon
    thread.start()

    print("Main program doing some work...")
    time.sleep(5)  # Main thread is busy for 5 seconds

    print("Main program finished.")
'''
print("\n")  

#non-deamon

import threading
import time

# Function to simulate a long-running important task
def important_task():
    print("Starting important task...")
    time.sleep(5)  # Simulating a task that takes 5 seconds
    print("Important task finished.")

if __name__ == "__main__":
    # Creating a non-daemon thread (default behavior)
    thread = threading.Thread(target=important_task)
    thread.start()

    print("Main program doing some work...")
    time.sleep(2)  # Main thread is busy for 2 seconds

    print("Main program finished, waiting for important task to complete.")
    thread.join()  # Main thread waits for the non-daemon thread to complete
