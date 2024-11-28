def input_students():
    # Tạo một danh sách rỗng để lưu trữ thông tin sinh viên.
    student_list = []
    # Nhập số lượng sinh viên từ người dùng.
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        # Nhập ID của sinh viên.
        student_id = input("Enter student ID: ")
        # Nhập tên của sinh viên.
        student_name = input("Enter student name: ")
        # Nhập ngày sinh của sinh viên.
        student_dob = input("Enter student date of birth: ")
        # Thêm thông tin sinh viên vào danh sách dưới dạng từ điển.
        student_list.append({"id": student_id, "name": student_name, "dob": student_dob})
    # Trả về danh sách sinh viên đã nhập.
    return student_list

def input_courses():
    # Tạo một danh sách rỗng để lưu trữ thông tin khóa học.
    course_list = []
    # Nhập số lượng khóa học từ người dùng.
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        # Nhập ID của khóa học.
        course_id = input("Enter course ID: ")
        # Nhập tên của khóa học.
        course_name = input("Enter course name: ")
        # Thêm thông tin khóa học vào danh sách dưới dạng từ điển.
        course_list.append({"id": course_id, "name": course_name})
    # Trả về danh sách khóa học đã nhập.
    return course_list

def input_marks(students, courses):
    # Tạo danh sách rỗng để lưu trữ điểm của sinh viên.
    marks = []
    # Duyệt qua từng khóa học trong danh sách.
    for course in courses:
        # Duyệt qua từng sinh viên trong danh sách.
        for student in students:
            # Nhập điểm cho sinh viên theo từng khóa học.
            mark = int(input(f"Enter mark for student {student['name']} in course {course['name']}: "))
            # Thêm điểm vào danh sách dưới dạng từ điển, bao gồm ID sinh viên, ID khóa học và điểm.
            marks.append({"student_id": student['id'], "course_id": course['id'], "mark": mark})
    # Trả về danh sách điểm đã nhập.
    return marks

def display_courses(courses):
    # Hiển thị danh sách các khóa học.
    print("Course list:")
    for course in courses:
        # In thông tin ID và tên của từng khóa học.
        print(f"ID: {course['id']}, Name: {course['name']}")

def display_students(students):
    # Hiển thị danh sách các sinh viên.
    print("Student list:")
    for student in students:
        # In thông tin ID, tên và ngày sinh của từng sinh viên.
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def display_marks(courses, students, marks):
    # Hiển thị danh sách điểm của các sinh viên.
    print("Student marks:")
    for mark in marks:
        # Tìm thông tin sinh viên tương ứng với ID trong danh sách điểm.
        student = next((s for s in students if s['id'] == mark['student_id']), None)
        # Tìm thông tin khóa học tương ứng với ID trong danh sách điểm.
        course = next((c for c in courses if c['id'] == mark['course_id']), None)
        if student and course:
            # In ra tên sinh viên, tên khóa học và điểm.
            print(f"Student: {student['name']}, Course: {course['name']}, Mark: {mark['mark']}")

# Ví dụ sử dụng các hàm trên.
students = input_students()  # Gọi hàm nhập thông tin sinh viên.
courses = input_courses()    # Gọi hàm nhập thông tin khóa học.
display_courses(courses)     # Hiển thị danh sách khóa học.
display_students(students)   # Hiển thị danh sách sinh viên.
marks = input_marks(students, courses)  # Nhập điểm cho sinh viên.
display_marks(courses, students, marks) # Hiển thị danh sách điểm.
