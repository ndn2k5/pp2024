class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __repr__(self):
        return f"Course(ID: {self.course_id}, Name: {self.name}, Credit: {self.credit})"