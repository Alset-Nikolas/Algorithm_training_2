class Node:
    def __init__(self, val, h):
        self.val = val
        self.l = None
        self.r = None
        self.h = h

    def __str__(self):
        return "." * self.h + str(self.val)


class BinaryTree:
    def __init__(self):
        self.n = 0
        self.root = None
        self.flag_create = False

    def create(self, val):
        self.root = Node(val, h=0)
        self.n += 1
        self.flag_create = True

    def add(self, val, node_x=None, h=0):

        if not self.flag_create:
            self.create(val)
            return True
        res = True
        node_x = node_x or self.root
        if node_x.val > val:
            if node_x.l is None:
                node_x.l = Node(val, h=h+1)
            else:
                res = self.add(val, node_x.l, h=h+1)
        elif node_x.val == val:
            return  False
        elif node_x.val < val:
            if node_x.r is None:
                node_x.r = Node(val, h=h+1)
            else:
                res = self.add(val, node_x.r, h=h+1)
        return res

    def search(self, val, node_x=None):
        if not self.flag_create:
            return False
        node_x = node_x or self.root
        if node_x.val > val:
            if node_x.l is None:
                return False
            else:
                res = self.search(val, node_x.l)
        elif node_x.val == val:
            return True
        elif node_x.val < val:
            if node_x.r is None:
                return False
            else:
                res = self.search(val, node_x.r)
        return res

    def print(self, node_x=None):
        if self.flag_create:
            node_x = node_x or self.root
            if node_x.l:
                self.print(node_x.l)
            print(node_x)
            if node_x.r:
                self.print(node_x.r)


if __name__ == '__main__':
    tree = BinaryTree()
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            if len(words) == 1:
                tree.print()
            else:
                key, val = words
                val = int(val)
                if key == 'ADD':
                    if tree.add(val):
                        print('DONE')
                    else:
                        print('ALREADY')
                elif key == 'SEARCH':
                    if tree.search(val):
                        print('YES')
                    else:
                        print('NO')
