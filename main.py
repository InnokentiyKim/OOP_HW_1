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
            return "Ошибка"
        
    def _get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grade in self.grades.values():
            grades_sum += sum(grade)
            grades_count += len(grade)
        return grades_sum / grades_count
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_average_grade()}\n"
                f"Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}")    
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() == other._get_average_grade()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() < other._get_average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() <= other._get_average_grade()
        return NotImplemented


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grade in self.grades.values():
            grades_sum += sum(grade)
            grades_count += len(grade)
        return grades_sum / grades_count
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_average_grade()}"
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() == other._get_average_grade()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() < other._get_average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() <= other._get_average_grade()
        return NotImplemented


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
