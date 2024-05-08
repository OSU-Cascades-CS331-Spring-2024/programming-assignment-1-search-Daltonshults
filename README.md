CS331

Spring 2024

Programming Assignment 1 – Search

Due April 22nd at 11:59pm PST

# Dalton Answers
1. The average number of nodes explored or entered (i.e., the number of nodes removed from the frontier)
    * AVERAGE BFS EXPLORED: 10.333333333333334
    * AVERAGE IDLS EXPLORED: 147.88888888888889
    * AVERAGE UCS EXPLORED: 15.88888888888889
    * AVERAGE ASTAR-E EXPLORED: 15.88888888888889
    * AVERAGE ASTAR-H EXPLORED: 15.88888888888889

2. The average number of nodes expanded (i.e., the total number of successors)
    * AVERAGE BFS EXPANDED: 35.111111111111114
    * AVERAGE IDLS EXPANDED: 148.77777777777777
    * AVERAGE UCS EXPANDED: 49.111111111111114
    * AVERAGE ASTAR-E EXPANDED: 49.111111111111114
    * AVERAGE ASTAR-H EXPANDED: 49.111111111111114


3. The average number of nodes maintained (i.e., stored in the frontier)
    * AVERAGE BFS MAINTAINED: 12.222222222222221
    * AVERAGE IDLS MAINTAINED: 148.77777777777777
    * AVERAGE UCS MAINTAINED: 17.22222222222222
    * AVERAGE ASTAR-E MAINTAINED: 17.22222222222222
    * AVERAGE ASTAR-H MAINTAINED: 17.22222222222222

4. The number of times it found the optimal solution (optimal here is measured as “found the best solution out of the four search algorithms)
* bfs was optimal 2 times.
* idls was optimal 3 times.
* ucs was optimal 6 times.
* astar_e was optimal 9 times.
* astar_h was optimal 9 times.


<p>The A-star algorithm is the most accurate of the set we implemented, as it finds the optimal answer every time if the heuristic is admissible. It was able to use less memory space than the Iterative-Deepening Depth-Limited Search (IDLS) but used more space than the Breadth-First Search (BFS). Comparing A-star to Uniform-Cost Search (UCS), they are similar in the amount of memory space both algorithms use, this isn’t surprising considering how similar they are, but UCS was not able to find the optimal answer as often. Out of UCS and A*, I do not see much of a use for UCS except when implementing an admissiable heuristic isn’t possible. BFS benefited from the memory space it utilized, and because of this, it could be useful in certain applications. BFS operated slightly better than I thought it would, but it might provide less-than-optimal answers because it isn’t an optimal search in weighted graphs. When you are limited on memory, the answer does not need to be optimal, or searching a non-weighted graph BFS is incredibly useful. The IDLS had to use much more memory space than the other algorithms as it had the highest averages of the explored, maintained, and expanded nodes. This occurs because of the way it iterates through depths. You repeatedly run into the same nodes if you explore up to a certain depth of node and then repeat going one edge deeper. This causes the agent to utilize more memory throughout the process, and the agent has to interact with more nodes throughout the search process. I could see this being useful in infinite memory spaces in that you can limit the depth you are searching compared to something like Depth-First Search. Overall, all of these algorithms are useful in their specific applications, but if finding the optimal answer is the most important aspect, I would implement an A* search.</p>

Percentage Of Optimal Answers:
* Breadth-First Search: 22.22%
* Iterative Deepening Depth-First Search: 33.33%
* Uniform-Cost Search: 66.66%
* A* Search Euclidian: 100%
* A* Search Haversine: 100%









