class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return other.x == self.x and other.y == self.y and other.z == self.z
        return False

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Point(x, y, z)

        raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, Point):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
            return Point(x, y, z)

        raise NotImplementedError()

    def __mul__(self, other):
        return Point(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
