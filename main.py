from map_parser import MapParser
from city_factory import CityFactory
from map import CountryMap
import argparse
from bfs import BreadthFirstSearch
from idls import IterativeDepthLimitedSearch
from ucs import UniformCostSearch
from astar import AStarEuclideanSearch, AStarHaversineSearch
from agent import Agent
from agent_actions import AgentActions

class LinePrinter:
    def print_line():
        print("------------------------------------------------------------------------------------------------------------------")

class ArgParser:        
    def arg_parsing():
        parser = argparse.ArgumentParser(description="Process a map file.")

        parser.add_argument('algorithm',
                            type=str,
                            help="The algorithm to use.",
                            default="bsf",
                            nargs="?")
        
        parser.add_argument('-A',
                            type=str,
                            help="The A argument.",
                            nargs="?")
        
        parser.add_argument('-B',
                            type=str,
                            help="The B argument.",
                            nargs="?")
        
        parser.add_argument('file',
                            type=str,
                            help="The file to process.",
                            default="./france.txt",
                            nargs="?")

        args = parser.parse_args()

        return args

class MapGenerator:
    def get_city_to_weights_map(self, node_list):
        city_to_weights_map = {}

        for i in node_list:
            city_to_weights_map[i.get_city_name()] = i.get_go_cities_with_weights()

        return city_to_weights_map

    def get_city_to_coordinates_map(self, node_list):
        city_to_coordinates_map = {}

        for i in node_list:
            city_to_coordinates_map[i.get_city_name()] = i.get_coordinates()

        return city_to_coordinates_map

