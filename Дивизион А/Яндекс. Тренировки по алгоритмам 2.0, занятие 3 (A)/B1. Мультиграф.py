def create_graf(m):
    graf = dict()
    for i in range(m):
        start, end = list(map(int, input().split()))
        if start not in graf:
            graf[start] = set()
        if end not in graf:
            graf[end] = set()
        graf[start].add(end)
    return graf


def add_del(del_dict, vertex, val):
    if vertex not in del_dict:
        del_dict[vertex] = set()
    del_dict[vertex].add(val)


def multi_graf(graf):
    del_dict = dict()
    len_graf = 0
    for vertex, edge in graf.items():
        len_graf += len(edge)
        for edge_i in edge:
            if edge_i == vertex:
                add_del(del_dict, vertex, vertex)
                len_graf -= 1
            if vertex in graf[edge_i] and (
                    (edge_i in del_dict and vertex not in del_dict[edge_i]) or edge_i not in del_dict):
                add_del(del_dict, vertex, edge_i)
                len_graf -= 1
    for vertex, del_sel in del_dict.items():
        graf[vertex] -= del_sel

    return graf, len_graf


def pprint(graf):
    for vertex, edge in graf.items():
        for edge_i in edge:
            print(vertex, edge_i)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    graf = create_graf(m)
    graf_res, m = multi_graf(graf)
    print(n, m)
    pprint(graf_res)
