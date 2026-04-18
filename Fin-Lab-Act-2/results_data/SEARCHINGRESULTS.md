*Results Data*

| Dataset | Target | Seq Index | Seq Time | Par Index | Par Time |
|---|---|---|---|---|---|
| small_random.pkl | 4665 | 465 | 0.000037s | 465 | 0.615057s |
| medium_random.pkl | 4665 | 15831 | 0.000560s | 15831 | 1.959237s |
| large_random.pkl | 4665 | 442335 | 0.012810s | 442335 | 1.863798s |
| small_sorted.pkl | 4665 | 3 | 0.000021s | 3 | 0.539038s |
| medium_sorted.pkl | 4665 | 481 | 0.000025s | 481 | 1.716707s |
| large_sorted.pkl | 4665 | 4661 | 0.000149s | 4661 | 1.830332s |

*Results Interpretation*
- Sequential search outperforms parallel search across all datasets. The parallel search's overhead from spawning processes (~0.5–1.9s) far exceeds the actual search time, making it inefficient for datasets of this size. The gap is most evident in the sorted datasets where the target was found very early, meaning sequential search barely did any work while parallel still paid the full process cost.
