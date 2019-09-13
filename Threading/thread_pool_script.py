# Use thread pool executor, instead of setting up and joining threads manually
import concurrent.futures 
import time

start = time.perf_counter()

def do_something(seconds, index):
    time.sleep(seconds)
    return f'Thread {index}: Slept for {seconds:.2f} seconds!' # return a value, instead of just printing    

# We can use a context manager to manage threads, via the with keyword:
with concurrent.futures.ThreadPoolExecutor() as executor:
    
    # Naive approach to creating and running multiple threads below - i.e. a for loop/listcomp:
    # results = [executor.submit(do_something, i/100, i) for i in range(1, 21)]

    # Instead can use the map() method of executor
    args = ((i/100, i) for i in range(1,21)) # generator expression to generate do_somehting args as a tuple
    results = executor.map(lambda p: do_something(*p), args) # unpack the tuples into do_something's args

    for result in results:
        print(result)

finish = time.perf_counter()
duration = finish - start

print(f'Finished in {duration:.2f} seconds') # Finished in 1.99 seconds