def main():
    args = ArgParser.arg_parsing()

    if args.A == None or args.B == None:
        visiting = [
            ("brest", "nice"),
            ("montpellier", "calais"),
            ("strasbourg", "bordeaux"),
            ("paris", "grenoble"),
            ("grenoble", "paris"),
            ("brest", "grenoble"),
            ("grenoble", "brest"),
            ("nice", "nantes"),
            ("caen", "strasbourg")            
            ]
        
        mp = MapParser()
        cnf = CityFactory()
        mg = MapGenerator()
        
        

        cities, go_cities_with_weights, coordinates = mp.driver(args.file)

        node_list = cnf.create_city_nodes_from_lists(cities,
                                                     go_cities_with_weights,
                                                     coordinates)
        
        city_to_weights_map = mg.get_city_to_weights_map(node_list)
        city_to_coordinates_map = mg.get_city_to_coordinates_map(node_list)
        
        cm = CountryMap(node_list)
        aa = AgentActions()
        agent = Agent(None, None, None, cm, aa)


        # Breadth-First Search ---------------------------------------------------------------------
        bfs_final_nodes = []
        bfs_average_explored = []
        bfs_average_maintained = []
        bfs_average_expanded = []
        bfs_costs = []
        for cities in visiting:
            bfs = BreadthFirstSearch(cm)

            agent.set_algorithm(bfs)
            agent.set_goal_city(cities[1])
            agent.set_start_city(cities[0])



            bfs_final_node = agent.search()

            bfs_final_nodes.append(bfs_final_node)

            cost = bfs_final_node.get_path_cost()

            agent.get_results(final_node_list = [bfs_final_node],
                              algo_str= "bfs", 
                              cost = cost,
                              search_metrics=bfs.get_search_metrics())
            
            bfs_average_explored.append(bfs.get_explored())
            bfs_average_maintained.append(bfs.get_maintained())
            bfs_average_expanded.append(bfs.get_expanded())
            bfs_costs.append(cost)


        # Iterative Deepening Depth-Limited Search -----------------------------------------------
        idls_final_nodes = []
        idls_average_explored = []
        idls_average_maintained = []
        idls_average_expanded = []
        idls_costs = []

        for cities in visiting:
            idls = IterativeDepthLimitedSearch(cm)
            
            agent.set_algorithm(idls)
            agent.set_goal_city(cities[1])
            agent.set_start_city(cities[0])

            idls_final_node = agent.search()
            idls_final_nodes.append(idls_final_node)
            
            cost = idls_final_node.get_path_cost()

            agent.get_results(final_node_list = [idls_final_node],
                              algo_str= "idls",
                              cost= cost,
                              search_metrics=idls.get_search_metrics())
            
            idls_average_explored.append(idls.get_explored())
            idls_average_maintained.append(idls.get_maintained())
            idls_average_expanded.append(idls.get_expanded())
            idls_costs.append(cost)




        # Uniform-Cost Search ---------------------------------------------------------------------
        ucs_final_nodes = []
        ucs_average_explored = []
        ucs_average_maintained = []
        ucs_average_expanded = []
        ucs_cost = []

        for cities in visiting:
            ucs = UniformCostSearch(country_map=cm,
                                    city_to_weight_map=city_to_weights_map)
            
            agent.set_algorithm(ucs)
            agent.set_goal_city(cities[1])
            agent.set_start_city(cities[0])
            
            ucs_final_node = agent.search()
            ucs_final_nodes.append(ucs_final_node)

            cost = ucs_final_node.get_path_cost()

            agent.get_results(final_node_list = [ucs_final_node],
                              algo_str= "ucs",
                              cost= cost,
                              search_metrics=ucs.get_search_metrics())
            
            ucs_average_explored.append(ucs.get_explored())
            ucs_average_maintained.append(ucs.get_maintained())
            ucs_average_expanded.append(ucs.get_expanded())
            ucs_cost.append(cost)



        # A-Star Euclidean Search ---------------------------------------------------------------------------
        astar_e_final_nodes = []
        astar_e_average_explored = []
        astar_e_average_maintained = []
        astar_e_average_expanded = []
        astar_e_costs = []

        for cities in visiting:
            astar_e = AStarEuclideanSearch(country_map=cm,
                                  city_to_weight_map=city_to_weights_map,
                                  city_to_coords=city_to_coordinates_map)
            
            agent.set_algorithm(astar_e)
            agent.set_goal_city(cities[1])
            agent.set_start_city(cities[0])
            
            
            astar_e_final_node = agent.search()
            astar_e_final_nodes.append(astar_e_final_node)

            cost = astar_e_final_node.get_path_cost()

            agent.get_results(final_node_list=[astar_e_final_node],
                              algo_str="astar_e",
                              cost=cost,
                              search_metrics=astar_e.get_search_metrics())
            
            astar_e_average_explored.append(astar_e.get_explored())
            astar_e_average_maintained.append(astar_e.get_maintained())
            astar_e_average_expanded.append(astar_e.get_expanded())
            astar_e_costs.append(cost)


        # A-Star Haversine Search ---------------------------------------------------------------------------
        astar_h_final_nodes = []
        astar_h_average_explored = []
        astar_h_average_maintained = []
        astar_h_average_expanded = []
        astar_h_costs = []

        for cities in visiting:
            astar_h = AStarHaversineSearch(country_map=cm,
                                  city_to_weight_map=city_to_weights_map,
                                  city_to_coords=city_to_coordinates_map)
            
            agent.set_algorithm(astar_h)
            agent.set_goal_city(cities[1])
            agent.set_start_city(cities[0])

  
            
            astar_h_final_node = agent.search()
            astar_h_final_nodes.append(astar_h_final_node)

            cost = astar_h_final_node.get_path_cost()
            

            agent.get_results(final_node_list=[astar_h_final_node],
                              algo_str="astar_h",
                              cost=cost,
                              search_metrics=astar_h.get_search_metrics())
            
            astar_h_average_explored.append(astar_h.get_explored())
            astar_h_average_maintained.append(astar_h.get_maintained())
            astar_h_average_expanded.append(astar_h.get_expanded())
            astar_h_costs.append(cost)

        with open('solutions.txt', 'a') as f:
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE BFS EXPLORED: {sum(bfs_average_explored) / len(bfs_average_explored)}\n")
            f.write(f"AVERAGE BFS MAINTAINED: {sum(bfs_average_maintained) / len(bfs_average_maintained)}\n")
            f.write(f"AVERAGE BFS EXPANDED: {sum(bfs_average_expanded) / len(bfs_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE IDLS EXPLORED: {sum(idls_average_explored) / len(idls_average_explored)}\n")
            f.write(f"AVERAGE IDLS MAINTAINED: {sum(idls_average_maintained) / len(idls_average_maintained)}\n")
            f.write(f"AVERAGE IDLS EXPANDED: {sum(idls_average_expanded) / len(idls_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE UCS EXPLORED: {sum(ucs_average_explored) / len(ucs_average_explored)}\n")
            f.write(f"AVERAGE UCS MAINTAINED: {sum(ucs_average_maintained) / len(ucs_average_maintained)}\n")
            f.write(f"AVERAGE UCS EXPANDED: {sum(ucs_average_expanded) / len(ucs_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE ASTAR-E EXPLORED: {sum(astar_e_average_explored) / len(astar_e_average_explored)}\n")
            f.write(f"AVERAGE ASTAR-E MAINTAINED: {sum(astar_e_average_maintained) / len(astar_e_average_maintained)}\n")
            f.write(f"AVERAGE ASTAR-E EXPANDED: {sum(astar_e_average_expanded) / len(astar_e_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"AVERAGE ASTAR-H EXPLORED: {sum(astar_h_average_explored) / len(astar_h_average_explored)}\n")
            f.write(f"AVERAGE ASTAR-H MAINTAINED: {sum(astar_h_average_maintained) / len(astar_h_average_maintained)}\n")
            f.write(f"AVERAGE ASTAR-H EXPANDED: {sum(astar_h_average_expanded) / len(astar_h_average_expanded)}\n")
            f.write("\n------------------------------------------------------------------------------------------------------------------\n")

            counts = {
                "bfs": 0,
                "idls": 0,
                "ucs": 0,
                "astar_e": 0,
                "astar_h": 0
            }

            for i in range(len(astar_h_costs)):
                with open('solutions.txt', 'a') as f:
                    f.write(f"\n\n\n\nastar_h: {astar_h_costs[i]}\n")
                    f.write(f"astar_e: {astar_e_costs[i]}\n")
                    f.write(f"bfs: {bfs_costs[i]}\n")
                    f.write(f"idls: {idls_costs[i]}\n")
                    f.write(f"ucs: {ucs_cost[i]}\n")

                if astar_h_costs[i] <= bfs_costs[i] and astar_h_costs[i] <= idls_costs[i] and astar_h_costs[i] <= ucs_cost[i] and astar_h_costs[i] <= astar_e_costs[i]:
                    counts["astar_h"] += 1
                if astar_e_costs[i] <= bfs_costs[i] and astar_e_costs[i] <= idls_costs[i] and astar_e_costs[i] <= ucs_cost[i] and astar_e_costs[i] <= astar_h_costs[i]:
                    counts["astar_e"] += 1
                if bfs_costs[i] <= idls_costs[i] and bfs_costs[i] <= ucs_cost[i] and bfs_costs[i] <= astar_h_costs[i] and bfs_costs[i] <= astar_e_costs[i]:
                    counts["bfs"] += 1
                if idls_costs[i] <= ucs_cost[i] and idls_costs[i] <= astar_h_costs[i] and idls_costs[i] <= astar_e_costs[i] and idls_costs[i] <= bfs_costs[i]:
                    counts["idls"] += 1
                elif ucs_cost[i] <= astar_h_costs[i] and ucs_cost[i] <= astar_e_costs[i] and ucs_cost[i] <= bfs_costs[i] and ucs_cost[i] <= idls_costs[i]:
                    counts["ucs"] += 1
                else:
                    print("No winner.")

            with open('solutions.txt', 'a') as f:
                f.write("\n------------------------------------------------------------------------------------------------------------------\n")
                for i in counts.keys():
                    f.write(f"{i} was optimal {counts[i]} times.\n")

        
    
    else:
        visiting = [(args.A, args.B)]
        algo = args.algorithm.lower()
        mp = MapParser()
        cnf = CityFactory()
        mg = MapGenerator()
        initial = args.A.lower()
        goal = args.B.lower()

        cities, go_cities_with_weights, coordinates = mp.driver(args.file)

        if initial not in cities or goal not in cities:
            print("One or both of the cities are not in the map.")
            return
        

        node_list = cnf.create_city_nodes_from_lists(cities,
                                                     go_cities_with_weights,
                                                     coordinates)
        
        city_to_weights_map = mg.get_city_to_weights_map(node_list)
        city_to_coordinates_map = mg.get_city_to_coordinates_map(node_list)
        
        cm = CountryMap(node_list)
        agent = Agent(None, None, None, cm, AgentActions)    

        if algo == "bfs":
            bfs = BreadthFirstSearch(cm)

            agent.set_algorithm(bfs)
            agent.set_goal_city(goal)
            agent.set_start_city(initial)

            bfs_final_node = agent.search()
            if bfs_final_node == None:
                print("No path found.")
                return
            else:
                agent.print_results([bfs_final_node], "bfs", bfs_final_node.get_path_cost(), bfs.get_search_metrics())

        elif algo == "dls":
            idls = IterativeDepthLimitedSearch(cm)

            agent.set_algorithm(idls)
            agent.set_goal_city(goal)
            agent.set_start_city(initial)

            idls_final_node = agent.search()
            if idls_final_node == None:
                print("No path found.")
                return
            else:
                agent.print_results([idls_final_node], "idls", idls_final_node.get_path_cost(), idls.get_search_metrics())

        elif algo == "ucs":
            ucs = UniformCostSearch(country_map=cm,
                                    city_to_weight_map=city_to_weights_map)

            agent.set_algorithm(ucs)
            agent.set_goal_city(goal)
            agent.set_start_city(initial)

            ucs_final_node = ucs.uniform_cost_search(initial, goal)
            if ucs_final_node == None:
                print("No path found.")
                return
            else:
                agent.print_results([ucs_final_node], "ucs", ucs_final_node.get_path_cost(), ucs.get_search_metrics())

        elif algo == "astar":
            astar_e = AStarEuclideanSearch(country_map=cm,
                                  city_to_weight_map=city_to_weights_map,
                                  city_to_coords=city_to_coordinates_map)
            
            agent.set_algorithm(astar_e)
            agent.set_goal_city(goal)
            agent.set_start_city(initial)
            
            astar_e_final_node = agent.search()
            if astar_e_final_node == None:
                print("No path found.")
                return
            else:
                agent.print_results([astar_e_final_node], "astar_e", astar_e_final_node.get_path_cost(), astar_e.get_search_metrics())    

            astar_h = AStarHaversineSearch(country_map=cm,
                                           city_to_weight_map=city_to_weights_map,
                                           city_to_coords=city_to_coordinates_map)
            
            agent.set_algorithm(astar_h)
            agent.set_goal_city(goal)
            agent.set_start_city(initial)

            astar_h_final_node = agent.search()

            if astar_h_final_node == None:
                print("No path found.")
                return
            else:
                agent.print_results([astar_h_final_node],
                                  "astar_h",
                                  astar_h_final_node.get_path_cost(),
                                  astar_h.get_search_metrics())

        else:
            print("Invalid algorithm.")
            return

if __name__ == "__main__":
    main()