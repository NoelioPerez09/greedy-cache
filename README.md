## Name:
Noelio Perez (77647747)

## Assumptions:
1. You have Python3 installed.
2. `main()` function should cover most edge cases (assuming $k, m \in \mathbb{Z}^{+}$)

## Instructions to Compile:
1. Clone the repository
2. Navigate to project directory
3. Drop an input file in the `input/` directory (optinal since you can use example input files already provided)
4. Navigate back to the project directory and then go to the `src/` directory
5. Run using the following command `python3 cache.py path/to/input_file` (Example: `python3 cache.py ../input/example1.in`)
6. To see the output file, navigate back to the project directory and then go to the `output/` directory


## Question 1: Empirical Comparison

| File/Input | k | m | FIFO | LRU | OPTFF |
| -------- | -------- | -------- | -------- | -------- | -------- |
| File1 | 5 | 100 | 92 | 92 | 72 |
| File2 | 8 | 700 | 597 | 596 | 428 |
| File3 | 2 | 200 | 184 | 183 | 161 |

OPTFF does have the fewest number of misses for all files, due to its optimality. FIFO is generally worst than LRU overall, we can see for these files LRU won twice against FIFO
and only tied once.
Note: All three files I used are provided on the `input/` directory as `example1.in` for File1, `example2.in` for File2, and `example3.in` for File3. Results are in the `output/` directory
as `example1.out`, `example2.out`, and `example3.out` respectively.

## Question 2: Bad Sequence for LRU or FIFO

There does exist exist a $k=3$ sequence for which OPTFF incurs strictly fewer misses than LRU and FIFO (in fact there are an infinite number of them). Example sequence:
    1 2 3 2 3 4 1
Where $k=3$ and $m=7$, running all three algorithms we obtain the following misses:

| File/Input | k | m | FIFO | LRU | OPTFF |
| -------- | -------- | -------- | -------- | -------- | -------- |
| File4 | 3 | 7 | 5 | 5 | 4 |

Note: File4 provided as `example4.in` in `input/` directory and `example4.out` in `output/` as its corresponding output.
The key differentiator in this case between OPTFF and both FIFO and LRU is what to evict when the request with ID of 4 comes in. Since neither FIFO nor LRU have knoweldge of the future, their strategy is to remove the first request that was inserted in the cache (request with ID of 1) and removed the least recently used request (1 since previously it used both requests with ID 2 and 3, and 1 hasn't used it since inserting). However, what they don't expect is that the very next request is for ID of 1, which they have just evicted. OPTFF on the other hand knows this and when the request with ID of 4 comes, it evicts either requests 2 or 3 (it doesn't really matter in this case) since neither of this will be used again after the second request of 3, meaning that it will still have the request with ID of 1 in the cache, therefore leading to a total of only 4 misses (which where inevitable), while both FIFO and LRU had 5 misses each (for which 1 was evitable if you knew the future).

## Question 3: Prove OPTFF is Optimal

- Let $R$ be the list of requests and let it be $R = [r_1, r_2, \dots, r_m]$ for which $r_i$ is the ID of the $i^{th}$ request.
- Let $M_B$ and $M_A$ be the total number of cache misses of Belady’s and $A$ respectively, for which $M_B \ge M_A$
- Suppose that Belady’s and $A$ both make the exact same decisions up to step $q$, for which at step $q$ they make a different decision (if this isn’t the case that means there is no step in which Belady’s and $A$ make a different decision, which entails that they are the same)
- We can see that step $q$ must be a miss and the cache for both must be full (since if it was hit or the cache wasn’t full, there would be nothing to decide on since both algorithms either just move to the next iteration or simply insert the request to cache without evicting anyone since it isn’t full).
- This means then that Belady’s must evict the request that will requested the furthest in the future (or will never be requested again) $r_B$ and $A$ will pick some other request to evict $r_A$ that will be requested before $r_B$. Notice that it is impossible for $r_A$ to be requested at a later time than $r_B$ since if that was the case then that would be the request that will request the furthest in the future and so Belady’s would have picked that one to be evicted. Also, if it will be requested at the same time then either they evicted the same request or they both picked a request that will never be requested again (making them mathematically equivalent since they’re both using the same eviction decision criteria).
- Since this is the case, that means we can swap the eviction decision of  for $r_B$ without increasing $M_A$ since $r_A$ will be requested again sometime in the future (guaranteed 1 extra miss), but $r_B$ will either never be requested again (no miss) or will be requested again but at a later time than $r_A$, (guaranteed 1 extra miss, but at a later time).
- From this it follows that it is mathematically equivalent in terms of minimizing the number of misses to exchange $r_B$ for $r_A$ at step $q$ for $A$, let’s call this algorithm $A’$ which does the same decision up to $q$ as $A$, but at step $q$ it evicts $r_B$ rather than $r_A$.
- Now from $q$, onwards let's consider the behavior of $A$ and $A'$. $A$ evicted $r_A$ at step $q$, which means that $r_B$ remains in the cache of $A$ and $A'$ evicted $r_B$, which means that $r_A$ remains in the cache of $A'$. However, we have showed that $r_A$ is requested before $r_B$, this means that in this instance $A'$ gets a hit (since $r_A$ is in $A'$) but $A$ suffers from a miss, with this free move we can force $A'$ to evict $r_B$ and so now both algorithms are  identical from that point onwards.
- From then on there is only two possibilities, either there are no more differences between Belady’s and $A’$ after $q$ (which would entail that they both have the same number of misses) or there is a another step $q’$ for which they make a different decision.
- If it is the latter, we can do the same thing we did with $A$ and $q$ and exchange the Belady’s decision for $A’$ decision at $q’$, since there was nothing special about $q$ due to it being an arbitrary step that both algorithms differ.
- Since this can be done for all such differences, that means we can swap all different eviction decisions from $A$ that differ from the ones done by Belady’s, without increasing $M_A$ .
- This means that Belady’s is mathematically equivalent in terms of total number of misses $M_B$ to $M_A$ and thus it necessarily follows that $M_B = M_A$ and thus Belady’s is the optimal offline cache eviction algorithm with not a lower number of misses than the optimal, which necessarily entails that Belady’s is an optimal algorithm.
