import utils
from utils import Exit


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

    return utils.create_edge_hash(edge_list)


def get_junctions():
    '''
    Return the junction/valve info for triangle_maze.jpg.
    '''
    dead_end = {'connection_lists': [[]]}
    triangle = {'connection_lists': [[+1], [-1], []]}

    # shallow clones
    return [dict(dead_end), dict(triangle), dict(triangle), dict(dead_end), dict(triangle), dict(dead_end)]


def get_source():
    return Exit(0, 0)


def get_sprinklers():
    return [
        set([Exit(1, 1), Exit(2, 0)]),
        set([Exit(1, 2), Exit(4, 2)])
    ]
