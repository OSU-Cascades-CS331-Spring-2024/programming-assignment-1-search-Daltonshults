from node import CityNodeAStar
from queue import PriorityQueue
from distance_checker import EuclideanDistance, HaversineDistance
from search_metrics import SearchMetrics

class AStarSearch:
    def __init__(self, country_map, city_to_weight_map, city_to_coords):
        self.frontier = PriorityQueue()
        self.reached = {}
        self.map = country_map
        self.city_to_weight_map = city_to_weight_map
        self.city_to_coords = city_to_coords
        self.search_metrics = SearchMetrics()


    def expand(self, current_node, goal, heuristic, actions):
        nodes = []

        state = current_node.get_state()
        neighbors = self.city_to_weight_map[state]

        for neighbor in neighbors:
            s_prime = neighbor[0]
            
            cost = int(neighbor[1]) + current_node.get_path_cost()

            h_score = heuristic(point_1 = self.city_to_coords[s_prime],
                                  point_2 = self.city_to_coords[goal])
            f_score = cost + h_score
            
            new_node = CityNodeAStar(state = s_prime,
                                     parent= current_node,
                                     action=actions.explored(),
                                     path_cost = cost,
                                     h_score=h_score,
                                     f_score=f_score)
            nodes.append(new_node)
            self.search_metrics.increment_expanded()

        return nodes

    def astar_search(self, initial, goal, heuristic, actions):
        initial_h_score = heuristic(point_1 = self.city_to_coords[initial],
                                    point_2 = self.city_to_coords[goal])

        node = CityNodeAStar(state = initial,
                            parent=None,
                            action=actions.initial(),
                            path_cost= 0,
                            h_score = initial_h_score,
                            f_score=initial_h_score)

        self.frontier.put(node)

        self.reached[initial] = node

        while not self.frontier.empty():

            node = self.frontier.get()
            self.search_metrics.increment_explored()

            if node.get_state() == goal:
                return node

            for child in self.expand(node, goal, heuristic, actions):
                s = child.get_state()

                if s not in self.reached or child.get_path_cost() < self.reached[s].get_path_cost():
                    child.set_action(actions.maintained())
                    self.reached[s] = child
                    self.frontier.put(child)
                    self.search_metrics.increment_maintained()

        return None
    
    def get_search_metrics(self):
        return self.search_metrics
    
    def astar_search_haversine(self, initial, goal, actions):
        return self.astar_search(initial, goal, HaversineDistance().distance, actions)
    
    def astar_search_euclidean(self, initial, goal, actions):
        return self.astar_search(initial, goal, EuclideanDistance().distance, actions)
    
    def search(self, initial, goal):
        return self.astar_search_haversine(initial, goal)
    
    def get_explored(self):
        return self.search_metrics.get_explored()
    
    def get_maintained(self):
        return self.search_metrics.get_maintained()
    
    def get_expanded(self):
        return self.search_metrics.get_expanded()
    
class AStarEuclideanSearch(AStarSearch):
    def __init__(self, country_map, city_to_weight_map, city_to_coords):
        super().__init__(country_map, city_to_weight_map, city_to_coords)
    
    def search(self, initial, goal, actions):
        return self.astar_search_euclidean(initial, goal, actions)
    
class AStarHaversineSearch(AStarSearch):
    def __init__(self, country_map, city_to_weight_map, city_to_coords):
        super().__init__(country_map, city_to_weight_map, city_to_coords)
    
    def search(self, initial, goal, actions):
        return self.astar_search_haversine(initial, goal, actions)