import math


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")

        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")

        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scale_number):
        return Vector(*[c * scale_number for c in self.components])

    def __rmul__(self, scale_number):
        return self * scale_number

    def magnitude(self):
        return math.sqrt(sum(c**2 for c in self.components))

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def normalize(self):
        if all(x == 0 for x in self.components):
            raise ValueError("The zero vector has no direction and cannot be normalized")

        length = self.magnitude()
        return Vector(*[c / length for c in self.components])


# --- Demo: every operation once ---
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("v1 = ", v1)
print("v2 = ", v2)

print("\nv1 + v2 = ", v1 + v2)

print("v1 scaled by 2 = ", v1 * 2)

print(f"\nmagnitude of v1 = {v1.magnitude()}")
print(f"dot product v1 . v2 = {v1.dot(v2)}")

# Orthogonality check: perpendicular vectors have dot product 0
right = Vector(1, 0)
up = Vector(0, 1)
print(f"dot product of perpendicular vectors = {right.dot(up)}")

print(Vector(3, 4).normalize())
print(Vector(3, 4).normalize().magnitude())

try:
    print(Vector(0,0).normalize())
except ValueError as error:
    print(f"Caught: {error}")
