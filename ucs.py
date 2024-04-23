from queue import PriorityQueue
from node import CityNode
from search_metrics import SearchMetrics

class UniformCostSearch:

    def __init__(self, country_map, city_to_weight_map):
        self.frontier = PriorityQueue()
        self.reached = {}
        self.map = country_map
        self.city_to_weight_map = city_to_weight_map
        self.search_metrics = SearchMetrics()

    def get_search_metrics(self):
        return self.search_metrics

    def expand(self, current_node, city_to_weight_map):

        nodes = []

        state = current_node.get_state()
        neighbors = city_to_weight_map[state]

        for neighbor in neighbors:

            s_prime = neighbor[0]

            cost = int(neighbor[1]) + current_node.get_path_cost()

            new_node = CityNode(state=s_prime,
                                parent = current_node,
                                action="Reached",
                                path_cost=cost)

            
            nodes.append(new_node)
            self.search_metrics.increment_expanded()

        return nodes


    def uniform_cost_search(self, initial, goal):
        # Set initial node
        node = CityNode(state = initial,
                        parent = None,
                        action = "Initial",
                        path_cost = 0)
        
        
        # Put node in priority queue
        self.frontier.put(node)

        # Put node into reached with a value of 0
        self.reached[initial] = node
        
        # While frontier is not empty do
        while not self.frontier.empty():

            # node = frontier.pop()
            node = self.frontier.get()

            # Increment the explored
            self.search_metrics.increment_explored()

            # If problem is goal state then return node
            if node.get_state() == goal:
                return node
            
            # for each child of the current node EXPAND do
            for child in self.expand(node, self.city_to_weight_map):

                # s = child.state
                s = child.get_state()

                # if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
                if s not in self.reached or child.get_path_cost() < self.reached[s].get_path_cost():
                    child.set_action("Explored")
                    # reached[s] = child
                    self.reached[s] = child
                    # add child to frontier
                    self.frontier.put(child)
                    self.search_metrics.increment_maintained()

                    
        # return failure
        return None
    
    def search(self, initial, goal):
        return self.uniform_cost_search(initial, goal)
    
    def get_explored(self):
        return self.search_metrics.get_explored()
    
    def get_maintained(self):
        return self.search_metrics.get_maintained()
    
    def get_expanded(self):
        return self.search_metrics.get_expanded()