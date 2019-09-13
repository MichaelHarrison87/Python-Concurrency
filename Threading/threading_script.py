# Use threading 
import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping!')    
    

t1 = threading.Thread(target = do_something)
t2 = threading.Thread(target = do_something)

t1.start()
t2.start()

print('Thread 1 running...')
print('Thread 2 running...')

# Code after start() method keeps running, until it reaches a join() - so it won't continue past this
# without the join, the 'Finished in ....' was printed before each thread has returned 'Done Sleeping!'. 
t1.join()
t2.join()

print('Thread 1 done...')
print('Thread 2 done...')

finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds') # Finished in 1.00 seconds - cf 2.00 seconds in the synchronous