from utils import Exit


def get_pipes():
    '''
    Return the sets of connections for the pipes that connect the valves.
    '''
    return [
        [Exit(0, 1), Exit(1, 3)],
        [Exit(0, 2), Exit(1, 0)],
        [Exit(0, 4), Exit(1, 4)],
        [Exit(1, 3), Exit(1, 5)]
    ]


def get_valves():
    '''
    Return the two interchangeable valves for simple_maze.jpg.
    '''

    return [
        {'name': 'A', 'connection_sets': [[0, 2], [1, 5]]},
        {'name': 'B', 'connection_sets': [[0, 3], [1, 2], [4, 5]]}
    ]


def get_source_entrance():
    return Exit(0, 0)


def get_sprinklers():
    return [
        [Exit(0, 2), Exit(1, 0)],
        [Exit(0, 4), Exit(1, 4)],
        [Exit(1, 3), Exit(1, 5)]
    ]
