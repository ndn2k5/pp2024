class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = []
        self.credits = []

    def add_mark(self, mark, credit):
        self.marks.append(mark)
        self.credits.append(credit)

    def calculate_gpa(self):
        if not self.marks or not self.credits:
            return 0.0
        weighted_sum = sum(mark * credit for mark, credit in zip(self.marks, self.credits))
        total_credits = sum(self.credits)
        return round(weighted_sum / total_credits, 1)

    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, DOB: {self.dob})"