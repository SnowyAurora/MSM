# pst2_main.py - The Persistent Application

import json
import datetime

DATA_FILE = "msms.json"
app_data = {} # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file."""
    global app_data
    try:
        with open(path, 'r') as f:
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }

def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file."""
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")


# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, specialty):
    """Adds a teacher dictionary to the data store."""
    teacher_id = app_data['next_teacher_id']
    new_teacher = {"id": teacher_id, "name": name, "specialty": specialty}
    app_data['teachers'].append(new_teacher)
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' (ID: {teacher_id}) added.")

def update_teacher(teacher_id, specialty):
    """Finds a teacher by ID and updates their data with provided fields."""
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            teacher.update({"specialty": specialty})
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            teacher.pop("id")
            teacher.pop("name")
            teacher.pop("specialty")
            print(f"Teacher removed from Database.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def add_student(name, instruments):
    """Adds a student dictionary to the data store."""
    student_id = app_data['next_student_id']
    new_student = {"id": student_id, "name": name, "instruments": instruments}
    app_data['students'].append(new_student)
    app_data['next_student_id'] += 1
    print(f"Core: Student '{name}' (ID : {student_id}) added.")

def update_student(student_id, instruments):
    """Finds a student then updates their data with the given fields"""
    for student in app_data['students']:
        if student['id'] == student_id:
            # Uses the provided fields to update the student data with the .update() method
            student.update({"instruments": instruments})
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")


def remove_student(student_id):
    """Removes a student from the data store."""
    # .remove doesn't exist.
    for student in app_data['students']:
        if student['id'] == student_id:
            student.pop("id")
            student.pop("name")
            student.pop("instruments")
            print(f"Student removed from database.")
            return
    print(f"Error: Student with ID {student_id} not found.")


# --- New Receptionist Features ---
def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course."""
    if timestamp is None:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
    
    # Looks horrible but it will do
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}, at {timestamp}")

def print_student_card(student_id):
    """Creates a text file badge for a student."""
    student_to_print = None
    for student in app_data['students']:
        if student['id'] == student_id:
            student_to_print = student
            break
    
    if student_to_print:
        filename = f"{student_id}_card.txt"
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {student_to_print['instruments']}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")


# --- Main Application Loop ---
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("5. Add Student")
        print("6. Update Student Info")
        print("7. Remove Teacher")
        print("8. Add Teacher Info")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            userinput = input("Checking in! Enter the Student's ID: ")
            try: 
                student_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            course_id = input("Enter the Course: ")
            check_in(student_id, course_id)
            made_change = True
        elif choice == '2':
            userinput = input("Enter Student ID: ")
            try: 
                student_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            print_student_card(student_id)
            pass
        elif choice == '3':
            userinput = input("Enter Teacher's ID: ")
            try: 
                teacher_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            specialty = input("Enter New Specialty: ")
            update_teacher(teacher_id, specialty)
            # TODO: BUGTEST
            made_change = True
        elif choice == '4':
            userinput = input("Enter Student ID: ")
            try: 
                student_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            remove_student(student_id)
            # TODO: BUGTEST
            made_change = True
        elif choice == '5':
            name = input("Enter New Student's Name: ")
            instruments = input("Enter instruments: ")
            add_student(name, instruments)
            made_change = True
        elif choice == '6':
            userinput = input("Enter Student's ID: ")
            try: 
                student_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            instruments = input("Enter student's new course: ")
            update_student(student_id, instruments)
            made_change = True
        elif choice == '7':
            userinput = input("Enter the ID of the teacher we are removing : ")
            try: 
                teacher_id = int(userinput)
            except ValueError:
                print("Invalid input.")
            remove_teacher(teacher_id)
            made_change = True
        elif choice == '8':
            name = input("Please enter the New Teacher's Name: ")
            specialty = input("Enter the new Teacher's Specialty: ")
            add_teacher(name, specialty)
            made_change = True
        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()