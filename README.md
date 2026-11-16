Student Record Management System

Project Description

The Student Record Management System is a simple command-line application developed using Python for the PROG211 – Object Oriented Programming Methods 1 assignment.

The project demonstrates how Object-Oriented Programming (OOP) can be applied to manage student information efficiently. It allows users to register students, display records, search for students, update course information, and count registered students.

Project Overview

The system manages the following student information:

* Student ID
* Student Name
* Course of Study

Student information is represented using objects and stored in a Python dictionary, with each student’s ID serving as a unique dictionary key.

Key Features

The application provides the following functionalities:

1. Register a Student: Add a new student record to the system.
2. Display All Students: View all registered student records.
3. Search for a Student: Find a student’s information using their ID.
4. Update Student’s Course: Modify the course associated with a registered student.
5. Count Registered Students: Display the total number of registered students.
6. Exit: Close the application.

Object-Oriented Programming Concepts

The project demonstrates the following fundamental OOP concepts:

* Classes: The Student and StudentRecordSystem classes organise the program’s data and functionalities.
* Objects: A Student object is created whenever a new student is registered.
* Attributes: The Student class contains attributes for student ID, name, and course.
* Instance Methods: The display_info() method displays student details, while update_course() modifies a student’s course.
* Class Method: The project demonstrates the use of a class method defined with the @classmethod decorator.
* Dictionary: A Python dictionary stores student objects, using student IDs as keys.

System Requirements

To run this application, you need:

* Python 3 installed on your computer.
* A terminal or command prompt.
* Visual Studio Code or another Python-compatible code editor (optional).

Note: The project does not require any third-party Python packages according to its documented implementation.

Installation and Execution

Follow these steps to run the application:

1. Clone or download this repository from GitHub.
2. Open the project folder in Visual Studio Code or your preferred code editor.
3. Locate the Python source code file.
4. Open the terminal in the project directory.
5. Execute the program using the following command:

python ruth.py

Alternatively, on systems that use Python 3 as a separate command, run:

python3 ruth.py

Note: Replace ruth.py with the actual name of the Python source file if it is different.

6. Follow the instructions displayed in the terminal and select your preferred operation from the main menu.

Application Menu

When the application runs, users are presented with the following menu:

================================
    STUDENT RECORD MANAGEMENT
================================
1. Register a student
2. Display all students
3. Search for a student
4. Update a student's course
5. Count registered students
6. Exit
Enter your choice:

Data Storage

The application uses an in-memory Python dictionary to store student objects. Each student ID serves as a key, allowing the system to retrieve and manage individual student records.

The current implementation does not document database integration or permanent file storage. Therefore, student records may need to be entered again after the application is closed.

GitHub Repository

Project Source Code:
https://github.com/Ruthmajua/O.O.P_Assignment1_905006005.git

Project Information

Category	Details
Course Code	PROG211
Course Title	Object Oriented Programming Methods 1
Assignment Title	Student Record Management System
Institution	Limkokwing University of Creative Technology, Sierra Leone
Faculty	Information Communication and Technology
Programming Language	Python 3

References

* Python Software Foundation. The Python Tutorial
* Python Software Foundation. Classes in Python
* GitHub. GitHub Documentation
* Digital Public Goods Alliance. Digital Public Goods Standard

⸻

Developed as part of the PROG211 – Object Oriented Programming Methods 1 assignment.
