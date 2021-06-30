class Student:
    def __init__(self, name, surname, gender, av_hw_grade=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.av_hw_grade = av_hw_grade
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def count_av_hw_grade(self):
        sum_hw_grade, grades_qty = 0, 0
        for grades in self.grades.values():
            for grade in grades:
                sum_hw_grade += grade
                grades_qty += 1
        av_hw_grade = sum_hw_grade / grades_qty
        return av_hw_grade

    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rate:
                lecturer.rate[course] += [grade]
            else:
                lecturer.rate[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        prt = f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.count_av_hw_grade()}\nКурсы " \
              f"В процессе изучения: {self.grades.keys()}\nЗавершенные курсы: {self.finished_courses}"
        return prt

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент!")
            return
        return self.count_av_hw_grade() < other.count_av_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        if isinstance(self, Reviewer):
            prt = f'Имя: {self.name} \nФамилия: {self.surname}'
            return prt
        elif isinstance(self, Lecturer):
            sum_lect_grade, grades_qty = 0, 0
            for grades in self.rate.values():
                for grade in grades:
                    sum_lect_grade += grade
                    grades_qty += 1
            av_grade = sum_lect_grade / grades_qty
            prt = f'Имя: {self.name} \nФамилия: {self.surname}\nСредний балл: {av_grade}'
            return prt


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate = {}

    def count_av_lect_grade(self):
        sum_lect_grade, grades_qty = 0, 0
        for grades in self.rate.values():
            for grade in grades:
                sum_lect_grade += grade
                grades_qty += 1
        av_lect_grade = sum_lect_grade / grades_qty
        return av_lect_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор!")
            return
        return self.count_av_lect_grade() < other.count_av_lect_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Иван', 'Крыльев', 'муж')
student2 = Student('София', 'Ковальская', 'жен')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']

lecturer1 = Lecturer('Индиана', 'Джонс')
lecturer2 = Lecturer('Иван', 'Павлов')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Git', 6)
student2.rate_lecturer(lecturer1, 'Python', 9)

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Mister', 'Twister')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Git', 5)
reviewer2.rate_hw(student2, 'Git', 7)


print(f"Средний бал {student1.name} {student1.surname}: {student1.count_av_hw_grade()}")
print(f"Средний бал {student2.name} {student2.surname}: {student2.count_av_hw_grade()}")
print(f"student1 < student2: {student1 < student2}")
print()
print(f"Средний бал лектора {lecturer1.name} {lecturer1.surname}: {lecturer1.count_av_lect_grade()}")
print(f"Средний бал лектора {lecturer2.name} {lecturer2.surname}: {lecturer2.count_av_lect_grade()}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")












# print(best_student.courses_in_progress)
#
# cool_reviewer = Reviewer('Some', 'Buddy')
# cool_reviewer.courses_attached += ['Python']
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
#
# cool_lecturer = Lecturer('Indiana', 'Jones')
# cool_lecturer.courses_attached += ['Python']
# cool_lecturer.courses_attached += ['Git']
# print(cool_reviewer.courses_attached)
# best_student.rate_lecturer(cool_lecturer, 'Python', 10)
# best_student.rate_lecturer(cool_lecturer, 'Git', 8)
# best_student.rate_lecturer(cool_lecturer, 'Python', 9)
#
# print(best_student.name, best_student.surname, "hw grades: ", best_student.grades)
# print(cool_lecturer.name, cool_lecturer.surname, "'s lectures grades: ", cool_lecturer.rate)
# print(cool_lecturer)
# print()
# print(best_student)
