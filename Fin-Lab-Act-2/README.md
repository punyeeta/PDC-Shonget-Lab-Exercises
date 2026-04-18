# Shonget PDC Answers

## Reflection and Analysis
1. Differences observed between sequential and parallel execution 
2. Performance behavior across dataset sizes 
3. Challenges encountered during implementation 
4. Insights about overhead, synchronization, or merging 
5. Situations where parallelism was beneficial or unnecessary

---

### Chiong, Heart
1. Sequential execution is simple and processes data one step at a time with no setup needed. Parallel splits the data across multiple processes running simultaneously, which adds complexity through coordination and synchronization. The biggest takeaway is that parallel does not automatically mean faster, it just means more moving parts.
2. Sequential won every search test by a huge margin, finishing in under 0.013s even on the largest dataset while parallel never went below 0.5s due to process startup costs. For sorting, parallel only started catching up on the large random dataset (2.39s vs 3.15s), showing that parallelism only helps when the workload is actually heavy. Python's built-in sorted() beat both in almost every case.
3. The trickiest part was returning the correct global index in parallel search. Since each worker only sees its own chunk, we had to pass an offset and return offset + i instead of just i. We also had to make sure every process puts something in the Queue even if the result is 1, otherwise the main process would hang waiting forever.
4. Parallel overhead is real and significant. Spawning processes alone cost nearly 2 seconds in some tests, completely burying the actual search time. Merging sorted chunks back together also adds extra work that sequential never deals with. Synchronization using join() and Queue worked correctly but still contributed to the slower runtime overall.
5. For searching, parallelism was unnecessary across all tests since overhead always dominated. For sorting, it only showed a slight benefit on the large random dataset. Parallelism would be worth it for much larger datasets or heavier computations, but for the sizes we tested, sequential was the smarter and faster choice almost every time.

---

### Limpahan, Mark Vincent
1. Sequential execution consistently finished faster than parallel across both sorting and searching tasks, except for larger datasets where parallel sorting could be at advantage.
2. For sorting, the performance gap between sequential and parallel narrowed as dataset size grew. For searching, parallel never caught up regardless of dataset size, since linear search is too lightweight to justify the multiprocessing cost.
3. The main challenge was correctly computing the global index in parallel search, as each worker only knows its local position within its chunk, so the offset had to be added to return the correct position in the original dataset. For sorting, merging the sorted chunks back in the right order required careful handling.
4. Python's multiprocessing has significant startup overhead per process. For short tasks, this overhead dominates total runtime. The Queue in searching and the merge step in sorting both add synchronization cost that sequential execution simply doesn't have.
5. Parallelism showed its only clear benefit in sorting the large random dataset. It was unnecessary for searching entirely, and for small to medium datasets across both tasks, highlighting that parallelism is not always the right tool, problem size and task complexity also matter.

---

### Locsin, Roxanne
1. 
2. 
3. 
4. 
5. 

---

### Sajol, Rhenel Jhon
1. 
2. 
3. 
4. 
5. 

---

### Mag-isa, Jules
1. 
2. 
3. 
4. 
5. 

---
