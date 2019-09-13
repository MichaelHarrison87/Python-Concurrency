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


# Code below runs the threads in sequence (i.e. synchronously) - as code doesn't run past the join() method
t1.start()
print('Thread 1 running...')
t1.join()
print('Thread 1 done...')

t2.start()
print('Thread 2 running...')
t2.join()
print('Thread 2 done...')


finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds')