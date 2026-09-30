# Vector Calculator — Project Statement

## 1. Project Title
**Vector Calculator**

## 2. Project Overview
The Vector Calculator is a Python-based modular program designed to perform common vector operations through a simple and organized menu-driven interface. The program allows users to enter vectors, perform mathematical calculations, view previous calculations, and clear the stored history.

The project is developed using a modular programming approach, where different functionalities can be separated into appropriate modules. This makes the program easier to understand, maintain, test, and extend.

## 3. Objectives
The main objectives of this project are:

- To implement common mathematical operations on vectors using Python.
- To demonstrate modular programming concepts.
- To provide a simple menu-driven interface for users.
- To reduce repetitive manual calculations.
- To maintain a history of previously performed operations.
- To provide an option to clear the calculation history.

## 4. Features and Operations

The Vector Calculator provides the following features:

### 4.1 Vector Addition
Adds two or more compatible vectors component-wise.

**Example:**

For vectors:

`A = (a₁, a₂, a₃)`

`B = (b₁, b₂, b₃)`

The result is:

`A + B = (a₁ + b₁, a₂ + b₂, a₃ + b₃)`

### 4.2 Vector Subtraction
Subtracts the corresponding components of one vector from another.

`A - B = (a₁ - b₁, a₂ - b₂, a₃ - b₃)`

### 4.3 Magnitude of a Vector
Calculates the magnitude or length of a vector.

For a three-dimensional vector:

`A = (a₁, a₂, a₃)`

the magnitude is:

`|A| = √(a₁² + a₂² + a₃²)`

### 4.4 Scalar Multiplication
Multiplies every component of a vector by a given scalar value.

`kA = (ka₁, ka₂, ka₃)`

where `k` is the scalar.

### 4.5 Vector Product
Calculates the cross product of two three-dimensional vectors.

`A × B`

The result is a vector perpendicular to both input vectors.

### 4.6 Dot Product
Calculates the scalar product of two vectors.

`A · B = a₁b₁ + a₂b₂ + a₃b₃`

The result is a scalar value.

### 4.7 Projection
Calculates the projection of one vector onto another vector.

The vector projection of `A` onto `B` is:

`proj_B(A) = (A · B / |B|²) B`

The program should handle invalid cases such as projection onto a zero vector appropriately.

### 4.8 Angle Between Two Vectors
Calculates the angle between two vectors using the dot product formula:

`cos θ = (A · B) / (|A||B|)`

Therefore:

`θ = cos⁻¹((A · B) / (|A||B|))`

The result can be displayed in degrees.

### 4.9 Show History
Displays the calculations that have been performed during the current program session.

The history may contain information such as:
- Operation performed
- Input vectors/values
- Calculated result

### 4.10 Clear History
Provides an option to remove all previously stored calculation history from the current session.

## 5. Modular Programming Approach
The project follows a modular structure so that individual operations can be organized separately rather than placing the entire program in one large block of code.

A possible structure is:

```text
Vector-Calculator/
│
├── main.py
├── vector_operations.py
├── history.py
└── README.md
```

### `main.py`
Acts as the main entry point of the program. It displays the menu, accepts user choices, takes input, and calls the required functions.

### `vector_operations.py`
Contains the mathematical functions required for vector calculations, such as:
- Addition
- Subtraction
- Magnitude
- Scalar multiplication
- Vector product
- Dot product
- Projection
- Angle calculation

### `history.py`
Handles the history-related functionality, including:
- Storing previous calculations
- Displaying history
- Clearing history

> The exact number and names of modules may vary depending on the final implementation.

## 6. Input
The program accepts inputs such as:

- Vector components
- Scalar values
- Menu choices
- Options for viewing or clearing history

The program should validate inputs wherever necessary to avoid invalid mathematical operations or unexpected program termination.

## 7. Output
The program displays:

- Results of selected vector operations
- Appropriate messages for invalid inputs
- Calculation history
- Confirmation when history is cleared

## 8. Error Handling
The program should handle common invalid cases, including:

- Invalid menu choices
- Incorrect numerical input
- Vectors with incompatible dimensions
- Division by zero
- Magnitude of a zero vector where required
- Projection onto a zero vector
- Angle calculation involving a zero vector

Clear and understandable error messages should be displayed to the user.

## 9. Sample Menu

```text
========== VECTOR CALCULATOR ==========

1. Addition
2. Subtraction
3. Magnitude
4. Scalar Multiplication
5. Vector Product
6. Dot Product
7. Projection
8. Angle Between Two Vectors
9. Show History
10. Clear History
11. Exit

Enter your choice:
```

## 10. Example

For:

`A = (1, 2, 3)`

`B = (4, 5, 6)`

The program can perform operations such as:

**Addition**

`A + B = (5, 7, 9)`

**Subtraction**

`A - B = (-3, -3, -3)`

**Dot Product**

`A · B = 32`

**Magnitude of A**

`|A| = √14`

The exact output format depends on the implementation.

## 11. Technologies Used

- **Programming Language:** Python
- **Programming Concept:** Modular Programming
- **Interface:** Command-line / menu-driven interface
- **Data Handling:** Python lists/tuples and appropriate data structures for history

## 12. Advantages

- Simple and easy-to-use interface.
- Performs multiple vector calculations in one program.
- Modular structure makes the code easier to maintain.
- Calculation history helps users review previous results.
- Demonstrates practical use of mathematical concepts in Python.
- Can be extended with additional vector operations in the future.

## 13. Future Scope

Possible future improvements include:

- Support for vectors of different dimensions where mathematically applicable.
- Graphical user interface (GUI).
- Saving calculation history permanently to a file.
- Loading previously saved history.
- Additional vector operations.
- Matrix calculations.
- Unit/vector visualization using graphs.
- More advanced input validation.

## 14. Conclusion
The Vector Calculator is a practical Python modular programming project that combines programming concepts with fundamental vector mathematics. It provides operations such as addition, subtraction, magnitude, scalar multiplication, vector product, dot product, projection, and angle calculation, along with history management features.

The project demonstrates how a mathematical problem can be converted into a structured Python application using separate modules and reusable functions.
