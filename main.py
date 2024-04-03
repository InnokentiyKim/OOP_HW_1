class Student:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course: str, grade: int):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def _get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grade in self.grades.values():
            grades_sum += sum(grade)
            grades_count += len(grade)
        if grades_count:
            return grades_sum / grades_count
        else:
            return 0
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_average_grade()}\n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}")    
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() == other._get_average_grade()
        return "Ошибка типов"
    
    def __ne__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() != other._get_average_grade()
        return "Ошибка типов"
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() < other._get_average_grade()
        return "Ошибка типов"
    
    def __gt__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() > other._get_average_grade()
        return "Ошибка типов"
    
    def __le__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() <= other._get_average_grade()
        return "Ошибка типов"
    
    def __ge__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() >= other._get_average_grade()
        return "Ошибка типов"


class Mentor:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grade in self.grades.values():
            grades_sum += sum(grade)
            grades_count += len(grade)
        if grades_count:
            return grades_sum / grades_count
        else:
            return 0
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_average_grade()}"
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() == other._get_average_grade()
        return "Ошибка типов"
    
    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() != other._get_average_grade()
        return "Ошибка типов"
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() < other._get_average_grade()
        return "Ошибка типов"
    
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() > other._get_average_grade()
        return "Ошибка типов"
    
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() <= other._get_average_grade()
        return "Ошибка типов"
    
    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() >= other._get_average_grade()
        return "Ошибка типов"


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def homeworks_aver_grade(students: list, course: str) -> float:
    grades_sum = 0
    grades_count = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades_sum += sum(student.grades[course])
            grades_count += len(student.grades[course])
    if grades_count:
        return grades_sum / grades_count
    else:
        return 0


def lectures_aver_grade(lecturers: list, course: str) -> float:
    grades_sum = 0
    grades_count = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades_sum += sum(lecturer.grades[course])
            grades_count += len(lecturer.grades[course])
    if grades_count:
        return grades_sum / grades_count
    else:
        return 0


cool_student = Student("Василий", "Петров", "мужской")
cool_student.courses_in_progress += ['Python', 'Java']
cool_student.finished_courses += ['HTML/CSS']
best_student = Student("Татьяна", "Иванова", "женский")
best_student.courses_in_progress += ['Python', 'JS', 'Java']
best_student.finished_courses += ['Motivation']
cool_lecturer = Lecturer("Сергей", "Крылов")
cool_lecturer.courses_attached += ['Python', 'Java']
best_lecturer = Lecturer("Анна", "Васильева")
best_lecturer.courses_attached += ['JS']
cool_reviewer = Reviewer("Петр", "Смирнов")
cool_reviewer.courses_attached += ['Python', 'JS']
best_reviewer = Reviewer("Ирина", "Грандова")
best_reviewer.courses_attached += ['Java']
cool_student.rate_lecturer(cool_lecturer, 'Python', 9)
cool_student.rate_lecturer(cool_lecturer, 'Java', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Java', 10)
best_student.rate_lecturer(best_lecturer, 'JS', 9)
best_student.rate_lecturer(best_lecturer, 'JS', 10)
best_student.rate_lecturer(best_lecturer, 'JS', 8)
cool_reviewer.rate_hw(cool_student, 'Python', 9)
cool_reviewer.rate_hw(cool_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'JS', 7)
best_reviewer.rate_hw(cool_student, 'Java', 9)
best_reviewer.rate_hw(cool_student, 'Java', 7)
best_reviewer.rate_hw(best_student, 'Java', 10)
best_reviewer.rate_hw(best_student, 'Java', 10)

print('Студенты:')
print(cool_student)
print(best_student)
print('Лекторы:')
print(cool_lecturer)
print(best_lecturer)
print('Эксперты:')
print(cool_reviewer)
print(best_reviewer)
print('Сравнение студентов по средней оценке за дз:')
print(f'{cool_student.name} == {best_student.name}: ', cool_student == best_student)
print(f'{cool_student.name} != {best_student.name}: ', cool_student != best_student)
print(f'{cool_student.name} < {best_student.name}: ', cool_student < best_student)
print(f'{cool_student.name} <= {best_student.name}: ', cool_student <= best_student)
print(f'{cool_student.name} > {best_student.name}: ', cool_student > best_student)
print(f'{cool_student.name} >= {best_student.name}: ', cool_student >= best_student)
print('Сравнение лекторов по средней оценке за лекции:')
print(f'{cool_lecturer.name} == {best_lecturer.name}: ', cool_lecturer == best_lecturer)
print(f'{cool_lecturer.name} != {best_lecturer.name}: ', cool_lecturer != best_lecturer)
print(f'{cool_lecturer.name} < {best_lecturer.name}: ', cool_lecturer < best_lecturer)
print(f'{cool_lecturer.name} <= {best_lecturer.name}: ', cool_lecturer <= best_lecturer)
print(f'{cool_lecturer.name} > {best_lecturer.name}: ', cool_lecturer > best_lecturer)
print(f'{cool_lecturer.name} >= {best_lecturer.name}: ', cool_lecturer >= best_lecturer)
students_list = [cool_student, best_student]
lecturers_list = [cool_lecturer, best_lecturer]
active_courses = set(sum([student.courses_in_progress for student in students_list], []))
for course in active_courses:
    print(f'По курсу {course}:')
    print(f'Средняя оценка за домашние задания {homeworks_aver_grade(students_list, course)}')
    print(f'Средняя оценка за лекции {lectures_aver_grade(lecturers_list, course)}')