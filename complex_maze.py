import utils
from utils import Exit


def get_edges():
    '''
    Return the exit connections for triangle_maze.jpg.
    '''
    edge_list = [
        [Exit(0, 0), Exit(1, 0)],
        [Exit(1, 1), Exit(8, 1)],
        [Exit(1, 2), Exit(4, 0)],
        [Exit(1, 3), Exit(3, 1)],
        [Exit(2, 0), Exit(3, 0)],
        [Exit(3, 2), Exit(6, 0)],
        [Exit(4, 1), Exit(5, 2)],
        [Exit(4, 2), Exit(5, 1)],
        [Exit(4, 3), Exit(5, 0)],
        [Exit(4, 4), Exit(6, 1)],
        [Exit(5, 3), Exit(7, 1)],
        [Exit(6, 2), Exit(7, 0)],
        [Exit(6, 3), Exit(7, 3)],
        [Exit(6, 4), Exit(8, 2)],
        [Exit(7, 2), Exit(8, 0)]
    ]

    return utils.create_edge_hash(edge_list)


def get_junctions():
    '''
    Return the junction/valve info for complex_maze.jpg.
    '''
    dead_end = {'connection_lists': [[]]}
    triangle = {'connection_lists': [[+1], [-1], []]}

    return [
        dict(dead_end),  # shallow clones
        {'connection_lists': [[+2], [+2], [-2], [-2]], 'max_spin': 1},
        dict(dead_end),
        dict(triangle),
        {'connection_lists': [[+1], [-1], [+1, +2], [+1, -1], [-1, -2]]},
        {'connection_lists': [[+1], [-1], [+1], [-1]], 'max_spin': 2},
        {'connection_lists': [[], [], [+2], [], [-2]]},
        {'connection_lists': [[+2], [], [-2], []], 'max_spin': 2},
        dict(triangle)
    ]


def get_source():
    return Exit(2, 0)


def get_sprinklers():
    return [
        [Exit(0, 0), Exit(1, 0)],
        [Exit(1, 1), Exit(8, 1)],
        [Exit(1, 2), Exit(4, 0)],
        [Exit(1, 3), Exit(3, 1)],
        [Exit(4, 1), Exit(5, 2)],
        [Exit(4, 2), Exit(5, 1)],
        [Exit(4, 3), Exit(5, 0)],
        [Exit(4, 4), Exit(6, 1)],
        [Exit(5, 3), Exit(7, 1)],
        [Exit(6, 3), Exit(7, 3)],
        [Exit(6, 4), Exit(8, 2)]
    ]
