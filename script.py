from enum import nonmember


#Compartment 1 - All the database and stored values being used in the whole project
#Compartment 2 - Consists of the Menu and its working
#Compartmenet 3 - Consists the code for the function "Add student" and all the different cases
#Compartment 4 - Consists the code for the function "Enroll Course" and all the different cases
#Compartment 5 - Consists the code for the function "Drop course" and all the different cases
#/---------------------------------------------------------Compartment 1---------------------------------------------------------------------------------------------------------------------------\


courses = {"C101": "Mathematics", "C102" : "Programming", "C103": "History"}
students={}

# \----------------------------------------------------------------------------------------------------------------------------------------------------------/




#/---------------------------------------------------------Compartment 2---------------------------------------------------------------------------------------------------------------------------\

def add_student(student_id, name):  # Defining a function to add student into the database
    global students  # Edits the global dictionary of students
    if student_id in students:  # This if else block checks the database if it already has the same id or not, if it does it will not add the new data in the database and give error
        print("Record cannot be added the same student id already exists!")
    else:
        students[student_id] = {
            "name": name,
            "courses": {},
        }
        print("Successfully added")

# \----------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 3---------------------------------------------------------------------------------------------------------------------------\

def enroll_course(std_id, course):
    if std_id not in students:
        print("Student ID does not exist!")

    elif course not in courses:
        print("Course does not exist!")

    else:
        students[std_id]["courses"][course] = None
        print("Successfully enrolled.")
# \----------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 4---------------------------------------------------------------------------------------------------------------------------\

def drop_course(std_id, course):
    global students
    if std_id not in students:
        print("Student ID does not exist!")

    elif course not in courses:
        print("Course does not exist!")
    elif course not in students[std_id]["courses"]:
        print("Student is not enrolled in this course!")
    else:
        students[std_id]["courses"].pop(course, None)
        print("Successfully dropped.")

# \------------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 5---------------------------------------------------------------------------------------------------------------------------\

def all_courses():
    return print(courses)

# \-----------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 6---------------------------------------------------------------------------------------------------------------------------\

def record_grade(std_id, course, grade):
    if std_id not in students:
        print("Student ID does not exist!")
    elif course not in courses:
        print("Course does not exist!")
    elif course not in students[std_id]["courses"]:
        print("Student is not enrolled in this course!")
    else:
        students[std_id]["courses"][course] = grade
        print("Successfully recorded.")

 #\--------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 7--------------------------------------------------------------------------------------------------------------------------\

def calculate_gpa(std_id):
    student = students[std_id]
    marks = 0
    count = 0
    if std_id not in students:
        print("Student ID does not exist!")
    else:
        for course in student['courses']:

            grade = student['courses'][course]

            if grade is not None:
                marks += grade
                count += 1
            else:
                print("No valid grades found, can't calculate GPA!")
    if count == 0:
        return 0
    return marks / count


#\----------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 8---------------------------------------------------------------------------------------------------------------------------\

def transcript(std_id):
    if std_id not in students:
        print("Student ID does not exist!")
    else:
        print(students[std_id]["courses"])
        print("GPA: ", calculate_gpa(std_id))


# \---------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 9---------------------------------------------------------------------------------------------------------------------------\

def check_honors_eligibility(std_id):
    student = students[std_id]
    for course in student['courses']:

        grade = student['courses'][course]

        if grade < 90:
            print("Not eligible")
            break
    else:
        print("Eligible for Honors")


 # Error: SHould be inside the else block

# \----------------------------------------------------------------------------------------------------------------------------------------/


# /-------------------------------Compartment 10-------------------------------------------\
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

        Choice = input("Enter your choice: ")

# \------------------------------------------------------------------------------------------/


# /--------------------------------------Compartment 11------------------------------------------------------------------------------------\

        if Choice == "1":
            print("Enter the Student ID and Name of the student you want to add:")
            student_id = input("Student ID: ")                  #Line 42 and 43 takes input form the user for the new student id and name
            name = input("Student Name: ")

            add_student(student_id, name)               #Calls the function

# \----------------------------------------------------------------------------------------------------------------------------------------/


# /-----------------------------------------------Compartment 12------------------------------------------------------------------\
        elif Choice == "2":
            print("Input the student id whom you want to enroll to the course")
            std_id = input("Student ID: ")
            print(courses)
            Course = input("Course ID: ").upper()

            enroll_course(std_id,Course)

            pass
# \-------------------------------------------------------------------------------------------------------------------------------/


# /-----------------------------------------Compartment 13-------------------------------------------------------------------------\
        elif Choice == "3":
            print("Input the student id whom you want to drop from the course")
            std_id = input("Student ID: ")
            print("Enter the course id")
            course = input("Course ID: ").upper()
            drop_course(std_id, course)  #Calling the function
            pass
 # \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 14--------------------------------------------------------------------------\

        elif Choice == "4":
            all_courses()
            pass

# \-------------------------------------------------------------------------------------------------------------------------------/


# /--------------------------------------------Compartment 15--------------------------------------------------------------------------\

        elif Choice == "5":
            std_id = input("Student ID: ")
            course = input("Course ID: ").upper()
            grade = int(input("Grade: "))                #Error, doesnt find out if the subject already exists and if it doesnt it jut adds it to the dictionary by it self, this shouldnt happen
            record_grade(std_id, course, grade)
            pass


# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 16--------------------------------------------------------------------------\

        elif Choice == "6":
                std_id = input("Student ID: ")
                gpa = calculate_gpa(std_id)
                print(gpa)
                pass
# /--------------------------------------------Compartment 17--------------------------------------------------------------------------\

        elif Choice == "7":
            std_id = input("Student ID: ")
            transcript(std_id)
            pass
# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 18--------------------------------------------------------------------------\

        elif Choice == "8":
            std_id = input("Student ID: ")
            check_honors_eligibility(std_id)

# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 19--------------------------------------------------------------------------\

        elif Choice == "9":
            print(students)

# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 20--------------------------------------------------------------------------\

        elif Choice == "10":
            print("Exiting system. Goodbye!")
            break
# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 21--------------------------------------------------------------------------\

        else:
            print("Invalid choice. Please try again.")

# \-------------------------------------------------------------------------------------------------------------------------------/


# /--------------------------------------------Compartment 21--------------------------------------------------------------------------\


add_student("S001", "Alice")
add_student("S002", "Bob")
enroll_course("S001", "C101")
add_student("a", "a")
enroll_course("a", "C101")
enroll_course("a", "C102")
record_grade("a", "C101", 90)
record_grade("a", "C102", 90)
menu()
# \-------------------------------------------------------------------------------------------------------------------------------/
#Make function  outside  the if else loop then call the function in the loop and not define it
#Course enrolling twice doesnt show but should give error
