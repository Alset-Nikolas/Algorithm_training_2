import copy


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


def multi_graf(graf):
    new_graf = copy.deepcopy(graf)
    len_new_graf = 0
    for vertex, edge in graf.items():
        for edge_i in edge:
            if edge_i == vertex:
                new_graf[vertex].remove(vertex)
            if vertex in new_graf[edge_i]:
                new_graf[vertex].remove(edge_i)
        len_new_graf += len( new_graf[vertex])
    return new_graf, len_new_graf


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
