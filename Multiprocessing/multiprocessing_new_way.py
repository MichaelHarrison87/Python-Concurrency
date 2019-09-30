import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} seconds...')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'

# Use ProcessPoolExecutor

# Can use submit() of a PoolExecutor to run individual tasks (but still concurrently)
with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    results = [executor.submit(do_something, second) for second in seconds]   # list of futures
    
    for f in concurrent.futures.as_completed(results):       # as_completed returns an iterator which yields results as they are completed
        print(f.result())


finish = time.perf_counter()
print(f'Finished in {finish - start:.2f} seconds')