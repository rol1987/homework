class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # temp = lecturer.grades

    def __str__(self):
      return (f"Имя: {self.name}\nФамилия: {self.surname}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
  
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")   

class Lecturer(Mentor):
    grades = {}
    def __init__(self):

      
class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



student_1 = Student('Иван', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']

reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'Java', 5)
reviewer_1.rate_homework(student_1, 'Excel', 6)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print("-----------------\n")

lecturer_1 = Lecturer('Сидор', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 8)
student_1.rate_lecturer(lecturer_1, 'Excel', 2)
print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print("-----------------\n")

print(student_1)

print(reviewer_1)

print(lecturer_1)