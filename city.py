class City:

    def __init__(self, city_name, go_cities_with_weights, coordinates):
        self.city_name = city_name
        self.coordinates = coordinates
        self.go_cities_with_weights = go_cities_with_weights

    def get_city_name(self):
        return self.city_name
    
    def get_coordinates(self):
        return self.coordinates 
    
    def get_go_cities_with_weights(self):
        return self.go_cities_with_weights