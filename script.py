
#/-----------------------------------Compartment 1------------------------------------------\

courses = {"C101": "Mathematics", "C102" : "Programming", "C103": "History"}
students={}
stu_error = "Student ID does not exist!"
cou_error = "Course does not exist!"

#\----------------------------------End of Compartment 1-----------------------------------/


#/---------------------------------Compartment 2----------------------------------------------------\
def std_id():
    student_id = input("Enter Student ID: ").upper()
    return student_id

def cou_id():
    course_id = input("Enter Course ID: ").upper()
    return course_id


def add_student(student_id, name):  # Defining a function to add student into the database
    if student_id in students:  # This if else block checks the database if it already has the same id or not, if it does it will not add the new data in the database and give error
        print("Record cannot be added the same student id already exists!")
        return
    else:
        students[student_id] = {
            "name": name,
            "courses": {},
        }
        print("Successfully added")

def enroll_course(student_id, course):  # Function defined to enroll students into a specific course
    if student_id not in students:   #Case check if student id exists or not
        print(stu_error)
        return

    elif course not in courses:  #Case check if a valid course is input
        print(cou_error)
        return

    elif course in students[student_id]["courses"]:   # Case check whether the student is already enrolled in the course or not
        print("Student already enrolled in this course!")
        return

    else:
        students[student_id]["courses"][course] = None  #Enrolls the student into the input course
        print("Successfully enrolled.")



def drop_course(student_id, course):  # Function defining from dropping a student from a course
    if student_id not in students:  #Case check for student id
        print(stu_error)
        return

    elif course not in courses:  #Case check for course id
        print(cou_error)
        return
    elif course not in students[student_id]["courses"]:  # case check whether the student is enrolled in course or not
        print("Student is not enrolled in this course!")
        return
    else:
        students[student_id]["courses"].pop(course, None)  # if all checks pass, removes the student from the course
        print("Successfully dropped.")


def view_courses():  #Function defined to view all the courses
    print("\nAvailable Courses:")
    for course_id, course_name in courses.items():
        print(course_id, "-", course_name)


def record_grade(student_id, course, grade): #Function defined to record grades for a student for input course
    if student_id not in students: # Checks student id exists or not
        print(stu_error)
        return
    elif course not in courses: # Checks for course id
        print(cou_error)
        return
    elif course not in students[student_id]["courses"]:  # Checks whether the student is enrolled in the input course or not
        print("Student is not enrolled in this course!")
        return
    elif grade < 0 or grade > 100: # Check whether the grade is a valid number
        print("Invalid grade!")
        return
    else:
        students[student_id]["courses"][course] = grade  # Records grade
        print("Successfully recorded.")


def calculate_gpa(student_id):  #Function defined to calculate gpa for the give student id
    if student_id not in students: # Checks student id exists or not
        print(stu_error)
        return 0

    student = students[student_id]
    marks = 0 # Variable
    count = 0 # Variable

    for course in student['courses']:
        grade = student['courses'][course]

        if grade is not None:
            marks += grade # Adds grade if it exists for a course into marks so at the end all the total of marks is stored in marks
            count += 1 # Increase count by 1 everytime it finds a valid grade so it can find out the gpa properly using the formula marks/number of courses

    if count == 0: # To prevent zero error
        return None

    return marks / count

def transcript(student_id): # Function defined to generate the transcript of the given student id
    if student_id not in students:
        print(stu_error)
        return

    print("\nTranscript for:", students[student_id]["name"])

    for course, grade in students[student_id]["courses"].items():  #Acesses course and grade for the given student in the dictionary
        if grade is None:
            print(course, "- Not graded")
        else:
            print(course, "-", grade)

    gpa = calculate_gpa(student_id)
    if gpa is not None:  #Checks whether GPA exists or not
        print("GPA:", gpa)

def check_honors_eligibility(student_id):
    if student_id not in students:  #Checks if student id exists
        print(stu_error)
        return

    if not students[student_id]["courses"]:   #Checks whether the given student id is enrolled in any courses or not, if yes then it moves on, if not then it gives error
        print("Not eligible for Honors")
        return
    student = students[student_id]  # variable for student id

    for course in student['courses']: #Acceses the courses enrolled of the given student id

        grade = student['courses'][course] #Checks the grade of the course and stores the value

        if grade is None or grade < 90:   # checks whether the value is above 90 or below
            print("Not eligible for Honors")
            break
    else:
        print("Eligible for Honors")

def view_students():  #Function for viewing all the enrolled students
    if students == {}:  # Case check to check whether there are any students enrolled or not, if not it gives back error
        print("No students available.")
        return

    for student_id in students: #acceses student id in the dictionary
        print("Student ID:", student_id)
        print("Name:", students[student_id]["name"])

        if students[student_id]["courses"] == {}:
            print("Courses: None")
        else:
            print("Courses:")
            for course in students[student_id]["courses"]:
                grade = students[student_id]["courses"][course]
                if grade is None:
                    print(course, "- Not graded")
                else:
                    print(course, "-", grade)

        print()

def menu():      #Menu for the management system to choose what task we have to do
    while True:
        print("\n--- Student Course Management System ---")
        print("1. Add Student")
        print("2. Enroll Course")
        print("3. Drop Course")
        print("4. View Courses")
        print("5. Record Grade")
        print("6. Calculate GPA")
        print("7. Show Transcript")
        print("8. Check Honors Eligibility")
        print("9. View all students")
        print("10. Exit")

        choice = input("Enter your choice: ")

#\-------------------------------------------End of compartment 2---------------------------------------/

#/---------------------------------------------Compartment 3----------------------------------------------\

        if choice == "1":
            print("Enter the Student ID and Name of the student you want to add:")
            student_id = std_id()
            name = input("Student Name: ") #takes input for name

            add_student(student_id, name)               #Calls the function

        elif choice == "2":
            print("Input the student id whom you want to enroll to the course")
            student_id = std_id()
            view_courses()
            course = cou_id()

            enroll_course(student_id,course)


        elif choice == "3":
            print("Input the student id whom you want to drop from the course")
            student_id = std_id()
            print("Enter the course id")
            course = cou_id()
            drop_course(student_id, course)  #Calling the function

        elif choice == "4":
            view_courses()

        elif choice == "5":
            student_id = std_id()
            course = cou_id()
            grade_input = input("Enter your grade: ") #Takes input from the user for grade
            if grade_input.isdigit(): #Case check to check if the input it a valid number or not
                grade = int(grade_input)
                record_grade(student_id, course, grade)
            else:
                print("Please enter a number for the grade.")

        elif choice == "6":
             student_id= std_id()
             gpa = calculate_gpa(student_id)
             if gpa is None:  # Case check to check if the gpa is non zero
                 print("Cannot calculate GPA: no grades recorded.")
             else:
                 print("The GPA is:", gpa)

        elif choice == "7":
            student_id = std_id()
            transcript(student_id)


        elif choice == "8":
            student_id = std_id()
            check_honors_eligibility(student_id)


        elif choice == "9":
            view_students()


        elif choice == "10":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Test cases-
print(add_student("S001", "Alice"))
print(add_student("S002", "Bob"))
print(enroll_course("S001", "C101"))
print(record_grade("S001", "C101", 90))
print(transcript("S001"))

menu()
#\-------------------------------------------End of Compartment 3--------------------------------/


