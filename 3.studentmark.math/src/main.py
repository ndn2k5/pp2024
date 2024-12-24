from student import Student
from course import Course
from marks import Mark
import numpy as np
import math
import curses

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        # Implementation for inputting student information
        pass

    def input_course_info(self):
        # Implementation for inputting course information
        pass

    def input_marks(self):
        # Implementation for inputting marks
        pass

    def list_students(self):
        # Implementation for listing students
        pass

    def list_courses(self):
        # Implementation for listing courses
        pass

    def show_student_marks(self):
        # Implementation for showing student marks
        pass

    def calculate_gpa(self, student_id):
        student_marks = [mark for mark in self.marks if mark.student_id == student_id]
        total_credits = sum(course.credit for course in self.courses if course.id in [mark.course_id for mark in student_marks])
        weighted_sum = sum(mark.mark * next(course.credit for course in self.courses if course.id == mark.course_id) for mark in student_marks)
        return round(weighted_sum / total_credits, 1) if total_credits > 0 else 0.0

    def sort_students_by_gpa(self):
        gpa_list = [(student, self.calculate_gpa(student.id)) for student in self.students]
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        return gpa_list

    def main(self):
        self.input_student_info()
        self.input_course_info()
        self.input_marks()
        self.list_students()
        self.list_courses()
        self.show_student_marks()

if __name__ == "__main__":
    school = School()
    curses.wrapper(school.main)