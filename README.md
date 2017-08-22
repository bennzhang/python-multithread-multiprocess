# python-multithread-multiprocess

In python, there are two ways to do parallel computation, `threading` and `multiprocessing`. The main differece is `threading` uses threads that run in the same meory space. While `multiprocessing` uses processes that have sparate memory space. Since threads share the same memory space, some lock mechanism should be applied to protect two or more threads will write to the same memory at the same time. Belows are examples showing how to use both `threading` and `multiprocessing` in python. 

```
$ python -V
Python 2.7.5
```

## Multithreading

`multiThread.py` show an example of threads working with queues. We have a list of system commands `cmd_list` and we want to run all of them in `nThreads` worker threads. When one thread finishes its current work, the thread picks up the next command in the `cmd_list` and continues to run. It ends when all commands in the `cmd_list` finish. `multiThread.py` only shows simplest `sleep` command, you can replace it with any command you need. Run it 

```
$ time python multiThread.py
```

It is a very useful code.  For example, we have a list of urls, we want to grab data from those urls using `curl`. You can build your `cmd_list` like below and run the `multiThread.py` code. 

```
# create the cmd_list
cmd_list=[
   'curl url1',
   'curl url2',
   'curl url3',
   'curl url4',
       .
       .
       .
       .
       .
       .
   'curl urln',
]

```

Example 2. we want to export all data from one big oracle table. We can split the table into multiple partitions based on `id` range and run the `multiThread.py`. Build your `cmd_list` like below.  An exmple of `export_table.sh` is provided too. 

```
# create the cmd_list
cmd_list=[
   './export_table.sh 1 1000000',
   './export_table.sh 1000001 2000000',
   './export_table.sh 2000001 3000000',
   './export_table.sh 3000001 4000000',
   './export_table.sh 4000001 5000000',
   './export_table.sh 5000001 6000000',
   './export_table.sh 6000001 7000000',
   './export_table.sh 7000001 8000000',
   './export_table.sh 8000001 9000000',
   './export_table.sh 9000001 10000000',
                   ...
]

```

## Multiprocessing

`multiProcess.py` shows an example using multip processeses. There are two types of list of numbers. Based on different types, different weights are applied. Return a list of multiplication of number and weights. 

```
$ python multiProcess.py

[('type1', 1, 2), ('type1', 2, 4), ('type1', 3, 6), ('type1', 4, 8), ('type1', 5, 10), ('type1', 6, 12), ('type1', 7, 14), ('type1', 8, 16), ('type1', 9, 18), ('type2', 1, 3), ('type2', 2, 6), ('type2', 3, 9), ('type2', 4, 12), ('type2', 5, 15), ('type2', 6, 18), ('type2', 7, 21), ('type2', 8, 24), ('type2', 9, 27)]
```

