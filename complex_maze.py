from utils import Exit


def get_pipes():
    '''
    Return the sets of connections for the pipes that connect the valves.
    '''
    return [
        [Exit(0, 2), Exit(0, 4), Exit(3, 2), Exit(3, 4)],
        [Exit(0, 1), Exit(1, 0)],
        [Exit(0, 3), Exit(1, 2)],
        [Exit(0, 5), Exit(4, 1)],
        [Exit(1, 3), Exit(2, 2)],
        [Exit(1, 5), Exit(2, 4)],
        [Exit(2, 0), Exit(2, 5)],
        [Exit(2, 1), Exit(2, 3)],
        [Exit(3, 0), Exit(5, 3)],
        [Exit(3, 3), Exit(4, 0)],
        [Exit(3, 5), Exit(4, 2)],
        [Exit(4, 3), Exit(5, 2)],
        [Exit(4, 4), Exit(5, 5)],
        [Exit(4, 5), Exit(5, 4)],
        [Exit(5, 0), Exit(5, 1)]
    ]


def get_valves():
    '''
    Return the six interchangeable valves for complex_maze.jpg.
    '''

    return [
        {'name': 'A', 'connection_sets': [[0, 2], [1, 5]]},
        {'name': 'B', 'connection_sets': [[0, 3], [1, 2], [4, 5]]},
        {'name': 'C', 'connection_sets': [[0, 2], [1, 4]]},
        {'name': 'D', 'connection_sets': [[0, 1], [2, 3]]},
        {'name': 'E', 'connection_sets': [[0, 1, 3], [2, 5]]},
        {'name': 'F', 'connection_sets': [[1, 2, 3, 5]]},
    ]


def get_source_entrance():
    return Exit(0, 0)


def get_sprinklers():
    return [
        [Exit(2, 0), Exit(2, 5)],
        [Exit(3, 0), Exit(5, 3)],
        [Exit(3, 1)],
        [Exit(3, 3), Exit(4, 0)],
        [Exit(4, 4), Exit(5, 5)]
    ]
