class AverageWriter:

    def __init__(self,
                 bfs_average_explored,
                idls_average_explored,
                astar_e_average_explored,
                astar_h_average_explored,
                bfs_average_maintained,
                idls_average_maintained,
                astar_e_average_maintained,
                astar_h_average_maintained,
                bfs_average_expanded,
                idls_average_expanded,
                astar_e_average_expanded,
                astar_h_average_expanded,
                ucs_average_explored,
                ucs_average_maintained,
                ucs_average_expanded,
                astar_h_costs,
                astar_e_costs,
                bfs_costs,
                idls_costs,
                ucs_costs):
        self.bfs_average_explored = bfs_average_explored
        self.idls_average_explored = idls_average_explored
        self.astar_e_average_explored = astar_e_average_explored
        self.astar_h_average_explored = astar_h_average_explored
        self.bfs_average_maintained = bfs_average_maintained
        self.idls_average_maintained = idls_average_maintained
        self.astar_e_average_maintained = astar_e_average_maintained
        self.astar_h_average_maintained = astar_h_average_maintained
        self.bfs_average_expanded = bfs_average_expanded
        self.idls_average_expanded = idls_average_expanded
        self.astar_e_average_expanded = astar_e_average_expanded
        self.astar_h_average_expanded = astar_h_average_expanded
        self.ucs_average_explored = ucs_average_explored
        self.ucs_average_maintained = ucs_average_maintained
        self.ucs_average_expanded = ucs_average_expanded
        self.astar_h_costs = astar_h_costs
        self.astar_e_costs = astar_e_costs
        self.bfs_costs = bfs_costs
        self.idls_costs = idls_costs
        self.ucs_costs = ucs_costs


    def print_averages_to_file(self):
        with open('solutions.txt', 'a') as f:
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE BFS EXPLORED: {sum(self.bfs_average_explored) / len(self.bfs_average_explored)}\n")
            f.write(f"AVERAGE BFS MAINTAINED: {sum(self.bfs_average_maintained) / len(self.bfs_average_maintained)}\n")
            f.write(f"AVERAGE BFS EXPANDED: {sum(self.bfs_average_expanded) / len(self.bfs_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE IDLS EXPLORED: {sum(self.idls_average_explored) / len(self.idls_average_explored)}\n")
            f.write(f"AVERAGE IDLS MAINTAINED: {sum(self.idls_average_maintained) / len(self.idls_average_maintained)}\n")
            f.write(f"AVERAGE IDLS EXPANDED: {sum(self.idls_average_expanded) / len(self.idls_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE UCS EXPLORED: {sum(self.ucs_average_explored) / len(self.ucs_average_explored)}\n")
            f.write(f"AVERAGE UCS MAINTAINED: {sum(self.ucs_average_maintained) / len(self.ucs_average_maintained)}\n")
            f.write(f"AVERAGE UCS EXPANDED: {sum(self.ucs_average_expanded) / len(self.ucs_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE ASTAR-E EXPLORED: {sum(self.astar_e_average_explored) / len(self.astar_e_average_explored)}\n")
            f.write(f"AVERAGE ASTAR-E MAINTAINED: {sum(self.astar_e_average_maintained) / len(self.astar_e_average_maintained)}\n")
            f.write(f"AVERAGE ASTAR-E EXPANDED: {sum(self.astar_e_average_expanded) / len(self.astar_e_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE ASTAR-H EXPLORED: {sum(self.astar_h_average_explored) / len(self.astar_h_average_explored)}\n")
            f.write(f"AVERAGE ASTAR-H MAINTAINED: {sum(self.astar_h_average_maintained) / len(self.astar_h_average_maintained)}\n")
            f.write(f"AVERAGE ASTAR-H EXPANDED: {sum(self.astar_h_average_expanded) / len(self.astar_h_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")

        counts = {
                "bfs": 0,
                "idls": 0,
                "ucs": 0,
                "astar_e": 0,
                "astar_h": 0
            }

        for i in range(len(self.astar_h_costs)):
            with open('solutions.txt', 'a') as f:
                f.write(f"\n\n\n\nastar_h: {self.astar_h_costs[i]}\n")
                f.write(f"astar_e: {self.astar_e_costs[i]}\n")
                f.write(f"bfs: {self.bfs_costs[i]}\n")
                f.write(f"idls: {self.idls_costs[i]}\n")
                f.write(f"ucs: {self.ucs_costs[i]}\n")

            if self.astar_h_costs[i] <= self.bfs_costs[i] and self.astar_h_costs[i] <= self.idls_costs[i] and self.astar_h_costs[i] <= self.ucs_costs[i] and self.astar_h_costs[i] <= self.astar_e_costs[i]:
                counts["astar_h"] += 1
            if self.astar_e_costs[i] <= self.bfs_costs[i] and self.astar_e_costs[i] <= self.idls_costs[i] and self.astar_e_costs[i] <= self.ucs_costs[i] and self.astar_e_costs[i] <= self.astar_h_costs[i]:
                counts["astar_e"] += 1
            if self.bfs_costs[i] <= self.idls_costs[i] and self.bfs_costs[i] <= self.ucs_costs[i] and self.bfs_costs[i] <= self.astar_h_costs[i] and self.bfs_costs[i] <= self.astar_e_costs[i]:
                counts["bfs"] += 1
            if self.idls_costs[i] <= self.ucs_costs[i] and self.idls_costs[i] <= self.astar_h_costs[i] and self.idls_costs[i] <= self.astar_e_costs[i] and self.idls_costs[i] <= self.bfs_costs[i]:
                counts["idls"] += 1
            elif self.ucs_costs[i] <= self.astar_h_costs[i] and self.ucs_costs[i] <= self.astar_e_costs[i] and self.ucs_costs[i] <= self.bfs_costs[i] and self.ucs_costs[i] <= self.idls_costs[i]:
                counts["ucs"] += 1
            else:
                print("No winner.")

        with open('solutions.txt', 'a') as f:
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            for i in counts.keys():
                f.write(f"{i} was optimal {counts[i]} times.\n")



