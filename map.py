class CountryMap:
    def __init__(self, cities):
        self.graph = {}
        self.cities = cities

        if cities != None:
            for city in self.cities:
                self.graph[city.city_name] = {}

                for go_city in city.go_cities_with_weights:
                    self.graph[city.city_name][go_city[0]] = go_city[1]

    # def create_graph(self):
    #     for city in self.cities:
    #         self.graph[city.city_name] = {}

    #         for go_city in city.go_cities_with_weights:
    #             self.graph[city.city_name][go_city[0]] = go_city[1]

    def get_graph(self):
        return self.graph
    
    def get_city(self, city_name):
        if city_name in self.graph.keys():
            return self.graph[city_name]
        
    def get_cities(self):
        return self.cities
        
    def get_neighbors(self, city_name):
        if city_name in self.graph.keys():
            return self.graph[city_name]
        else:
            return None
    
    def strip_va(self, city_name):
        '''
        Might not need this because I can strip va- when parsing
        '''
        return city_name[3:]