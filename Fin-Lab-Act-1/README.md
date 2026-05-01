# Shonget PDC Answers

## Reflection Questions

Provide written answers to the following questions: 
1. How did you distribute orders among worker processes? 
2. What happens if there are more orders than workers? 
3. How did processing delays affect the order completion? 
4. How did you implement shared memory, and where was it initialized? 
5. What issues occurred when multiple workers wrote to shared memory simultaneously? 
6. How did you ensure consistent results when using multiple processes? 

---

### Chiong, Heart
1. Round-robin method was the method we used to distribute the orders through the workers, where tasks are assigned one by one to each worker in order, then repeated.
2. If there are more orders than workers, some workers just handle multiple orders. All workers still run at the same time, so processing continues efficiently and balanced.
3. The delays made the finishing order random. Even if tasks were given in sequence, they didn’t finish in the same order because of different processing times.
4. We used a Manager to create a shared list that all processes can access. It was set up in the main process before the workers started.
5. When workers wrote at the same time, it caused conflicts in the shared data. Some outputs got messy or out of order.
6. To fix that, we added a lock so only one worker can write at a time, which kept the results correct and consistent.

---

### Limpahan, Mark Vincent
1. 
2. 
3. 
4. 
5. 
6. 

---

### Locsin, Roxanne
1. We used a round-robin approach to distribute the orders evenly across workers. Each order is assigned one by one, and once all workers receive an order, the assignment cycles back to the first worker. This ensures that the workload is balanced and no single worker is overloaded.
2. If there are more orders than workers, some workers simply receive more tasks, but the distribution remains balanced overall. Each worker processes its assigned orders sequentially, while all workers run concurrently. The system still works efficiently since no worker blocks others, and the master waits for all results before finishing.
3. Processing delays made the completion order non-deterministic. Since all workers run in parallel and each task includes a delay, the order in which tasks finish depends on timing rather than assignment. As a result, the output order can vary in each run even though the processing itself is correct.
4. We implemented shared memory using a Manager, which maintains a shared list accessible by all processes. This shared structure is initialized by the master process and managed in a separate process. Workers connect to it and update the shared list, allowing all results to be stored in a centralized location.
5. When multiple workers wrote to shared memory at the same time, race conditions occurred. This led to inconsistent outputs such as unordered or missing entries because there was no control over simultaneous access. As a result, the output became unpredictable across different runs.
6. We ensured consistency by using a lock to control access to the shared memory. Only one worker can write at a time, preventing conflicts and ensuring correct results. This made the final output stable, complete, and consistent in every execution.

---

### Sajol, Rhenel Jhon
1. 
2. 
3. 
4. 
5. 
6. 

---

### Mag-isa, Jules
1. Here, we used the round-robin approach, where each task for the workers happens one at a time, then repeated until all of them got their tasks completed.  
2. Though some orders are more than workers, there are some of those that run sequentially, and the rest are run concturrently. But good news is that the distribution still remains balanced. That's because no other blocks the others, and the master waits for them to finish.
3. The order completion (thanks to processing delays) will result in random orders for the workers. Which means that they did not get the desired order due to different processing times, even if they're given a sequence of orders.
4. We used Manager for implementing the shared memory for all processes to have the same list. This is initialized by the master process and it is managed by a seprate class. Thanks to a entralized location, workers can access connection and updates with the shared list, where all results can be stored there.
5. For the issues with simultaneous writing to shared memory from workers, we have race conditions; due to the fact that some of them have no orders, while others have missing ones, making the results inconsistent and messy to look at.
6. To make a remedy for inconsistent results in using multiple processes, we used a lock to control access to the shared memory. This allows a worker to access one at a time, making the results consistent, clean, and organized.

---
