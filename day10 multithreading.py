
'''
import threading

# Example: Create a simple thread
def print_hello():
    print("Hello from the thread")

thread_1= threading.Thread(target=print_hello)

thread_1.start()
thread_1.join()

print("\n")


#multithreading
#print the square and cube of the number

import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

print("\n")
'''
import threading
import os
import time

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    time.sleep(1)

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":

    print("ID of process running main program: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task1, name='t1')
    t3 = threading.Thread(target=task1, name='t1')
    t4 = threading.Thread(target=task1, name='t1')
    t5 = threading.Thread(target=task1, name='t1')
    t6 = threading.Thread(target=task1, name='t1')
    t7 = threading.Thread(target=task1, name='t1')
    t8 = threading.Thread(target=task1, name='t1')
    t9 = threading.Thread(target=task1, name='t1')
    t10 = threading.Thread(target=task1, name='t1')

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    


print("\n")

import threading 
import time 



def print_squares(thread_name, numbers): 
	
	for number in numbers: 
		print(thread_name, number**2) 
		 
		time.sleep(1) 



thread1 = threading.Thread(target=print_squares, 
						args=("thread1", [1, 2, 3, 4, 5])) 

thread2 = threading.Thread(target=print_squares, 
						args=("thread2", [6, 7, 8, 9, 10])) 

thread3 = threading.Thread(target=print_squares, 
						args=("thread3", [11, 12, 13, 14, 15])) 

thread1.start() 
thread2.start() 
thread3.start() 


thread1.join() 
thread2.join() 
thread3.join() 

#threadpool
'''
import concurrent.futures

def worker():
    print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
'''