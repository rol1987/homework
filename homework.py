class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Иван', 'Иванович', 'М')
best_student.courses_in_progress += ['Excel']
best_student.courses_in_progress += ['Java']

best_lec = Lecturer('Роман', 'Романович')
best_lec.courses_attached += ['Excel']
best_lec.courses_attached += ['Java']
 
best_student.rate_lecturer(best_lec, 'Excel', 9)
best_student.rate_lecturer(best_lec, 'Java', 9)
best_student.rate_lecturer(best_lec, 'Python', 10)

print(best_lec.grades)