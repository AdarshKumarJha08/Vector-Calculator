import math

class Vector:
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError("Vector components must be provided as a list.")

        if len(components) not in (2, 3):
            raise ValueError("Vector must have either 2 or 3 components.")

        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError("All vector components must be numbers.")

        self.components = components

    def dimension(self):
        return len(self.components)

    def magnitude(self):
        total = 0

        for component in self.components:
            total += component ** 2

        return math.sqrt(total)

    def unit_vector(self):
        magnitude = self.magnitude()

        if magnitude == 0:
            raise ValueError("Zero vector does not have a unit vector.")

        return Vector([component / magnitude for component in self.components])

    def add(self, other):
        if self.dimension() != other.dimension():
            raise ValueError("Vectors must have the same dimension.")

        result = []

        for i in range(self.dimension()):
            result.append(self.components[i] + other.components[i])

        return Vector(result)

    def subtract(self, other):
        if self.dimension() != other.dimension():
            raise ValueError("Vectors must have the same dimension.")

        result = []

        for i in range(self.dimension()):
            result.append(self.components[i] - other.components[i])

        return Vector(result)

    def scalar_multiply(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")

        result = []

        for component in self.components:
            result.append(component * scalar)

        return Vector(result)

    def dot_product(self, other):
        if self.dimension() != other.dimension():
            raise ValueError("Vectors must have the same dimension.")

        total = 0

        for i in range(self.dimension()):
            total += self.components[i] * other.components[i]

        return total

    def cross_product(self, other):
        if self.dimension() != 3 or other.dimension() != 3:
            raise ValueError("Cross product is available only for 3D vectors.")

        a = self.components
        b = other.components

        return Vector([
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        ])

    def projection(self, other):
        if self.dimension() != other.dimension():
            raise ValueError("Vectors must have the same dimension.")

        denominator = other.magnitude() ** 2

        if denominator == 0:
            raise ValueError("Cannot project onto the zero vector.")

        coefficient = self.dot_product(other) / denominator

        return other.scalar_multiply(coefficient)

    def angle_with(self, other):
        if self.dimension() != other.dimension():
            raise ValueError("Vectors must have the same dimension.")

        magnitude_product = self.magnitude() * other.magnitude()

        if magnitude_product == 0:
            raise ValueError("Angle cannot be calculated with a zero vector.")

        cosine = self.dot_product(other) / magnitude_product

        # Prevent tiny floating-point errors
        cosine = max(-1, min(1, cosine))

        return math.degrees(math.acos(cosine))

    def __str__(self):
        return str(self.components)