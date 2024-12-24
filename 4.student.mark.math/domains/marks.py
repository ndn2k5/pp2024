class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark

    def __repr__(self):
        return f"Mark(Course ID: {self.course_id}, Student ID: {self.student_id}, Mark: {self.mark})"