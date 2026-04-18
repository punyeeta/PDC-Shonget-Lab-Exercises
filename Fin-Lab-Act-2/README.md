# Execution Demo
<img width="1152" height="648" alt="PDC GIF" src="https://github.com/user-attachments/assets/8c44ec7e-0f62-46b2-985d-e844d415bff3" />


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
1. We used Quick Sort because of its efficient O(n log n) performance and its ability to divide tasks, making it suitable for parallelism. From the results, sequential Quick Sort was faster on small and medium datasets due to lower overhead, while parallel Quick Sort performed better on large datasets where the workload justified the extra cost. For searching, sequential linear search consistently outperformed parallel search since the overhead of creating processes was higher than the actual work, especially when the target was found early.
2. As dataset size increased, both sequential and parallel sorting took longer, but sequential Quick Sort remained faster for small and medium datasets, while parallel Quick Sort became slightly better for large datasets. In searching, sequential linear search was always faster across all dataset sizes, showing that increasing input size alone does not guarantee better performance with parallelism, especially for simple operations.
3. The main challenge for me was making the sequential Quick Sort flexible for testing while keeping the code simple, including handling inputs and ensuring safe defaults. I also needed to verify correctness clearly by adding checks like partial outputs and full sorting validation. Managing dataset paths was another issue, as incorrect paths could cause errors during testing.
4. A key insight for this is that performance is not just about the algorithm but also the overhead. In multiprocessing, process creation and synchronization like queues and merging add extra cost. For small tasks, this overhead dominates, for example, parallel search took much longer than sequential. In sorting, parallel only became faster for large datasets where the workload offset the overhead. Overall, efficiency depends on minimizing overhead, not just using parallelism.
5. Parallelism was beneficial for large, computation-heavy tasks like sorting, where it improved performance. However, it was unnecessary for small datasets and simple tasks like linear search, especially when early termination is possible. Overall, sequential methods are better for lightweight tasks, while parallelism is more effective for large workloads with independent computations.

---

### Sajol, Rhenel Jhon
1. Sequential and parallel gave the same correct outputs for sorting, but their speed was different. Sequential was faster for small random (0.002174s vs 0.018173s), medium random (0.206448s vs 0.284572s), small sorted (0.001137s vs 0.068730s), medium sorted (0.123600s vs 0.147476s), and large sorted (1.565447s vs 1.621215s). Parallel only became faster in large random, where it took 2.388788s compared to 3.149599s for sequential.
2. As dataset size increased, sorting runtime also increased. For random data, sequential grew from 0.002174s at 1,000 elements to 3.149599s at 1,000,000 elements, while parallel grew from 0.018173s to 2.388788s. For sorted data, both versions were still affected by size, but sequential remained faster in all three cases.
3. A challenge for me was during my parallel sorting implementation was dividing the dataset correctly across processes and then combining the sorted parts back into one final sorted output. It was also difficult to make sure every worker finished properly and that the parallel version still produced the same correct result as the sequential version. Another challenge was understanding why the parallel version was slower on smaller datasets, since process overhead can outweigh the benefit of splitting the work.
4. The results show overhead is very important in sorting. Synchronization and merging of partitions added extra work, which is why parallel was slower for small and medium datasets like small random, medium random, small sorted, medium sorted, and large sorted. Parallel only improved when the workload was large enough, as shown by large random.
5. Parallelism was beneficial only in large random sorting, where parallel quicksort took 2.388788s versus 3.149599s sequential. It was unnecessary for small random, medium random, small sorted, medium sorted, and large sorted because sequential sorting was still faster in those cases.

---

### Mag-isa, Jules
1. 
2. 
3. 
4. 
5. 

---
