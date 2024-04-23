from node import CityNode
from queue import Queue  as q
from search_metrics import SearchMetrics

class BreadthFirstSearch:
    def __init__(self, country_map) -> None:
        self.frontier = q()
        self.reached = []
        self.map = country_map
        self.search_metrics = SearchMetrics()

    def get_search_metrics(self):
        return self.search_metrics

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
                                path_cost= int(current_node.get_path_cost()) + int(neighbors[i]))
                
                
                
                nieghbor_nodes.append(node)
                self.search_metrics.increment_expanded()
                

            return nieghbor_nodes




    def search(self, intitial, goal):
        #print(f"\n------------------------------------------------------------------------------------------------------\n")
        # Initialize first node ROOT
        node = CityNode(state =intitial,
                        parent= None,
                        action="Initial",
                        path_cost=0)
        
        #If the node is the goal node return node]
        if node.get_state() == goal:
            return node

        # Add node to frontier, FIFO queue
        self.frontier.put(node)

        # Add node to reached set/list
        self.reached.append(node.get_state())

        # While frontier is not empty
        while not self.frontier.empty():
            
            # Node = frontier.pop()
            node = self.frontier.get()
            self.search_metrics.increment_explored()
            node.set_action("Explored")

            # For each child of the node
            children = self.expand(node)
            if children is not None:   
                for child in children:                

                    # if node is the goal node return
                    if child.get_state() == goal:
                        return child

                    # if node not in reached set add node to reached
                    if child.get_state() not in self.reached:
                        child.set_action("Maintained")
                        self.reached.append(child.get_state())
                        self.frontier.put(child)
                        self.search_metrics.increment_maintained()

        return None


    def get_expanded(self):
        return self.search_metrics.get_expanded()
    
    def get_explored(self):
        return self.search_metrics.get_explored()
    
    def get_maintained(self):
        return self.search_metrics.get_maintained()