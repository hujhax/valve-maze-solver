import itertools
import sys

from utils import Exit


def prep_pipes(pipes):
    pipe_hash = {}
    for pipe_set in pipes:
        for pipe_end in pipe_set:
            pipe_hash[pipe_end] = list(set(pipe_set) - set([pipe_end]))

    return pipe_hash


def prep_valves(valves):
    def normalize_valve(valve):
        # prep the connection sets for the card in 'flipped' position
        flip_hash = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}

        def flip_set(connection_set):
            return [flip_hash[connection] for connection in connection_set]

        valve['flip_connection_sets'] = [flip_set(connection_set) for connection_set in valve['connection_sets']]

        # convert the connection sets to (faster but cryptic) 'connection hashes'
        def connection_hash(connection_sets):
            valve_hash = {}
            for connection_set in connection_sets:
                for connector in connection_set:
                    valve_hash[connector] = list(set(connection_set) - set([connector]))
            return valve_hash

        valve['connection_hash'] = connection_hash(valve['connection_sets'])
        valve['flip_connection_hash'] = connection_hash(valve['flip_connection_sets'])
        return valve

    return [normalize_valve(valve) for valve in valves]


def find_active_exits(pipes, valves, source_entrance):
    '''
    Compute the final set of 'active exits' for the given maze.
    '''

    valve_hashes = [valve['flip_connection_hash'] if valve['flip'] else valve['connection_hash']
                    for valve in valves]

    def run_through_valve(entrance):

        exits = valve_hashes[entrance.valve].get(entrance.index, [])
        return [Exit(entrance.valve, exit) for exit in exits]

    def run_through_pipes(entrance):
        return pipes.get(entrance, [])

    old_active_exits = set()
    active_exits = set(run_through_valve(source_entrance))

    while old_active_exits != active_exits:
        new_exits = set()

        for active_exit in (active_exits - old_active_exits):  # only *new* active exits
            valve_entrances = run_through_pipes(active_exit)
            for valve_entrance in valve_entrances:
                valve_exits = run_through_valve(valve_entrance)

                new_exits.update(valve_exits)

        old_active_exits = set(active_exits)  # shallow clone
        active_exits.update(new_exits)

    return active_exits


def hits_sprinklers(sprinklers, exits):
    for sprinkler in sprinklers:
        if not exits & set(sprinkler):
            return False

    return True


def output_solution(valves):
    positions = ['top left', 'top center', 'top right', 'bottom left', 'bottom center', 'bottom right']

    print '=== solution found: ==='
    for valve, position in zip(valves, positions):
        flipped_string = ' (flipped)' if valve['flip'] else ''
        print '{0}: Valve {1}{2}'.format(position, valve['name'], flipped_string)
    print ''

if __name__ == "__main__":

    maze_name = sys.argv[1]
    __import__(maze_name)
    maze = sys.modules[maze_name]

    pipes = prep_pipes(maze.get_pipes())
    master_valve_list = prep_valves(maze.get_valves())
    source_entrance = maze.get_source_entrance()
    sprinklers = maze.get_sprinklers()

    # calculate all possible orderings for the valves
    valve_permutations = itertools.permutations(master_valve_list)

    # calculate all possible flip combos for valves
    flip_combos = list(itertools.product(*([[True, False]]*len(master_valve_list))))

    for valves in valve_permutations:
        for flip_combo in flip_combos:
            for valve, flip in zip(valves, flip_combo):
                valve['flip'] = flip

            all_active_exits = find_active_exits(pipes, valves, source_entrance)

            if hits_sprinklers(sprinklers, all_active_exits):
                output_solution(valves)
