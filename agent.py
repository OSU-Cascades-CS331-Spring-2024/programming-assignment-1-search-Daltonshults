class Agent:

    def __init__(self, algorithm, start_city, goal_city, map, actions):
        self._algorithm = algorithm
        self._start_city = start_city
        self._goal_city = goal_city
        self._map = map
        self.actions = actions
    
    def construct_path(self, final_node):
        path = []
        current_node = final_node

        while current_node != None:
            path.append(current_node)
            current_node = current_node.get_parent()

        return path[::-1]
    
    def travel_path(self, path):

        for i in range(0, len(path)-1):
            self.actions.move_city_a_to_city_b(
                city_a = path[i].get_state(), 
                city_b = path[i+1].get_state(),
                node =path[i])
            
        path[-1].set_action("Goal")

        return path
    
    def print_path_to_solutions(self, path, algo_str, search_metrics, cost):
        with open('solutions.txt', 'a') as f:
            f.write("\n---------------------------------------------\n")
            f.write(f"Algorithm: {algo_str}\n")
            f.write(f"Start City: {self.get_start_city()}\n")
            f.write(f"Goal City: {self.get_goal_city()}\n")
            f.write(f"Path Cost: {cost}\n")
            f.write(f"Explored: {search_metrics.get_explored()}\n")
            f.write(f"Expanded: {search_metrics.get_expanded()}\n")
            f.write(f"Maintained: {search_metrics.get_maintained()}\n")
            for i in path:
                f.write(f"Actions: {i.get_action()}\n")

    def print_info_to_terminal(self, path, algo_str, search_metrics, cost):
        print("\n---------------------------------------------\n")
        print(f"Algorithm: {algo_str}")
        print(f"Start City: {self.get_start_city()}")
        print(f"Goal City: {self.get_goal_city()}")
        print(f"Path Cost: {cost}")
        print(f"Explored: {search_metrics.get_explored()}")
        print(f"Expanded: {search_metrics.get_expanded()}")
        print(f"Maintained: {search_metrics.get_maintained()}")
        for i in path:
            print(f"Actions: {i.get_action()}")

            
    
    def get_path_cost(self, path):
        cost = 0
        for i in path:
            cost += i.get_path_cost()

        return cost
    
    def get_results(self, final_node_list, algo_str, cost, search_metrics):
        for final_node in final_node_list:
            path = self.construct_path(final_node)
            path = self.travel_path(path)

            self.print_path_to_solutions(path, algo_str, search_metrics, cost)

    def print_results(self, final_node_list, algo_str, cost, search_metrics):
        for final_node in final_node_list:
            path = self.construct_path(final_node)
            path = self.travel_path(path)

            self.print_info_to_terminal(path, algo_str, search_metrics, cost)


    
    # Getters
    def get_algorithm(self):
        return self._algorithm
    
    def get_start_city(self):
        return self._start_city
    
    def get_goal_city(self):
        return self._goal_city
    
    def get_map(self):
        return self._map
    
    def get_actions(self):
        return self.actions
    
    # Setters
    def set_algorithm(self, algorithm):
        self._algorithm = algorithm
    
    def set_start_city(self, start_city):
        self._start_city = start_city
    
    def set_goal_city(self, goal_city):
        self._goal_city = goal_city
    
    def set_map(self, map):
        self._map = map

    def set_actions(self, actions):
        self.actions = actions


    def search(self):
        return self._algorithm.search(self._start_city, self._goal_city, self.actions)
