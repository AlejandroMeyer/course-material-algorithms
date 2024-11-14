# main.py (Where you import the vector module and perform operations)
from vector import Vector
from vector import Vector3D

# Example usage:
v = Vector(3, 4, 0)
print(v.magnitude())  # Output: 5.0

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
result = v1 + v2
print(result.x, result.y, result.z)  # Output: 5 7 9


# Example usage of Vector3D class:
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(v1.dot_product(v2))  # Output: 32

# Example usage:
v = Vector3D(1, 2, 3)
print(v)  # Output: (1, 2, 3)