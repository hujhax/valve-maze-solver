import itertools
import sys

from utils import Exit


def prep_junctions(junctions):
    def add_defaults(j):
        j['spin'] = 0
        j.setdefault('max_spin', len(j['connection_lists']))
        return j

    return [add_defaults(j) for j in junctions]


def calculate_flow(edges, junctions, source):
    '''
    Compute the final set of 'active exits' for the given configuration.
    '''
    old_active_exits = set()
    active_exits = set([source])

    while old_active_exits != active_exits:
        new_exits = set()

        for active_exit in (active_exits - old_active_exits):  # new active exits
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


def hits_sprinklers(sprinklers, exits):
    for sprinkler in sprinklers:
        if not exits & set(sprinkler):
            return False

    return True


if __name__ == "__main__":
    maze_name = sys.argv[1]
    __import__(maze_name)
    maze = sys.modules[maze_name]

    edges = maze.get_edges()
    junctions = prep_junctions(maze.get_junctions())
    source = maze.get_source()
    sprinklers = maze.get_sprinklers()

    # calculate all possible rotation combos for valves
    rotation_lists = [range(junction['max_spin']) for junction in junctions]

    rotations = list(itertools.product(*rotation_lists))

    for rotation in rotations:
        for spin, junction in zip(rotation, junctions):
            junction['spin'] = spin

        exits = calculate_flow(edges, junctions, source)

        if hits_sprinklers(sprinklers, exits):
            print "Rotation {0}: exits = {1}".format(rotation, exits)
