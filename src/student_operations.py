import statistics
from data_handler import load_data, save_data

def enter_marks(students):
    name = input("\nEnter student name: ")
    marks = input("Enter marks separated by spaces: ").split()
    students[name] = [float(mark) for mark in marks]
    save_data(students)
    print(f"Marks entered for {name}.\n")

def remove_student(students):
    name = input("\nEnter student name to remove: ")
    if name in students:
        del students[name]
        save_data(students)
        print(f"\n{name} has been removed from the system.\n")
    else:
        print("\nStudent not found!\n")

def calculate_average(students):
    if not students:
        print("\nNo students in the system.\n")
        return
    
    for name, marks in students.items():
        avg = statistics.mean(marks)
        print(f"\n{name}'s average marks: {avg:.2f}")
    print()
