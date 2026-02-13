# Laboratory Activity: Applying Task and Data Parallelism

## Overview

This laboratory activity explores the concepts of Task Parallelism and Data Parallelism using Python's `concurrent.futures` module. The implementation focuses on a simplified payroll system to demonstrate how different concurrency models handle computational tasks.

## Analysis Questions

### 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division
>
> **Answer:**
> [Placeholder: Define Task Parallelism (focus on distinct operations) and Data Parallelism (focus on same operation on multiple data). [cite_start]Explain that Part A used ThreadPoolExecutor for different deductions (Task) and Part B used ProcessPoolExecutor for multiple employees (Data).] [cite: 114]

### 2. Explain how `concurrent.futures` managed execution, including `submit()`, `map()`, and `Future` objects. Discuss the purpose of `with` when creating an Executor
>
> **Answer:**
> [Placeholder: Explain that `submit()` schedules individual tasks and returns a Future, while `map()` applies a function to an iterable. Define `Future` as a proxy for a result that isn't ready yet. [cite_start]Explain that the `with` statement ensures the executor shuts down and frees resources automatically.] [cite: 115, 116]

### 3. Analyze `ThreadPoolExecutor` execution in relation to the GIL and CPU cores. Did true parallelism occur?
>
> **Answer:**
> [Placeholder: Discuss the Global Interpreter Lock (GIL) in Python. [cite_start]Explain that ThreadPoolExecutor is limited by the GIL for CPU-bound tasks, meaning it likely provided concurrency (context switching) rather than true parallelism on multiple cores.] [cite: 117]

### 4. Explain why `ProcessPoolExecutor` enables true parallelism, including memory space separation and GIL behavior
>
> **Answer:**
> [Placeholder: Explain that ProcessPoolExecutor creates separate processes, each with its own Python interpreter and memory space. [cite_start]Since each process has its own GIL, they can run simultaneously on different CPU cores, achieving true parallelism.] [cite: 118]

### 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
>
> **Answer:**
> [Placeholder: Compare the overhead of creating threads vs. processes. For 10,000 CPU-bound tasks (payroll calculations), ProcessPoolExecutor generally scales better due to multicore usage, though it has higher startup overhead. [cite_start]Threading might struggle with the GIL.] [cite: 119]

### 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use
>
> **Answer:**
> [Placeholder: Example: Generating pay slips for a massive corporation.
>
> - **Data Parallelism:** Calculating net pay for 50,000 employees (ProcessPoolExecutor).
> [cite_start]- **Task Parallelism:** Fetching data from a database while simultaneously writing logs or sending emails for a single employee (ThreadPoolExecutor/I/O bound).] [cite: 120]
