class MapParser:

    def open_map(self, file_path):  
        strings = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    strings.append(line.strip())

            return strings
                    
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except IOError:
            print(f"Error reading file '{file_path}'.")

    def arrow_split(self, lines): 
        split_lines_vertex = []
        split_lines_edges = []

        for i in lines:
            line = i.split(" --> ")
            split_lines_vertex.append(line[0])
            split_lines_edges.append(line[1])

        return split_lines_vertex, split_lines_edges
    
    def city_from_dms(self, split_lines_vertex):
        cities = []
        dmss = []
        for vertex in split_lines_vertex:
            city_dms = vertex.split(" ")
            cities.append(city_dms[0])
            dmss.append(self._combine_dms(city_dms))
            
        

        return cities, dmss
    
    def _combine_dms(self, city_dms_split):
        return city_dms_split[1:]
    
    def split_go_city_from_weight(self, split_lines_edges):
        # Initializing the list with the right number of lists
        cities_with_weights = [[] for i in range(len(split_lines_edges)) ] 

        # Iterating over the length of the list to split by the space
        for i in range(len(split_lines_edges)):
            splits = split_lines_edges[i].split(" ")

            # Pairing every second item on the list.
            for j in range(0, len(splits), 2):

                # Stripping va- from the city name
                cities_with_weights[i].append((splits[j][3:], splits[j+1]))  

        return cities_with_weights
    
    def split_dms(self, dmss):
        dms_split = []
        for i in range(len(dmss)):
            first_coord = dmss[i][0:4]
            second_coord = dmss[i][4:8]
            dms_split.append((first_coord, second_coord))

        return dms_split




    def driver(self, file_path):
        lines = self.open_map(file_path)
        split_lines_vertex, split_lines_edges = self.arrow_split(lines)

        cities, dmss = self.city_from_dms(split_lines_vertex)
        go_cities_with_weights = self.split_go_city_from_weight(split_lines_edges)
        coordinates = self.split_dms(dmss)
        
        return cities, go_cities_with_weights, coordinates
            