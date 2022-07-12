def read_file():
    children = dict()
    parents = dict()
    answer = []
    links = dict()
    with open('input.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i == 0:
                n = int(line) - 1
                continue

            person, parent = line.split()
            if n > 0:
                if parent not in children:
                    children[parent] = set()
                if person not in children:
                    children[person] = set()
                if parent not in parents:
                    parents[parent] = None
                if person not in parents:
                    parents[person] = None
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
        self.flag = [False, False]


class Tree:
    def __init__(self, root_name, parents, children, links):
        self.parents = parents
        self.root_name = root_name
        self.children = children
        self.root = Node(name=self.root_name, parent=None)
        self.links = links
        self.links[self.root_name] = self.root
        self.H = 0

    def create(self):
        parents = [self.root]
        h = 1
        while len(parents) != 0:
            box = []
            for parent in parents:

                for ch_name in self.children[parent.name]:
                    new_child = Node(name=ch_name, parent=parent)
                    self.links[ch_name] = new_child
                    new_child.h = h
                    parent.children.append(new_child)
                    self.H = max(self.H, h)
                box += parent.children

            parents = box
            h += 1


def draw(person_1, person_2):
    for i, person in enumerate([person_1, person_2]):
        node = links[person]
        node.flag[i] = True
        if all(node.flag):
            return node.name
        p_node = node.parent
        while p_node != None:
            p_node.flag[i] = True
            if all(p_node.flag):
                return p_node.name
            p_node = p_node.parent
    print_tree(links[root])


def clear(person_1, person_2):
    for i, person in enumerate([person_1, person_2]):
        node = links[person]
        node.flag[i] = False
        p_node = node.parent
        while p_node != None:
            p_node.flag[i] = False
            p_node = p_node.parent


def check(person_1, parent_2):
    ans = draw(person_1, parent_2)
    clear(person_1, parent_2)
    return ans


def print_tree(root):
    v = [root]
    while v != []:
        box = []
        for v_i in v:
            if v_i.parent:
                print((v_i.name, v_i.h, v_i.parent.name, v_i.flag), end=' ')
            else:
                print((v_i.name, v_i.parent), end=' ')
            box += v_i.children
        print('-' * 30)
        v = box


if __name__ == '__main__':
    n, children, parents, roots, answer, links = read_file()
    trees = []
    for root in roots:
        tree = Tree(root_name=root, parents=parents, children=children, links=links)
        tree.create()
        # print_tree(links[root])
        trees.append(tree)
    for i, q in enumerate(answer):
        person, parent = q
        ans = check(person, parent)
        print(ans)
