import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} seconds...')
    time.sleep(seconds)
    print('Done sleeping...')

# Assign tasks to processes
p1 = multiprocessing.Process(target = do_something)
print(p1) # <Process(Process-1, initial)>

# Start 10 processes, then join them all - this runs all 10 in parallel (so runtime is ~1.5 secs)
processes = [multiprocessing.Process(target = do_something, args = (1.5,)) for _ in range(10)]
for process in processes:
    process.start()

for process in processes:
    process.join()


finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds')