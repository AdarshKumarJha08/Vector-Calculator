from vector import Vector

def add_vectors(vector_a, vector_b):
    return vector_a.add(vector_b)

def subtract_vectors(vector_a, vector_b):
    return vector_a.subtract(vector_b)

def scalar_multiply(vector, scalar):
    return vector.scalar_multiply(scalar)

def dot_product(vector_a, vector_b):
    return vector_a.dot_product(vector_b)

def cross_product(vector_a, vector_b):
    return vector_a.cross_product(vector_b)

def projection(vector_a, vector_b):
    return vector_a.projection(vector_b)

def angle_between(vector_a, vector_b):
    return vector_a.angle_with(vector_b)