import random

def generate_input_file(filename, k, m, max_id):
    with open(filename, 'w') as f:
        f.write(f"{k} {m}\n")
        requests = [str(random.randint(1, max_id)) for _ in range(m)]
        f.write(" ".join(requests) + "\n")

generate_input_file("example2.txt", 8, 700, 60)
