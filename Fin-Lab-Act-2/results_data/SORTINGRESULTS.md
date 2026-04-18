# Sorting Results

## Sequential Quicksort Evaluation

| Dataset | Elements | Execution Time (seconds) | First 5 | Last 5 | Sorted Correctly |
|---|---:|---:|---|---|---|
| small_random.pkl | 1000 | 0.002174 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_random.pkl | 100000 | 0.206448 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_random.pkl | 1000000 | 3.149599 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |
| small_sorted.pkl | 1000 | 0.001137 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_sorted.pkl | 100000 | 0.123600 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_sorted.pkl | 1000000 | 1.565447 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |

## Parallel Quicksort Evaluation

| Dataset | Elements | Execution Time (seconds) | First 5 | Last 5 | Sorted Correctly |
|---|---:|---:|---|---|---|
| small_random.pkl | 1000 | 0.018173 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_random.pkl | 100000 | 0.284572 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_random.pkl | 1000000 | 2.388788 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |
| small_sorted.pkl | 1000 | 0.068730 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_sorted.pkl | 100000 | 0.147476 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_sorted.pkl | 1000000 | 1.621215 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |

## Python Built-in sorted() Baseline

| Dataset | Elements | Execution Time (seconds) | First 5 | Last 5 | Sorted Correctly |
|---|---:|---:|---|---|---|
| small_random.pkl | 1000 | 0.000102 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_random.pkl | 100000 | 0.015629 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_random.pkl | 1000000 | 0.260167 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |
| small_sorted.pkl | 1000 | 0.039895 | [76, 914, 3962, 4665, 4973] | [991860, 994852, 997167, 998052, 999903] | True |
| medium_sorted.pkl | 100000 | 0.000630 | [5, 9, 17, 21, 29] | [999975, 999978, 999980, 999981, 999990] | True |
| large_sorted.pkl | 1000000 | 0.032350 | [3, 3, 8, 9, 11] | [999996, 999997, 999999, 999999, 1000000] | True |

## Results Interpretation

Sequential Quicksort is generally faster than Parallel Quicksort for small and medium datasets because process overhead dominates. Parallel Quicksort only shows an advantage on the large random dataset, where workload is big enough to offset overhead. Python's built-in `sorted()` remains the fastest baseline in nearly all cases.
