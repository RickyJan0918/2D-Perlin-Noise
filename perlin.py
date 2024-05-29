import random

class Perlin2D:
    def __init__(self, x, y):
        self.vector = [random.uniform(-1.0, 1.0) for _ in range(0, (int(x) + 1) * (int(y) + 1) * 2)]
        self.num_col = int(x)
    
    def get(self, x, y):
        i = (int(x) + int(y) * self.num_col) * 2
        x %= 1
        y %= 1
        n1 = self._lerp(self._dot(i, x, y), self._dot(i + 2, x - 1, y), self._curve(x))
        i += 2 * self.num_col
        n2 = self._lerp(self._dot(i, x, y - 1), self._dot(i + 2, x - 1, y - 1), self._curve(x))
        return self._lerp(n1, n2, self._curve(y))
    
    def _dot(self, i, x, y):
        return self.vector[i] * x + self.vector[i+1] * y
    
    def _lerp(self, a, b, t):
        return a + (b - a) * t
    
    def _curve(self, x):
        return x ** 2 * (3 - 2 * x)