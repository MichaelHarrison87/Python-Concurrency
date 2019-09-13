# Use threading 
import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping!')    

# Create mutliple threads - below runs do_something 10 times
threads = []    
for _ in range(10):
    t = threading.Thread(target = do_something)
    threads.append(t)
    t.start()

# Note: putting the join() method inside the for loop above would effectively run the code synchronously

# Instead we put the join()'s after the creating/starting the threads
for thread in threads:
    thread.join()

finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds') # Finished in 1.01 seconds - 1sec, even tho we ran do_something 10 times