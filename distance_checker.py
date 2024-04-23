from math import radians, cos, sin, asin, sqrt

class DistanceChecker:
    def decimal_degrees(self, point):
        lat = point[0]
        long = point[1]

        d_degrees_lat = int(lat[0]) + int(lat[1])/60 + int(lat[2])/3600
        d_degrees_long = int(long[0]) + int(long[1])/60 + int(long[2])/3600
        
        if lat[3] == "S":
            d_degrees_lat = -d_degrees_lat

        if long[3] == "W":
            d_degrees_long = -d_degrees_long        

        return d_degrees_lat, d_degrees_long

    def convert_to_radians(self, lat_1, long_1, lat_2, long_2):
        lat_1 = radians(lat_1)
        long_1 = radians(long_1)
        lat_2 = radians(lat_2)
        long_2 = radians(long_2)

        return lat_1, long_1, lat_2, long_2
    
class HaversineDistance(DistanceChecker):

    def compute_c(self, alpha):
        return 2 * asin(sqrt(alpha))

    def compute_distance(self, c, r):
        return c * r

    def haversine(self, point_1, point_2):
        # Aproximate radius of the earth in kilometers
        r = 1
        lat_1, long_1 = self.decimal_degrees(point_1)
        lat_2, long_2 = self.decimal_degrees(point_2) 

        lat_1, long_1, lat_2, long_2 = self.convert_to_radians(lat_1,
                                                        long_1,
                                                        lat_2,
                                                        long_2)     


        dlat = lat_2 - lat_1
        dlong = long_2 - long_1

        alpha = (sin(dlat/2)**2) + cos(lat_1) * cos(lat_2) * (sin(dlong/2)**2)

        return self.compute_distance(self.compute_c(alpha), r)
    
    def distance(self, point_1, point_2):
        return self.haversine(point_1, point_2)
    
class EuclideanDistance(DistanceChecker):

    def euclidean(self, point_1, point_2):
        lat_1, long_1 = self.decimal_degrees(point_1)
        lat_2, long_2 = self.decimal_degrees(point_2)

        y = (abs(lat_1 - lat_2))** 2
        x = (abs(long_1 - long_2))** 2

        total = sqrt(x + y) #* 111.2
        '''
        One degree of latitude is equal to 25,000/360 
                                          = 69.4 miles 
                                          = 111.2 kilometers
        '''
        return total
    
    def distance(self, point_1, point_2):
        return self.euclidean(point_1, point_2)