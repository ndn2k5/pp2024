from domains.student import Student
from domains.course import Course
from domains.marks import Mark
import numpy as np
import math
import curses
from input import input_student_info, input_course_info, input_marks
from output import display_menu, show_students

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        self.students = input_student_info()

    def input_course_info(self):
        self.courses = input_course_info()

    def input_marks(self):
        self.marks = input_marks(self.students, self.courses)

    def list_students(self):
        print("\nList of students: ")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of courses: ")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        student_id = input("Enter student id: ")
        for course in self.courses:
            for mark in self.marks:
                if mark.course_id == course.course_id and mark.student_id == student_id:
                    print(f"Course: {course.name}, Mark: {mark.mark}")

    def calculate_gpa(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            return student.calculate_gpa()
        return 0.0

    def sort_students_by_gpa(self):
        gpa_list = [(student, self.calculate_gpa(student.student_id)) for student in self.students]
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        return gpa_list

    def main(self, stdscr):
        self.input_student_info()
        self.input_course_info()
        self.input_marks()
        self.list_students()
        self.list_courses()
        self.show_student_marks()

if __name__ == "__main__":
    school = School()
    curses.wrapper(school.main)