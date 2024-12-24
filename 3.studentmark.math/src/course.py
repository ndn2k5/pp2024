class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __repr__(self):
        return f"Course(course_id={self.course_id}, name='{self.name}', credits={self.credits})"