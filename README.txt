# Dalton Answers
1. The average number of nodes explored or entered (i.e., the number of nodes removed from the frontier)
    * AVERAGE BFS EXPLORED: 10.333333333333334
    * AVERAGE IDLS EXPLORED: 147.88888888888889
    * AVERAGE UCS EXPLORED: 15.88888888888889
    * AVERAGE ASTAR-E EXPLORED: 8.333333333333334
    * AVERAGE ASTAR-H EXPLORED: 9.222222222222221

2. The average number of nodes expanded (i.e., the total number of successors)
    * AVERAGE BFS EXPANDED: 35.111111111111114
    * AVERAGE IDLS EXPANDED: 148.77777777777777
    * AVERAGE UCS EXPANDED: 49.111111111111114
    * AVERAGE ASTAR-E EXPANDED: 26.0
    * AVERAGE ASTAR-H EXPANDED: 29.22222222222222


3. The average number of nodes maintained (i.e., stored in the frontier)
    * AVERAGE BFS MAINTAINED: 12.222222222222221
    * AVERAGE IDLS MAINTAINED: 148.77777777777777
    * AVERAGE UCS MAINTAINED: 17.22222222222222
    * AVERAGE ASTAR-E MAINTAINED: 13.11111111111111
    * AVERAGE ASTAR-H MAINTAINED: 14.333333333333334

4. The number of times it found the optimal solution (optimal here is measured as “found the best solution out of the four search algorithms)
    * bfs was optimal 2 times.
    * idls was optimal 3 times.
    * ucs was optimal 6 times.
    * astar_e was optimal 8 times.
    * astar_h was optimal 8 times.


The A-star algorithm is the most accurate of the bunch, as it should find the optimal answer every time if the heuristic is implemented correctly. However, my implementation must have an error that I could not see after hours of searching, and my implementation is not returning the optimal answer every time. To try and fix this, I went through and disabled the heuristic calculations by setting them to 0. It then came up with the same result as UCS, leading me to believe that my heuristic was implemented incorrectly. I spent 2 hours looking over the heuristics and even wrote some tests to see if it would return the expected answers, and it did. However, without the limitations of my implementation, this would be one of the best searching methods as it decreases the space complexity by pruning certain paths using the heuristic. However, UCS did come up with an answer that was more optimal in one situation; it did not come up with as many optimal answers as often as A-star. The iterative-deepening search used a ton of memory space as it had the highest averages of the explored, maintained, and expanded nodes. This seems to occur because of the way it iterates through depths. If you explore all of the nodes up to a certain depth and then increase the maximum depth, you are running the same nodes repeatedly allowing for more of them to be loaded in and out of memory by the agent. BFS did operate slightly better than I thought it would, but because it is an uninformed search it might provide less than optimal answers.

If you can find the error please let me know because I would love to know where I made the mistake. I rebuilt the entire A* algo, and rewrote all of the heuristics again. Then came up with the same problem. 