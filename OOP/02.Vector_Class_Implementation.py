import math

class Vector:
    def __init__(self, coordinates: list):
        self._dims = len(coordinates)
        self.val = coordinates

    def _dim_check(self, b):
        if self._dims != b._dims:
            raise TypeError("invalid dimension")

    def add(self, y):
        self._dim_check(y)
        res = []

        for i in range(self._dims):
            res.append(self.val[i] + y.val[i])

        return Vector(res)

    def subtract(self, y):
        self._dim_check(y)
        res = []

        for i in range(self._dims):
            res.append(self.val[i] - y.val[i])

        return Vector(res)

    def dot(self, b):
        self._dim_check(b)
        res = 0

        for i in range(self._dims):
            res += self.val[i] * b.val[i]

        return res

    def norm(self):
        res = 0

        for i in range(self._dims):
            res += self.val[i] ** 2

        return math.sqrt(res)

    def equals(self, b):
        return self.val == b.val
    def __str__(self):
        return f"({','.join(map(str,self.val))})"
