# Valve Maze Solver

## About

This is a Python program for solving a 'valve maze'.

The solver has a set of 'valves'.  Each valve has six exits, and connects those exits in a particular way.

The maze is a set of 'pipes' with empty slots for the valves.  The solver must put a valve in each spot.  The valve can be placed either right-side-up or upside-down.

The puzzle states that a fluid starts at one 'source' exit, and that fluid flows forward through the valves and pipes to the next.  The objective is to place your valves such that the fluid reaches a set of "sprinklers" set on particular pipes.

## Usage

Call the solver like this:
```
python maze_solver.py <maze_name>
```

The maze_name should correspond to a file, maze_name.py, that defines the following methods:
* get_pipes:
    * This should return a list of pipes.  Each pipe is a list of Exits, indicating that those exits are all connected by pipes.
        * An Exit is a named tuple -- the first number is the valve index (starting from zero) and the second number is the exit index (0-5).
* get_valves:
    * This should return a list of valves.
    * Each valve should have a name and 'connection_sets' list.
        * Each 'connection set' is a list of of exits that are all connected.
* get_source_entrance:
    * Returns the valve entrance where the fluid starts.
* get_sprinklers:
    * Return a list of pipes (see above) that contain sprinklers.

Try to also include a picture of the maze, with numbered junctions, exits, and valves, as <maze_name>.jpg.

When run, the algorithm lists out all the puzzle solutions.  It lists the ordering of the valves, and whether each one is flipped.

## Algorithm

We define an 'active exit' as an exit with fluid coming out of it.  For a given configuration, we start by initializing our set of 'active exits' to just the one exit at the source.  Then, we iterate, letting the fluid flow along one edge, and figuring out which active exits we should add to our set.  Then we add those new ones to our set of our 'active exits'.  We then check to see if our set has stabilized -- no new exits added -- and if not, we reiterate.

The algorithm runs this process for each possible combination of valve rotations, and finally prints the configurations that include the requested 'sprinklers'.