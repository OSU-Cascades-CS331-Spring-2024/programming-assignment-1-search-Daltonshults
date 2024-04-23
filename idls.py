from node import CityNode
from queue import LifoQueue
from search_metrics import SearchMetrics

class DepthLimitedSearch:

    def __init__(self, country_map, search_metrics):
        self.frontier = LifoQueue()
        self.reached = []
        self.map = country_map
        self.search_metrics = search_metrics

    def depth(self, node):
        '''
        Returns the depth of a node in a graph
        '''
        depth = 1

        while True:
            if node.get_parent() != None:
                depth += 1
                node = node.get_parent()
            else:
                break

        return depth

    def expand(self, current_node):
        '''
        Used to generate children nodes of a node
        '''
        neighbors = self.map.get_neighbors(current_node.get_state())
        nieghbor_nodes = []
        if neighbors is not None:
            for i in neighbors.keys():
                node = CityNode(state=i,
                                parent=current_node,
                                action="Expanded",
                                path_cost=int(current_node.get_path_cost()) + int(neighbors[i]))
                
                nieghbor_nodes.append(node)
                self.search_metrics.increment_expanded()

            return nieghbor_nodes
        
    def pop_node_path(self):
        node = self.frontier.get()
        path = set()
        current = node.get_parent()
        while current != None:
            path.add(current.get_state())
            current = current.get_parent()

        return node, path





    def depth_limited_search(self, initial, goal, max_depth):
        # Add initial node to the frontier using a LIFO queue
        self.frontier.put(CityNode(state=initial,
                                   parent= None,
                                   action ="Initial",
                                   path_cost=0))

        result = None

        # while frontier is not empty

        while not self.frontier.empty():

            # Node = frontier.pop()
            node, path = self.pop_node_path()
            node.set_action("Explored")
            self.search_metrics.increment_explored()

            # if node is the goal return the node
            if node.get_state() == goal:
                return node
            
            # if the depth of node is greater than max_depth 
            if self.depth(node) > max_depth:
                result = "cutoff"
            
            # elif if it is not a cycle
            elif node.get_state() not in path:

                # for each child of the node expand()
                children = self.expand(node)
                if children is not None:
                    for child in children:
                        
                        # Add child to frontier
                        child.set_action("Maintained")
                        self.frontier.put(child)
                        self.search_metrics.increment_maintained()

        return result
    


class IterativeDepthLimitedSearch:
    
    def __init__(self, country_map, depth_limited_search=None):
        self.search_metrics = SearchMetrics()
        if depth_limited_search is None:
            self.dls = DepthLimitedSearch(country_map=country_map,
                                          search_metrics=self.search_metrics)
        else:
            self.dls = depth_limited_search

    def iterative_depth_limited_search(self, initial, goal, max_depth):
        for depth in range(0, max_depth+1):
            result = self.dls.depth_limited_search(initial=initial,
                                                   goal=goal, 
                                                   max_depth=depth)

            if result != "cutoff" and result != None:
                return result
        if result == "cutoff":
            return "cutoff"
        
        return None
    
    def search(self, initial, goal):
        return self.iterative_depth_limited_search(initial, goal, 500)
    
    def get_expanded(self):
        return self.search_metrics.get_expanded()
    
    def get_explored(self):
        return self.search_metrics.get_explored()
    
    def get_maintained(self):
        return self.search_metrics.get_maintained()
    
    def get_search_metrics(self):
        return self.search_metrics