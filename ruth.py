"""
Student Record Management System
Course: PROG211 - Object-Oriented Programming 1

This program demonstrates:
- Classes and objects
- Attributes and methods
- Dictionary data structure
- Instance methods
- Class methods
- Basic input validation
"""


class Student:
    """Represents an individual student."""

    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_info(self):
        """Display the student's information."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

    def update_course(self, new_course):
        """Update the student's course."""
        self.course = new_course

    @classmethod
    def create_student(cls, student_id, name, course):
        """Create and return a new Student object."""
        return cls(student_id, name, course)


class StudentRecordSystem:
    """Manages student records using a dictionary."""

    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, course):
        """Add a student to the dictionary."""

        if student_id in self.students:
            print("Error: This student ID already exists.")
            return

        student = Student.create_student(
            student_id, name, course
        )

        self.students[student_id] = student
        print("Student registered successfully.")

    def display_students(self):
        """Display all registered students."""

        if not self.students:
            print("No student records available.")
            return

        print("\n--- REGISTERED STUDENTS ---")

        for student in self.students.values():
            print("---------------------------")
            student.display_info()

    def search_student(self, student_id):
        """Search for a student using the student ID."""

        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
        else:
            print("\n--- STUDENT FOUND ---")
            student.display_info()

    def update_student_course(self, student_id, new_course):
        """Update a student's course."""

        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
        else:
            student.update_course(new_course)
            print("Student course updated successfully.")

    def count_students(self):
        """Return the total number of registered students."""
        return len(self.students)

    def run(self):
        """Display the menu and process user choices."""

        while True:
            print("\n==============================")
            print(" STUDENT RECORD MANAGEMENT")
            print("==============================")
            print("1. Register a student")
            print("2. Display all students")
            print("3. Search for a student")
            print("4. Update a student's course")
            print("5. Count registered students")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                student_id = input(
                    "Enter student ID: "
                ).strip()

                name = input("Enter student name: ").strip()
                course = input("Enter course: ").strip()

                if not student_id or not name or not course:
                    print("Error: All fields are required.")
                else:
                    self.add_student(
                        student_id, name, course
                    )

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                student_id = input(
                    "Enter student ID to search: "
                ).strip()

                self.search_student(student_id)

            elif choice == "4":
                student_id = input(
                    "Enter student ID: "
                ).strip()

                new_course = input(
                    "Enter new course: "
                ).strip()

                if not new_course:
                    print("Error: Course cannot be empty.")
                else:
                    self.update_student_course(
                        student_id, new_course
                    )

            elif choice == "5":
                total = self.count_students()
                print("Total registered students:", total)

            elif choice == "6":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Please select 1-6.")


# Start the program.
if __name__ == "__main__":
    system = StudentRecordSystem()
    system.run()