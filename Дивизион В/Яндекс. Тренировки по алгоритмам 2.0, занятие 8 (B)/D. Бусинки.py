import sys
sys.setrecursionlimit(10000)
def read_file():
    with open('input.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i == 0:
                n = int(line)
                binds = [set() for x in range(n + 1)]
                continue
            x, y = map(int, line.split())
            binds[x].add(y)
            binds[y].add(x)
    return n, binds


class Node:
    def __init__(self, n, binds):
        self.n = n
        self.binds = binds
        self.val = 0


class BollsTree:
    def __init__(self, n, binds):
        self.n = n
        self.binds = binds
        self.vals = [0 for x in range(self.n+1)]
        self.ans = 0

    def run(self, root, start=1):
        self.vals[root] = start
        for boll in self.binds[root]:
            if self.vals[boll] == 0:
                self.run(boll, start+1)
        self.ans = max(self.ans, start)

    def clear(self):
        self.vals = [0 for x in range(self.n + 1)]




if __name__ == '__main__':
    n, binds= read_file()
    tree = BollsTree(n, binds)
    for x, ys in enumerate(binds):
        if x == 0:
            continue
        if len(ys) == 1:

            tree.run(x)
        tree.clear()
    print(tree.ans)

