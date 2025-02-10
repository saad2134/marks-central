from admin import setup_admin, admin_login
from data_handler import load_data
from student_operations import enter_marks, remove_student, calculate_average

def main():
    setup_admin()
    students = load_data()
    if not admin_login():
        return
    
    while True:
        print("1. Enter Marks")
        print("2. Remove Student")
        print("3. Calculate Average Marks")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            enter_marks(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Exiting...\n")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
