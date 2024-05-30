# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/29/2024
# Description: the code for point and segment classes, incorporating the concepts of private data members.
class Point:
    """Represent a point in 2D space."""
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def distance(self, other_point):
        x1, y1 = self._x_coord, self._y_coord
        x2, y2 = other_point.get_x_coord(), other_point.get_y_coord()
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2
    def get_endpoint_1(self):
        return self._endpoint_1
    def get_endpoint_2(self):
        return self._endpoint_2
    def length(self):
        return self._endpoint_1.distance(self._endpoint_2)
    def slope(self):
        x1, y1 = self._endpoint_1.get_x_coord(), self._endpoint_1.get_y_coord()
        x2, y2 = self._endpoint_2.get_x_coord(), self._endpoint_2.get_y_coord()
        if x2 - x1 == 0:
            return float ('int')
        return (y2-y1)/(x2-x1)
    def is_parallel(self, other_line):
        slope1 = self.slope()
        slope2 = other_line.slope()
        return abs(slope1-slope2) < 0.000001