# MSMS.py - The In-Memory Prototype

# DB's (Database), DO NOT TOUCH!!!
STUDENT_DATA = []
TEACH_DATA = []
NEXT_INCREMENT_STUDENT_ID = 1
NEXT_INCREMENT_TEACHER_ID = 1

# Basic Data Structures
class Student:
    """Student Data"""
    def __init__(self, student_id, name, instrument):
        self.id = student_id
        self.name = name
        self.instrument = instrument
        # Temp Store for Student Data, to be appended to DB's
        self.enrolled_in = []

class Teacher:
    """Teacher Data"""
    def __init__(self, teacher_id, name, speciality):
        self.id = teacher_id
        self.name = name
        self.speciality = speciality
        # Temp Data Store, NO TOUCHY
        self.employee_in = []
        

# ------ Backend Functions ------
def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database."""
    global NEXT_INCREMENT_TEACHER_ID
    # Creates a new string that stores a Teacher's data
    new_teacher = Teacher(NEXT_INCREMENT_TEACHER_ID, name, speciality)
    # Function to add a new Teacher to the Database
    TEACH_DATA.append(new_teacher)
    # Increments the index value of the database
    NEXT_INCREMENT_TEACHER_ID += 1
    print(f"Core: Teacher '{name}', (ID : {NEXT_INCREMENT_TEACHER_ID - 1}) added successfully.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not STUDENT_DATA:
        print("No students in the system.")
        return
    # Loops through STUDENT_DATA. For each student, prints their ID, name, and their enrolled_in list.
    for student in STUDENT_DATA:
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    """Prints all teachers in the database."""
    # Loops through TEACHER_DATA. For each student, prints their ID, name, and their specialty list.
    print("\n--- Teacher List ---")
    for teacher in TEACH_DATA:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")


def find_students(term):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{term}' ---")
    list_1 = []
    for student in STUDENT_DATA:
        if student.name == term:
            list_1.append(student)
    if not list_1:
            print("No Match Found")
    for student in list_1:
        print(f"Name : {student.name} - ID : {student.id} - Enrolled in : {student.instrument}")
    # TODO: Create an empty list to store results.
    # Loop through STUDENT_DATA. If the search 'term' (case-insensitive) is in the student's name,
    # add them to your results list.
    # After the loop, if the results list is empty, print "No match found."
    # Otherwise, print the details for each student in the results list.
    # TODO: ADD FUZZY SEARCH FUNCTION (EVENTUALLY) (NOT NOW) (NEEDS A NEW LIBRARY WHICH I AM NOT EQUIPPED TO DO RIGHT NOW)
    

def find_teachers(term):
    """Finds teachers by name or speciality."""
    print(f"\n--- Finding Teachers matching '{term}' ---")
    list_2 = []
    for teacher in TEACH_DATA:
        if teacher.name == term:
            list_2.append(teacher)
        if teacher.speciality == term:
            list_2.append(teacher)
    if not list_2:
            print("No Match Found")
    for teacher in list_2:
        print(f"Name : {teacher.name} - ID : {teacher.id} - Enrolled in : {teacher.speciality}")
    # TODO: Implement this function similar to find_students, but check
    # for the term in BOTH the teacher's name AND their speciality.


# --- Front Desk Functions ---
def find_student_by_id(student_id):
    """A new helper to find one student by their exact ID."""
    # Loops through STUDENT_DATA. If a student's ID matches student_id, return the student object.
    for student in STUDENT_DATA:
        if student.id == student_id:
            return student
    # If the loop does not find a matching student ID, returns this value
    return None

def front_desk_register(name, instrument):
    """High-level function to register a new student and enrol them."""
    global NEXT_INCREMENT_STUDENT_ID
    # Creates a new Student object, add it to STUDENT_DATA, and increment the ID.
    new_student = Student(NEXT_INCREMENT_STUDENT_ID, name, instrument)
    STUDENT_DATA.append(new_student)
    NEXT_INCREMENT_STUDENT_ID += 1
    
    # Prints out the new student's name, ID and enrolled instrument
    front_desk_enrol(new_student.id, instrument)
    print(f"Front Desk: Successfully registered '{name}' (ID : {NEXT_INCREMENT_STUDENT_ID - 1}) and enrolled them in '{instrument}'.")

def front_desk_enrol(student_id, instrument):
    """High-level function to enrol an existing student in a course."""
    # Finds the student by the inputted ID
    student = find_student_by_id(student_id)
    # Appends the new instrument to the student's enrollment data
    if student:
        student.enrolled_in.append(instrument)
        print(f"Front Desk: Enrolled student {student_id} in '{instrument}'.")
    else:
        # Error Message Printout
        print(f"Error: Student ID {student_id} not found.")

def front_desk_lookup(term):
    """High-level function to search everything."""
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term)
    find_teachers(term)

    # --- Main Application ---
def main():
    """Runs the main interactive menu for the receptionist."""
    # Pre-populate some data for easy testing
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")

    while True:
        print("\n===== Music School Front Desk =====")
        print("1. Register New Student")
        print("2. Enrol Existing Student")
        print("3. Lookup Student or Teacher")
        print("4. (Admin) List all Students")
        print("5. (Admin) List all Teachers")
        print("q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompts for Name and Instrument from the receptionist.
            name = input("Enter student name: ")
            instrument = input("Enter instrument to enrol in: ")
            front_desk_register(name, instrument)
        elif choice == '2':
            # Prompts for student ID (as an int) and the instrument that will be added to the student, then calls the front_desk_enrol function.
            try:
                student_id = int(input("Enter student ID: "))
                instrument = input("Enter instrument to enrol in: ")
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '3':
            # Prompts for a search term, then calls front_desk_lookup.
            term = input("Enter search term: ")
            front_desk_lookup(term)
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_teachers()
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# --- Program Start ---
if __name__ == "__main__":
    main()