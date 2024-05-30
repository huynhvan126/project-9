# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/29/2024
# Description: the code for point and segment classes, incorporating the concepts of private data members.
class Point:
    """Represent a point in 2D space."""
    def __init__(self, x_coord, y_coord):
        """Initialize the point object with the given x and y coordinates."""
        self._x_coord = x_coord
        self._y_coord = y_coord
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def distance_to(self, other_point):
        """Calculate the distance between this point and the other."""
        x_diff = self._x_coord - other_point.get_x_coord()
        y_diff = self._y_coord - other_point.get_y_coord()
        return (x_diff ** 2 + y_diff ** 2) ** 0.5
class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        """Initialize the line segment object with the given 2 endpoints."""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2
    def get_endpoint_1(self):
        return self._endpoint_1
    def get_endpoint_2(self):
        return self._endpoint_2
    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)
    def slope(self):
        x1 = self._endpoint_1.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        x2 = self._endpoint_2.get_x_coord()
        y2 = self._endpoint_2.get_y_coord()
        if x1 == x2 and y1 == y2:
            return None
        else:
            return None
        return (y2 - y1) / (x2 - x1)
    def is_parallel_to(self, other_line):
        slope1 = self.slope()
        slope2 = other_line.slope()
        if slope1 is None and slope2 is None:
            return True
        if slope1 is None or slope2 is None
            return False
        return abs(slope1-slope2) < 0.000001
