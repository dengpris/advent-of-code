from collections import defaultdict, deque
from functools import lru_cache

class Graph:
    def __init__(self, arr):
        self.graph = self.build(arr)

    def build(self, arr):
        graph = defaultdict(str)
        for inp, outp in arr:
            graph[inp] = outp
        return graph

    def find_paths(self, start, end):
        out = 0
        q = deque([start])
        while len(q):
            curr = q.popleft()
            if curr == end:
                out += 1
                continue
            for neighbour in self.graph[curr]:
                q.append(neighbour)
        return out
    
    def find_paths_must_contain(self, start, end, required):
        # Using DFS for performance
        @lru_cache(None)
        def dfs(node, has_req):
            if node == end:
                if all(x == 1 for x in has_req):
                    return 1
                return 0

            if not self.graph[node]:
                return 0
            
            req_list = list(has_req)
            for idx, req in enumerate(required):
                if node == req:
                    req_list[idx] = 1
                
            total_paths = 0
            for neighbour in self.graph[node]:
                total_paths += dfs(neighbour, tuple(req_list))
            
            return total_paths
        
        return dfs(start, (0,) * len(required))

def day11(filepath, part2=False):
    arr = []
    with open(filepath) as f:
        for line in f:
            inp, outp = line.split(':')
            arr.append([inp, outp.split()])
    g = Graph(arr)

    if part2:
        return g.find_paths_must_contain('svr', 'out', ['dac', 'fft'])
    return g.find_paths('you', 'out')


print(day11('input'))
print(day11('input_sample', part2=True))
        