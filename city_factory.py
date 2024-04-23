from city import City

class CityFactory:

    def create_city_nodes_from_lists(self, cities, go_cities_with_weights, coordinates):
        node_list = []
        for i in range(len(cities)):
            node_list.append(City(cities[i], go_cities_with_weights[i], coordinates[i]))

        return node_list