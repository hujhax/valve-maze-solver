**Valve Maze Solver**

This is a Python program for solving a 'valve maze'.

A valve maze is a maze with a number of junctions, each of which has equidistant 'exits' and is operated by a valve.  A valve is a piece that sits in the junction, has the same number of exits, and connects those exits in a particular way -- e.g., if there are three exits, maybe it connects exits 0 and 1, while exit 2 dead-ends.  The puzzle states that a fluid starts at one 'source' exit, and that fluid flows forward from one junction to the next, following the valve connections as appropriate.  The objective is to *rotate* these valves such that the fluid reaches a set of "sprinklers" set in maze connections between particular pairs of exits.

To use the solver, we need to set up data structres for the 'edges' (the maze connections between exit), the 'valves' (what connects to what at each junction), and the 'sprinklers' (edges that must be hit with fluid for the puzzle to be solved).

We define an 'active exit' as an exit with fluid coming out of it.  For a given configuration, we start by initializing our set of 'active exits' to just the one exit at the source.  Then, we iterate, letting the fluid flow along one edge, and figuring out which active exits we should add to our set.  Then we add those new ones to our set of our 'active exits'.  We then check to see if our set has stabilized -- no new exits added -- and if not, we reiterate.

The algorithm runs this process for each possible combination of valve rotations, and finally prints the configurations that include the requested 'active edges'.

Currently all the data structures are hard-coded, so we call the solver just by running it with no arguments.