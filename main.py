
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def average_grade(self):
        return round(sum(map(lambda i:sum(i),self.grades.values()))/len(self.grades),2)

    def add_courses(self, course_name):
            self.finished_courses.append(course_name)
            
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        n = ", ".join(self.courses_in_progress)
        m = ", ".join(self.finished_courses)
        x = Student.average_grade(self)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\
               \nСредняя оценка за домашние задания: {x}\
               \nКурсы в процессе изучения: {n}\
               \nЗаконченные курсы: {m}")

    def __lt__(self,other):
        return self.average_grade() < other.average_grade()
    

class Mentor: 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    


class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}

    

    def average_grade(self):
        return round(sum(map(lambda i:sum(i),self.grades.values()))/len(self.grades),2)
        


        
    
    def __str__(self):
        x = Lecturer.average_grade(self)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {x}"

    def __lt__(self,other):
        return self.average_grade() < other.average_grade()
        
   

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

#Создаю по 2 экземляра класса
S1 = Student("Иван","Царевич","мужской")
S1.finished_courses = ["C","C++"]
S1.courses_in_progress = ["Git","Pandas","Python"]
S1.grades = {"Python":[9,8], "C":[7,10],"C++":[8,10,7]}
S2 = Student("Василиса","Прекрасная","женский")
S2.finished_courses = ["Python", "C","C++"]
S2.courses_in_progress = ["Git","Pandas"]
S2.grades = {"Python":[6,8], "C":[10,10],"C++":[10,10,7]}
M1 = Mentor("Николай","Николаев")
M1.courses_attached = ["Python","Git"]
M2 = Mentor("Тимофей","Тимофеев")
M2.courses_attached = ["Python","Git","C++"]
L1 = Lecturer()
L1.name = "Алберт"
L1.surname = "Энштейн"
L1.courses_attached = ["Python","Git","C++"]
L1.grades = {"Python":[8,9],"Git":[10],"C++":[7,7]}
L2 = Lecturer()
L2.name = "Стив"
L2.surname = "Джобс"
L2.courses_attached = ["Python","C","C++"]
L2.grades = {"Python":[10,7],"C":[8],"C++":[8,9,10]}
R1 = Reviewer()
R1.name = "Эл"
R1.surname = "Баньё"
R1.courses_attached = ["Python","Git","C"]
R2 = Reviewer()
R2.name = "Грег"
R2.surname = "Даян"
R2.courses_attached = ["C++","Git","C"]

#Вызов всех методов
print(S2)
print()
print(S1)
print()
S1.add_courses("JS")
print()
print(S1)
print()
print(L1)
print()
S1.rate_lecturer(L1, "Python", 10)
print()
print(L1)
print()
R1.rate_hw(S1, "Python", 9)
print()
print(S1)
print()
print(L2)
print()
print(R1)
print()
print(R2)
print()
print(L1<L2)
print(S1<S2)
print()
                    
def average_student_grade_course(student_list,course):
    average_grade_course = {}
    for student in student_list:
        if course in student.grades.keys():
            if course  in average_grade_course.keys():
                average_grade_course[course]+=student.grades[course]
            else:
                average_grade_course[course]=student.grades[course]
    print(f"For course {course} the student's av grade is {sum(average_grade_course[course])/len(average_grade_course[course])}")

average_student_grade_course([S1,S2],"Python")


def average_lecturer_grade_course(lecturer_list,course):
    average_grade_course = {}
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            if course  in average_grade_course.keys():
                average_grade_course[course]+=lecturer.grades[course]
            else:
                average_grade_course[course]=lecturer.grades[course]
    print(f"For course {course} the lecturer's av grade is {sum(average_grade_course[course])/len(average_grade_course[course])}")

average_lecturer_grade_course([L1,L2],"Python")
