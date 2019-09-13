# Use threading 
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping!')    

# Create mutliple threads - below runs do_something 10 times
threads = []    
for _ in range(10):
    t = threading.Thread(target = do_something, args = [2]) # pass arguments as a list of values
    threads.append(t)
    t.start()

# Note: putting the join() method inside the for loop above would effectively run the code synchronously

# Instead we put the join()'s after the creating/starting the threads
for thread in threads:
    thread.join()

finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds') # Finished in 2.00 seconds - ran 10 times, sleeping 2 seconds