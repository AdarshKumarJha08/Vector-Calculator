# Vector Mathematics Calculator

A menu-driven Python application for performing common mathematical operations on 2D and 3D vectors.

## 📌 Project Overview

The **Vector Mathematics Calculator** is a Python-based project designed to perform various vector calculations through a simple command-line interface.

The project uses **Object-Oriented Programming (OOP)** and a **multi-file modular structure** to keep different responsibilities organized.

## ✨ Features

The calculator supports the following operations:

* Vector Magnitude
* Unit Vector
* Vector Addition
* Vector Subtraction
* Scalar Multiplication
* Dot Product
* Cross Product
* Projection of One Vector onto Another
* Angle Between Two Vectors
* Calculation History
* Clear Calculation History
* Input Validation
* Support for 2D and 3D vectors

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Python Modules
* File Handling
* Exception Handling
* Mathematical Functions

## 📂 Project Structure

```text
Vector_Calculator/
│
├── main.py
├── vector.py
├── operations.py
├── input_handler.py
├── history.py
├── history.txt
└── README.md
```

### File Descriptions

**`main.py`**
The main entry point of the application. It displays the menu, coordinates different modules, and manages the overall program flow.

**`vector.py`**
Contains the `Vector` class and the core vector-related functionality such as magnitude, addition, subtraction, dot product, cross product, projection, and angle calculation.

**`operations.py`**
Provides functions that connect the main program with the operations implemented by the `Vector` class.

**`input_handler.py`**
Handles user input, input validation, vector creation, scalar input, and menu-choice validation.

**`history.py`**
Handles saving, displaying, and clearing calculation history using a text file.

**`history.txt`**
Stores previously performed calculations.

**`README.md`**
Contains information about the project, its features, structure, and usage.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python installation using:

```bash
python --version
```

### 2. Open the Project Folder

Open a terminal or command prompt inside the project folder.

### 3. Run the Program

Execute:

```bash
python main.py
```

The calculator menu will appear in the terminal.

## 🧮 Example

For example, if the user enters:

```text
Vector A = [1, 2, 3]
Vector B = [4, 5, 6]
```

The calculator can perform operations such as:

```text
A + B = [5, 7, 9]

A · B = 32

A × B = [-3, 6, -3]
```

The results can also be stored in the calculation history.

## 🧠 Concepts Demonstrated

This project demonstrates several fundamental Python and programming concepts:

* Classes and Objects
* Constructors (`__init__`)
* Instance methods
* Encapsulation
* Modules and imports
* Lists
* Loops
* Conditional statements
* Functions
* Exception handling
* File handling
* Mathematical operations
* Input validation
* Modular programming

## ⚠️ Limitations

* The calculator currently supports only **2D and 3D vectors**.
* Cross product is available only for **3D vectors**.
* The application currently uses a command-line interface rather than a graphical interface.

## 🎯 Purpose of the Project

The purpose of this project is to apply Python programming concepts to a practical mathematical application while demonstrating Object-Oriented Programming, modular programming, input validation, and file handling.

## 👨‍💻 Author

**Adarsh Jha**

B.Tech CSE (AI/ML)
VIT Bhopal University

## 📄 License

This project was created for educational purposes.
