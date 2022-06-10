class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = sum(self.grades.values())/len(self.grades)

    def add_courses(self, course_name):
            self.finished_course.append(course_name)
            
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\
               \nСредняя оценка за домашние задания: {self.average_grade}\
               \nКурсы в процессе изучения: {", ".join(self.courses_in_progress}\
               \nЗаконченные курсы: {", ".join(self.finished_courses}"

    def __lt__(self,other):
        return self.average_grade < other.average_grade
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    


class Lecturer(Mentor):
    def __init__(self):
        self.grades = []
        self.average_grade = sum(self.grades)/len(self.grades)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average_grade}"

    def __lt__(self,other):
        return self.average_grade < other.average_grade 
        
   

class Reviewer(Mentor):
    def __init__(self):
        pass
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


