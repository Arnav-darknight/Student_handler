from enum import nonmember


#Compartment 1 - All the database and stored values being used in the whole project
#Compartment 2 - Consists of the Menu and its working
#Compartmenet 3 - Consists the code for the function "Add student" and all the different cases
#Compartment 4 - Consists the code for the function "Enroll Course" and all the different cases
#Compartment 5 - Consists the code for the function "Drop course" and all the different cases
#/---------------------------------------------------------Compartment 1---------------------------------------------------------------------------------------------------------------------------\


courses = {"C101": "Mathematics", "C102" : "Programming", "C103": "History"}
students={}
stu_error = "Student ID does not exist!"
cou_error = "Course does not exist!"

# \----------------------------------------------------------------------------------------------------------------------------------------------------------/

def std_id():
    student_id = input("Enter Student ID: ")
    return student_id

def cou_id():
    course_id = input("Enter Course ID: ").upper()
    return course_id


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

def enroll_course(student_id, course):
    if student_id not in students:
        print(stu_error)

    elif course not in courses:
        print(cou_error)

    else:
        students[student_id]["courses"][course] = None
        print("Successfully enrolled.")
# \----------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 4---------------------------------------------------------------------------------------------------------------------------\

def drop_course(student_id, course):
    global students
    if student_id not in students:
        print(stu_error)

    elif course not in courses:
        print(cou_error)
    elif course not in students[student_id]["courses"]:
        print("Student is not enrolled in this course!")
    else:
        students[student_id]["courses"].pop(course, None)
        print("Successfully dropped.")

# \------------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 5---------------------------------------------------------------------------------------------------------------------------\

def all_courses():
    return print(courses)

# \-----------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 6---------------------------------------------------------------------------------------------------------------------------\

def record_grade(student_id, course, grade):
    if student_id not in students:
        print(stu_error)
    elif course not in courses:
        print(cou_error)
    elif course not in students[student_id]["courses"]:
        print("Student is not enrolled in this course!")
    else:
        students[student_id]["courses"][course] = grade
        print("Successfully recorded.")

 #\--------------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 7--------------------------------------------------------------------------------------------------------------------------\

def calculate_gpa(student_id):
    student = students[student_id]
    marks = 0
    count = 0
    if student_id not in students:
        print(stu_error)
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

def transcript(student_id):
    if student_id not in students:
        print(stu_error)
    else:
        print(students[student_id]["courses"])
        print("GPA: ", calculate_gpa(student_id))


# \---------------------------------------------------------------------------------------------------------------------------------------------------/


#/---------------------------------------------------------Compartment 9---------------------------------------------------------------------------------------------------------------------------\

def check_honors_eligibility(student_id):
    student = students[student_id]
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
            student_id = std_id()                #Line 42 and 43 takes input form the user for the new student id and name
            name = input("Student Name: ")

            add_student(student_id, name)               #Calls the function

# \----------------------------------------------------------------------------------------------------------------------------------------/


# /-----------------------------------------------Compartment 12------------------------------------------------------------------\
        elif Choice == "2":
            print("Input the student id whom you want to enroll to the course")
            student_id = std_id()
            print(courses)
            Course = cou_id()

            enroll_course(student_id,Course)


# \-------------------------------------------------------------------------------------------------------------------------------/


# /-----------------------------------------Compartment 13-------------------------------------------------------------------------\
        elif Choice == "3":
            print("Input the student id whom you want to drop from the course")
            student_id = std_id()
            print("Enter the course id")
            course = cou_id()
            drop_course(student_id, course)  #Calling the function

 # \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 14--------------------------------------------------------------------------\

        elif Choice == "4":
            all_courses()


# \-------------------------------------------------------------------------------------------------------------------------------/


# /--------------------------------------------Compartment 15--------------------------------------------------------------------------\

        elif Choice == "5":
            student_id = std_id()
            course = cou_id()
            grade = int(input("Grade: "))                #Error, doesnt find out if the subject already exists and if it doesnt it jut adds it to the dictionary by it self, this shouldnt happen
            record_grade(student_id, course, grade)



# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 16--------------------------------------------------------------------------\

        elif Choice == "6":
             student_id= std_id()
             gpa = calculate_gpa(student_id)
             print(gpa)
# /--------------------------------------------Compartment 17--------------------------------------------------------------------------\

        elif Choice == "7":
            student_id = input("Student ID: ")
            transcript(student_id)

# \-------------------------------------------------------------------------------------------------------------------------------/

# /--------------------------------------------Compartment 18--------------------------------------------------------------------------\

        elif Choice == "8":
            student_id = std_id()
            check_honors_eligibility(student_id)

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
