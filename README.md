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
