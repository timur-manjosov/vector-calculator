import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"[ {self.x} , {self.y} ]")


    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def scale(self, scale_number):
        new_x = self.x * scale_number
        new_y = self.y * scale_number
        return Vector(new_x, new_y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y


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
v1.scale(2).show()

print(f"\nmagnitude of v1 = {v1.magnitude()}")
print(f"dot product v1 . v2 = {v1.dot(v2)}")

# Orthogonality check: perpendicular vectors have dot product 0
right = Vector(1, 0)
up = Vector(0, 1)
print(f"dot product of perpendicular vectors = {right.dot(up)}")
