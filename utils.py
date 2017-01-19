from collections import namedtuple

Exit = namedtuple('NamedTuple', 'junction exit')


def create_edge_hash(edge_list):
    edges = {}
    for edge_pair in edge_list:
        a, b = edge_pair
        edges[a] = b
        edges[b] = a
    return edges
