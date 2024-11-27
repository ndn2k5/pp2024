students = []
courses = []
marks = {}

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    students.append({'id': student_id, 'name': name, 'dob': dob})

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append({'id': course_id, 'name': name})

def select_course_and_input_marks():
    course_id = input("Enter course ID to input marks: ")
    if course_id not in marks:
        marks[course_id] = {}
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark

def list_courses():
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students():
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks_for_course():
    course_id = input("Enter course ID to show marks: ")
    if course_id in marks:
        for student_id, mark in marks[course_id].items():
            student = next((s for s in students if s['id'] == student_id), None)
            if student:
                print(f"Student ID: {student_id}, Name: {student['name']}, Mark: {mark}")
    else:
        print("No marks available for this course.")

# Example usage
num_students = input_number_of_students()
for _ in range(num_students):
    input_student_info()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_course_info()

select_course_and_input_marks()
list_courses()
list_students()
show_student_marks_for_course()