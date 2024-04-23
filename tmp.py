from math import radians, cos, sin, asin, sqrt

point_1 = ([48, 23, 0, "N"], [5, 29, 0, "W"])
point_2 = ([51, 30, 53, "N"], [1, 51, 23, "E"])

class HaversineDistance:

    def decimal_degrees(self, point):
        long = point[1]
        lat = point[0]

        d_degrees_long = long[0] + long[1]/60 + long[2]/3600
        d_degrees_lat = lat[0] + lat[1]/60 + lat[2]/3600

        if long[3] == "W":
            d_degrees_long = -d_degrees_long

        if lat[3] == "S":
            d_degrees_lat = -d_degrees_lat
        

        return d_degrees_lat, d_degrees_long

    def convert_to_radians(self, lat_1, long_1, lat_2, long_2):
        lat_1 = radians(lat_1)
        long_1 = radians(long_1)
        lat_2 = radians(lat_2)
        long_2 = radians(long_2)

        return lat_1, long_1, lat_2, long_2

    def compute_c(self, alpha):
        return 2 * asin(sqrt(alpha))

    def compute_distance(self, c, r):
        return c * r

    def haversine(self, point_1, point_2):
        r = 6371
        lat_1, long_1 = self.decimal_degrees(point_1)
        lat_2, long_2 = self.decimal_degrees(point_2) 

        print(f"lat_1: {lat_1}\n, long_1: {long_1}\n, lat_2: {lat_2}\n, long_2: {long_2}\n")

        lat_1, long_1, lat_2, long_2 = self.convert_to_radians(lat_1,
                                                        long_1,
                                                        lat_2,
                                                        long_2)
        


        dlat = lat_2 - lat_1
        dlong = long_2 - long_1

        alpha = (sin(dlat/2)**2) + cos(lat_1) * cos(lat_2) * (sin(dlong/2)**2)

        return self.compute_distance(self.compute_c(alpha), r)

hd = HaversineDistance()
distance = hd.haversine(point_1, point_2)

print(distance)