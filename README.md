# Laboratory 3 – Applying Task and Data Parallelism using `concurrent.futures`

## Overview

This laboratory activity explores the concepts of Task Parallelism and Data Parallelism using Python's `concurrent.futures` module. The implementation focuses on a simplified payroll system to demonstrate how different concurrency models handle computational tasks.

## Analysis Questions

### 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division
>
> **Answer:**
> Task Parallelism involves executing distinct and independent operations concurrently, which is demonstrated in Part A of the lab where four different deduction functions (SSS, PhilHealth, Pag-IBIG, Tax) run simultaneously for a single employee. In contrast, Data Parallelism involves executing the same operation on multiple data elements at the same time. Part B demonstrates this by running the exact same payroll computation function across a list of five different employees.

### 2. Explain how `concurrent.futures` managed execution, including `submit()`, `map()`, and `Future` objects. Discuss the purpose of `with` when creating an Executor
>
> **Answer:**
> The `concurrent.futures` module manages execution through high-level abstractions. The `submit()` method schedules a specific callable function to run and immediately returns a `Future` object, which acts as a placeholder for a result that hasn't been computed yet. The `map()` method is used to apply a single function to an iterable (like a list) in parallel. The `with` statement is used as a context manager to automatically initialize the Executor and, crucially, ensure it shuts down and frees system resources once the code block finishes.

### 3. Analyze `ThreadPoolExecutor` execution in relation to the GIL and CPU cores. Did true parallelism occur?
>
> **Answer:**
> The `ThreadPoolExecutor` uses thread-based concurrency which shares the same memory space. Due to Python's Global Interpreter Lock (GIL), true parallelism (simultaneous execution on multiple CPU cores) does not occur for CPU-bound tasks like pure math calculations. Instead, the interpreter rapidly switches between threads to provide concurrency. However, since we introduced `time.sleep()` delays to simulate I/O operations, the threads were able to release the GIL and run concurrently, efficiently handling the "waiting" periods.

### 4. Explain why `ProcessPoolExecutor` enables true parallelism, including memory space separation and GIL behavior
>
> **Answer:**
> `ProcessPoolExecutor` enables true parallelism because it creates separate operating system processes for each worker instead of threads. Each process has its own independent memory space and its own instance of the Python interpreter. Because each process has its own private GIL, they do not block each other and can run simultaneously on different CPU cores, making this approach ideal for CPU-intensive tasks.

### 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
>
> **Answer:**
> If the system scales to 10,000 employees, the **Data Parallelism** approach using `ProcessPoolExecutor` scales significantly better. With a massive number of CPU-bound payroll calculations, spreading the work across multiple CPU cores reduces the total processing time effectively. In contrast, using threads for 10,000 CPU-bound tasks would suffer from the GIL bottleneck and the overhead of context switching, likely resulting in slower performance than even a sequential loop.

### 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use
>
> **Answer:**
> in a real-world payroll system for a large corporation, **Data Parallelism** (`ProcessPoolExecutor`) would be used for the month-end batch processing to calculate net salary and tax for thousands of employees simultaneously. **Task Parallelism** (`ThreadPoolExecutor`) would be used for handling individual user requests, such as when an employee logs in; the system can concurrently fetch their profile from a database, log the access, and check for notifications without blocking the user interface
