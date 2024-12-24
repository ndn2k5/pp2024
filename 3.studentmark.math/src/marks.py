from math import floor
import numpy as np

class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = self.round_down(mark)

    def round_down(self, mark):
        return floor(mark * 10) / 10

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def calculate_gpa(self, course_credits):
        total_weighted_marks = sum(mark.mark * course_credits[mark.course_id] for mark in self.marks)
        total_credits = sum(course_credits[mark.course_id] for mark in self.marks)
        return total_weighted_marks / total_credits if total_credits > 0 else 0

def sort_students_by_gpa(students, course_credits):
    return sorted(students, key=lambda student: student.calculate_gpa(course_credits), reverse=True)