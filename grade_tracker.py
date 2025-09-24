# Student Grade Tracker
def add_student(tracker, student_name):
    if student_name not in tracker:
        tracker[student_name] = {}
        print("Added student:", student_name)
    else:
        print("Student", student_name, "is already in the tracker!")

def add_grade(tracker, student_name, subject, grade):
    if student_name in tracker:
        tracker[student_name][subject] = grade
        print("Added grade", grade, "for", student_name, "in", subject)
    else:
        print("Student", student_name, "not found! Add them first.")

def calculate_average(tracker, student_name):
    if student_name in tracker:
        grades = tracker[student_name].values()
        if grades:
            average = sum(grades) / len(grades)
            print(student_name, "has an average grade of", round(average, 2))
            return average
        else:
            print("No grades found for", student_name)
            return 0
    else:
        print("Student", student_name, "not found!")
        return 0

def display_grades(tracker):
    if not tracker:
        print("No students in the tracker.")
        return
    for student, subjects in tracker.items():
        print("Student:", student)
        for subject, grade in subjects.items():
            print("  ", subject, ":", grade)
        calculate_average(tracker, student)

while True:
    print("\n=== Student Grade Tracker ===")
    print("1. Add a new student")
    print("2. Add or update a grade")
    print("3. Calculate a student's average")
    print("4. Show all grades")
    print("5. Exit")
    
    choice = input("Pick an option (1-5): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        add_student(grade_tracker, name)
    
    elif choice == "2":
        name = input("Enter student name: ")
        subject = input("Enter subject (e.g., Math): ")
        try:
            grade = float(input("Enter grade (e.g., 85): "))
            add_grade(grade_tracker, name, subject, grade)
        except ValueError:
            print("Oops! Please enter a number for the grade.")
    
    elif choice == "3":
        name = input("Enter student name: ")
        calculate_average(grade_tracker, name)
    
    elif choice == "4":
        display_grades(grade_tracker)
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Pick a number from 1 to 5.")
        
