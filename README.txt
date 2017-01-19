# Valve Maze Solver

## About

This is a Python program for solving a 'valve maze'.

A valve maze is a maze with a number of junctions, each of which has equidistant 'exits' and is operated by a valve.  A valve is a piece that sits in the junction, has the same number of exits, and connects those exits in a particular way -- e.g., if there are three exits, maybe it connects exits 0 and 1, while exit 2 dead-ends.  The puzzle states that a fluid starts at one 'source' exit, and that fluid flows forward from one junction to the next, following the valve connections as appropriate.  The objective is to *rotate* these valves such that the fluid reaches a set of "sprinklers" set in maze connections between particular pairs of exits.

## Usage

Call the solver like this:
```
python maze_solver.py <maze_name>
```

The maze_name should correspond to a file, maze_name.py, that defines the following methods:
* get_edges:
    * This should return a hash of Exits to other Exits, indicating the connections that define the maze.
    * If all the maze's edges are bidirectional -- i.e., none of them are one-way -- you can define a list of maze pairs and use utils.create_edge_hash to generate a hash from that.
* get_junctions:
    * This should return a list of objects, each of which corresponds to a junction -- an intersection with a valve, in the puzzle.
    * These junctions are numbered starting from zero.
    * Each junction has the following fields:
        * connection_lists: look at your valve.  Number its exits clockwise from zero.  connection_lists is a list with an item corresponding to each exit.  The nth list item tells the solver what other exits that nth exit connects to.  It represents this as a list of offsets.  So: if exit 3 is connected to exits 0, 2, and 5, then its list item is [-3,-1,+2].  If exit 2 is a dead end, then its list item is [].
            * Note that a dead end in the maze should be represented as a junction with connection_lists set to [[]].
        * max_spin (optional): The maximum number of times you can rotate this valve before, due to symmetry, it starts repeating yourself.  For instance, if you have a 4-exit valve with a N/S pipe crossing over an E/W pipe, set max_spin to 2.
* get_source:
    * Returns an exit showing where the fluid launches from.
* get_sprinklers:
    * Return where the sprinklers are -- a list of Exit pairs, where each pair comprises the two ends of a pipe where a sprinkler is.

Try to also include a picture of the maze, with numbered junctions, exits, and valves, as <maze_name>.jpg.

When run, the algorithm lists out all the puzzle solutions.  It lists the rotation for each valve (as numbered in get_junctions).  If it lists a rotation of '2', that means to start that valve with its zeroth exit aligned with the junction's zeroth exit, and then rotate it two notches counterclockwise.

## Algorithm

We define an 'active exit' as an exit with fluid coming out of it.  For a given configuration, we start by initializing our set of 'active exits' to just the one exit at the source.  Then, we iterate, letting the fluid flow along one edge, and figuring out which active exits we should add to our set.  Then we add those new ones to our set of our 'active exits'.  We then check to see if our set has stabilized -- no new exits added -- and if not, we reiterate.

The algorithm runs this process for each possible combination of valve rotations, and finally prints the configurations that include the requested 'active edges'.