class Vector:
    def __init__(self, coord):
        self.x, self.y, self.z = map(float, coord.split(','))

    def __abs__(self):
        res = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return res

    def __add__(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        z = self.z + obj.z
        return Vector('{},{},{}'.format(x, y, z))

    def __sub__(self, obj):
        x = self.x - obj.x
        y = self.y - obj.y
        z = self.z - obj.z
        return Vector('{},{},{}'.format(x, y, z))
    
    def __mul__(self, obj):
        if isinstance(obj, Vector):
            return self.x * obj.x + self.y * obj.y + self.z * obj.z
        else:
            x, y, z = obj * self.x, obj * self.y, obj * self.z
            return Vector('{},{},{}'.format(x, y, z))
    def __rmul__(self, obj):
        if isinstance(obj, Vector):
            return self.x * obj.x + self.y * obj.y + self.z * obj.z
        else:
            x, y, z = obj * self.x, obj * self.y, obj * self.z
            return Vector('{},{},{}'.format(x, y, z))
    
    def __and__(self, obj):
        # a & b
        x = self.y * obj.z - self.z * obj.y
        y = self.z * obj.x - self.x * obj.z
        z = self.x * obj.y - self.y * obj.x
        return Vector('{},{},{}'.format(x, y, z))
    
    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        res = self.x == other.x and self.y == other.y and self.z == other.z
        return res

if __name__ == '__main__':
    a = Vector('1,1,1')
    b = Vector('1,1,1')
    print(a + b)
    print(a - b)
    print(a - b == Vector('0,0,0'))
    print(abs(a))
    print(a * b)
    print(a & b)
    print(2 * a)
    print(a * 2)
