from collections import deque, OrderedDict
import math
import sys

def read_requests(filename):
    with open(filename, 'r') as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))
    return k, m, requests

def FIFO(k, m, requests):
    cache = deque()
    items = set()
    misses = 0
    for req in requests:
        if req not in items:
            misses += 1
            if len(cache) < k:
                cache.append(req)
                items.add(req)
            else:
                removed = cache.popleft()
                items.remove(removed)
                cache.append(req)
                items.add(req)
    return misses

def LRU(k, m, requests):
    cache = OrderedDict()
    misses = 0
    for req in requests:
        if req in cache:
            cache.move_to_end(req)
        else:
            misses += 1
            if len(cache) < k:
                cache[req] = 0
            else:
                cache.popitem(last=False)
                cache[req] = 0
    return misses

def OPTFF(k, m, requests):
    next_occur = dict()
    for i, req in enumerate(requests):
        if req not in next_occur:
            next_occur[req] = deque()
        next_occur[req].append(i)
    cache = dict()
    misses = 0
    for req in requests:
        next_occur[req].popleft()
        req_next_index = math.inf
        if len(next_occur[req]) > 0:
            req_next_index = next_occur[req][0]
        if req not in cache:
            misses += 1
            if len(cache) < k:
                cache[req] = req_next_index
            else:
                cache.pop(max(cache, key=cache.get))
                cache[req] = req_next_index
        else:
            cache[req] = req_next_index
    return misses

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments!")
        sys.exit()
    try:
        k, m, requests = read_requests(sys.argv[1])
    except:
        print("Invalid File Structure!")
        sys.exit()
    if k < 1:
        print("Invalid k!")
        sys.exit()
    if m < 1 or len(requests) < 1:
        print("Invalid m or list of requests!")
        sys.exit()
    
    fifo_misses = FIFO(k, m, requests)
    lru_misses = LRU(k, m, requests)
    optff_misses = OPTFF(k, m, requests)
    
    out_name = f'../output/{sys.argv[1].split("/")[-1].split(".")[0]}.out'
    with open(out_name, "w") as file:
        file.write(f'FIFO  : {fifo_misses}\n')
        file.write(f'LRU   : {lru_misses}\n')
        file.write(f'OPTFF : {optff_misses}\n')

    print(f'FIFO  : {fifo_misses}')
    print(f'LRU   : {lru_misses}')
    print(f'OPTFF : {optff_misses}')

if __name__ == "__main__":
    main()