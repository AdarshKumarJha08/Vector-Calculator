from input_handler import get_vector, get_scalar, get_choice

from operations import add_vectors, subtract_vectors, scalar_multiply, dot_product, cross_product, projection, angle_between

from history import save_history, show_history, clear_history

def display_vector(vector):
    print(f"Vector: {vector}")

def main():
    print("=" * 50)
    print("        VECTOR MATHEMATICS CALCULATOR")
    print("=" * 50)

    while True:
# giving the user an breif about which number means what.
        print("\nChoose an operation:")
        print("1. Magnitude")
        print("2. Unit Vector")
        print("3. Addition")
        print("4. Subtraction")
        print("5. Scalar Multiplication")
        print("6. Dot Product")
        print("7. Cross Product")
        print("8. Projection")
        print("9. Angle Between Vectors")
        print("10. Show History")
        print("11. Clear History")
        print("12. Exit")

        choice = get_choice()

        try:
            if choice == 1 :
                vector = get_vector("the vector")
                print(f"Magnitude = {vector.magnitude()}")
                save_history(f"The magnitude of vector{vector} is:", vector.magnitude())
#It will print the magnitude of the vector.

            elif choice == 2 :
                vector = get_vector("the vector")
                result = vector.unit_vector()
                print(f"Unit Vector = {result}")
                save_history(f"The unit vector of vector{vector} is:", result)
# it will print unit vector of the given vector.

            elif choice == 3 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.add(vector_b)
                print(f"A + B = {result}")
                save_history(f"The addition of vector{vector_a} and vector{vector_b} is:", result)
# it will print the addition of 2 vectors.

            elif choice == 4 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.subtract(vector_b)
                print(f"A - B = {result}")
                save_history(f"The sustraction of vector{vector_a} and vector{vector_b} is:", result)
# it will print the subs. of two vectors.

            elif choice == 5 :
                vector = get_vector("the vector")
                scalar = get_scalar()
                result = vector.scalar_multiply(scalar)
                print(f"Result = {result}")
                save_history(f"The scalar multiplication of vector{vector} is:", result)
# it will print the vector multiplied by a scalar.

            elif choice == 6 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.dot_product(vector_b)
                print(f"A · B = {result}")
                save_history(f"The dot product of vector{vector_a} and vector{vector_b} is:", result)
# It will print the dot product of 2 vectors.

            elif choice == 7 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.cross_product(vector_b)
                print(f"A x B = {result}")
                save_history(f"The cross product of vector{vector_a} and vector{vector_b} is:", result)
# iT will print the cross product of 2 vectors.
#                 
            elif choice == 8 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.projection(vector_b)
                print(f"Projection of A onto B = {result}")
                save_history(f"The projection of vector{vector_a} on vector{vector_b} is:", result)
# It will print the projection of vector a on vector b.

            elif choice == 9 :
                vector_a = get_vector("Vector A")
                vector_b = get_vector("Vector B")
                result = vector_a.angle_with(vector_b)
                print(f"Angle between A and B = {result} degrees")
                save_history(f"The angle between vector{vector_a} and vector{vector_b} is:", result)
# it will print the angle between 2 vectors.

            elif choice == 10 :
                show_history()
# Will display the history.

            elif choice == 11 :
                clear_history()
# Will clear the past records.

            elif choice == 12 :
                print("\nThank you for using Vector Mathematics Calculator!")
                print("GOODBYE! 👋")
                break

        except (ValueError, TypeError) as error:
            print(f"\nError: {error}")

if __name__ == "__main__":
    main()