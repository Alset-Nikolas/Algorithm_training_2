def read_file():
    children = dict()
    parents = dict()
    answer = []
    links = dict()
    with open('input.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i == 0:
                n = int(line) -1
                continue

            person, parent = line.split()
            if n > 0:
                if parent not in children:
                    children[parent] = set()
                if parent not in parents:
                    parents[parent] = None
                parents[person] = parent
                children[parent].add(person)
                links[parent] = None
                links[person] = None

                n -= 1
            else:
                answer.append([person, parent])

    root = []
    for per, par in parents.items():
        if par is None:
            root.append(per)
    return n, children, parents, root, answer, links


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.h = 0


class Tree:
    def __init__(self, root_name, parents, children, links):
        self.parents = parents
        self.root_name = root_name
        self.children = children
        self.root = Node(name=self.root_name, parent=None)
        self.links = links
        self.links[self.root_name] = self.root

    def create(self):
        parents = [self.root]
        h = 1
        while len(parents) != 0:
            box = []
            for parent in parents:
                if parent.name in self.children:
                    for ch_name in self.children[parent.name]:
                        new_child = Node(name=ch_name, parent=parent)
                        self.links[ch_name] = new_child
                        new_child.h = h
                        parent.children.append(new_child)
                    box += parent.children
            parents = box
            h += 1

    def pprint(self, node=None):
        node = node or self.root
        for x in node.children:
            self.pprint(x)



def check(person_1, parent_2):
    node = links[person_1]
    p_node = node.parent
    flag = False
    while p_node != None:
        if p_node.name == parent_2:
            return True
        p_node = p_node.parent
    return False

if __name__ == '__main__':
    n, children, parents, roots, answer, links = read_file()
    trees = []
    for root in roots:
        tree=Tree(root_name=root, parents=parents, children=children, links=links)
        tree.create()
        trees.append(tree)
    for q in answer:
        person, parent = q
        if check(parent, person):
            print(1, end=' ')
        elif check(person, parent):
            print(2, end=' ')
        else:
            print(0, end=' ')
