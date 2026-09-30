from vector import Vector

def get_vector(name):
    while True:
        try:
            values = input(
                f"Enter the components of {name} "
                "(separated by spaces): "
            ).split()

            components = [float(value) for value in values]

            return Vector(components)

        except (ValueError, TypeError) as error:
            print(f"Invalid input: {error}")
            print("Please enter a valid 2D or 3D vector.\n")


def get_scalar():
    while True:
        try:
            return float(input("Enter the scalar: "))

        except ValueError:
            print("Invalid scalar. Please enter a number.\n")


def get_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= 12:
                return choice

            print("Please enter a number between 1 and 12.")

        except ValueError:
            print("Invalid choice. Please enter a number.")