from collections import namedtuple

Exit = namedtuple('NamedTuple', 'junction exit')


def get_edges():
    '''
    Return the exit connections for triangle_maze.jpg.
    '''
    edge_list = [
        [Exit(0, 0), Exit(1, 0)],
        [Exit(1, 1), Exit(2, 0)],
        [Exit(1, 2), Exit(4, 2)],
        [Exit(2, 1), Exit(3, 0)],
        [Exit(2, 2), Exit(4, 0)],
        [Exit(4, 1), Exit(5, 0)]
    ]

    edges = {}
    for edge_pair in edge_list:
        a, b = edge_pair
        edges[a] = b
        edges[b] = a

    return edges


def get_junctions():
    '''
    Return the junction/valve info for triangle_maze.jpg.
    '''
    dead_end = {'connection_lists': [[]], 'spin': 0, 'max_spin': 0}
    triangle = {'connection_lists': [[+1], [-1], []], 'spin': 0, 'max_spin': 2}

    # shallow clones
    return [dict(dead_end), dict(triangle), dict(triangle), dict(dead_end), dict(triangle), dict(dead_end)]


def calculate_flow(edges, junctions, source):
    '''
    Compute the final set of 'active exits' for the given configuration.
    '''
    old_active_exits = set()
    active_exits = set([source])

    while old_active_exits != active_exits:
        new_exits = set()

        for active_exit in active_exits:
            far_end_of_the_edge = edges[active_exit]
            junction_index = far_end_of_the_edge.junction
            junction = junctions[junction_index]
            entrance = far_end_of_the_edge.exit
            num_valves = len(junction['connection_lists'])

            index = (entrance + junction['spin']) % num_valves

            for connection_offset in junction['connection_lists'][index]:
                new_exits.add(Exit(junction_index, (entrance + connection_offset) % num_valves))

        old_active_exits = set(active_exits)  # shallow clone
        active_exits.update(new_exits)

    return active_exits

if __name__ == "__main__":
    edges = get_edges()
    junctions = get_junctions()
    source = Exit(0, 0)

    print calculate_flow(edges, junctions, source)
