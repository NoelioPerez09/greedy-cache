Name:
    Noelio Perez (77647747)

Instructions to Compile **Python3 required to run**:
    1. Clone the repository
    2. Navigate to project directory
    3. Drop an input file in the `input/` directory (optinal since you can use example input files already provided)
    4. Navigate back to the project directory and then go to the `src/` directory
    5. Run using the following command `python3 cache.py path/to/input_file` (Example: `python3 cache.py ../input/example1.in`)
    6. To see the output file, navigate back to the project directory and then go to the `output/` directory

Assumptions:
    1. You have Python3 installed.
    2. Main function should cover most edge cases (assuming $k, m \in \mathbb{Z}$)

## Question 1: Empirical Comparison

| File/Input | k | m | FIFO | LRU | OPTFF |
| -------- | -------- | -------- | -------- | -------- | -------- |
| File1 | 5 | 100 | 92 | 92 | 72 |
| File2 | 8 | 700 | 597 | 596 | 428 |
| File3 | 2 | 200 | 184 | 183 | 161 |

