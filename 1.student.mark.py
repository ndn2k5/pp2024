student_list = []
course_list = []
marks_data = []
#Nhap thong tin sinh vien
def input_student_info():
    num_student = int(input("Enter number of students: "))
    for i in range(num_student):
        student = {}
        student['id'] = input("Enter student id: ")
        student['name'] = input("Enter student name: ")
        student['dob'] = input("Enter student dob: ")
        student_list.append(student)
#Nhap thong tin khoa hoc
def input_course_info():
    num_course = int(input("Enter number of courses: "))
    for i in range(num_course):
        course = {}
        course['id'] = input("Enter course id: ")
        course['name'] = input("Enter course name: ")
        course['credit'] = int(input("Enter course credit: "))
        course_list.append({"id": course['id'], "name": course['name'], "credit": course['credit']})
#Nhap diem cua sinh vien
def input_marks():
    print("\n Enter marks for each student in a selected course: ")
    for course in course_list:
        print(f"\ncourse: {course['name']}  (id: {course['id']})")
        course_marks = {}
        for student in student_list:
            mark = float(input(f"Enter mark for student {student['name']} (id: {student['id']}): "))
            course_marks[student['id']] = mark
        marks_data.append({course['id']: course_marks})
#Ham liet ke danh sach sinh vien
def list_student():
    print("\nList of students: ")
    for student in student_list:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")
#Ham liet ke danh sach khoa hoc
def list_course():
    print("\nList of courses: ")
    for course in course_list:
        print(f"ID: {course['id']}, Name: {course['name']}, Credit: {course['credit']}")
def show_student_marks():
    student_id = input("Enter student id: ")
    for course in course_list:
        for marks in marks_data:
            if course['id'] in marks and student_id in marks[course['id']]:
                print(f"Course: {course['name']}, Mark: {marks[course['id']][student_id]}")
#Ham main
def main():
    input_student_info()
    input_course_info()
    input_marks()
    list_student()
    list_course()
    show_student_marks()
if __name__ == "__main__":
    main()