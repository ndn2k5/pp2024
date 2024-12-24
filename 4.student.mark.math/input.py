from domains.student import Student
from domains.course import Course
from domains.marks import Mark

def input_student_info():
    students = []
    num_student = int(input("Enter number of students: "))
    for _ in range(num_student):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        students.append(Student(student_id, name, dob))
    return students

def input_course_info():
    courses = []
    num_course = int(input("Enter number of courses: "))
    for _ in range(num_course):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        courses.append(Course(course_id, name, credit))
    return courses

def input_marks(students, courses):
    marks = []
    print("\nEnter marks for each student in a selected course: ")
    for course in courses:
        print(f"\nCourse: {course.name} (id: {course.course_id})")
        for student in students:
            mark = float(input(f"Enter mark for student {student.name} (id: {student.student_id}): "))
            student.add_mark(mark, course.credit)
            marks.append(Mark(course.course_id, student.student_id, mark))
    return marks