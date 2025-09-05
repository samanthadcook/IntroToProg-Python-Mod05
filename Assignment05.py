# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Samantha Cook, 9-4-2025, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
file = None
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, 'r')
except FileNotFoundError as e:
    print(f"Could not find file: {FILE_NAME}")
    print("JSON file must exist before running this script!]\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    students.append(student_data)
file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        student_first_name = input("Please enter the student's first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers!")
        student_last_name = input("What is the student's last name? ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")
        student_data = [student_first_name,student_last_name,course_name]
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*100)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*100)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        try:
            for student in students:
                json_data = f"{student[0]},{student[1]},{student[2]}\n"
                file.write(json_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        except Exception as e:
            print(f"An error occurred while writing data: {str(e)}")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("exiting the program")
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
