# Threading Notes

Script runs "synchronously" - if it does operations in sequences. There's opportunity here to use concurrency.

Types of task:
* CPU-Bound: making heavy use of the CPU, e.g. number-crunching calculations
* IO-Bound: need to wait for input/output operations to complere, but not making as much use of the CPU. E.g. reading/writing from files on the filesystem, network operations, downloaing data from web.

Threading is most beneficial for IO-bound tasks over CPU-bound, i.e. where we're waiting around for operations to finish.

Multiprocessing is most beneficial for CPU-bound tasks, by running them in parallel.

Threading gives the illusion of having all the threads run the code at the same time - instead, it uses the IO waiting time to move ahead with the script. But code is not actually run simulataneously.

