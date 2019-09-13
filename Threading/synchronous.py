# Starter script - no concurrency, runs synchronously
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping!')    
    
do_something()
do_something()

finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds') # Finished in 2.00 seconds