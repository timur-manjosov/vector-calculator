import math

class Vector:
    def __init__(self, *components):
        self.components = components


    def show(self):
        print(f"{self.components}")


    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")

        new_components = []
        for a, b in zip(self.components, other.components):
            new_components.append(a + b)
        return Vector(*new_components)

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")

        new_components = []
        for a, b in zip(self.components, other.components):
            new_components.append(a - b)
        return Vector(*new_components)

    def __mul__(self, scale_number):
        new_components = []
        for c in self.components:
            new_components.append(c * scale_number)
        return Vector(*new_components)

    def __rmul__(self, scale_number):
        return self * scale_number

    def magnitude(self):
        result = 0
        for c in self.components:
            result += c**2
        return math.sqrt(result)

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension.")
        result = 0
        for a, b in zip(self.components, other.components):
            result += a * b
        return result

# --- Demo: every operation once ---
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("v1 =", end=" ")
v1.show()
print("v2 =", end=" ")
v2.show()

print("\nv1 + v2 =", end=" ")
(v1 + v2).show()

print("v1 scaled by 2 =", end=" ")
v4 = v1 * 2 
v5 = 2 * v1
v4.show()
v5.show()

print(f"\nmagnitude of v1 = {v1.magnitude()}")
print(f"dot product v1 . v2 = {v1.dot(v2)}")

# Orthogonality check: perpendicular vectors have dot product 0
right = Vector(1, 0)
up = Vector(0, 1)
print(f"dot product of perpendicular vectors = {right.dot(up)}")

