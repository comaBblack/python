import math as m

#eazy_2
class triangle:
    def __init__(self, a1, b1, a2, b2, a3, b3):
      self.a1 = a1
      self.b1 = b1
      self.a2 = a2
      self.b2 = b2
      self.a3 = a3
      self.b3 = b3

      
    
    #площадь
    def pl(self):
        self.S = abs(float((self.a1 - self.a3)*(self.b2 - self.b3) - (self.a2 - self.a3)*(self.b1 - self.b3)))/2
    #периметр
    def per(self):
        self.P = float(m.sqrt((self.a2 - self.a1)**2 + (self.b2 - self.b1)**2) + m.sqrt((self.a3 - self.a1)**2 + (self.b3 - self.b1)**2) + m.sqrt((self.a3 - self.a2)**2 + (self.b3 - self.b2)**2) )
    #высота
    def height(self):
        self.h = float((abs((self.b2 - self.b3)*self.a1 + (self.a3 - self.a2)*self.b1 +(self.a2*self.b3 - self.a3*self.b2))/m.sqrt((self.b2 - self.b3)**2 + (self.a3 + self.a2)**2)))
tr1 = triangle(0, 0, 2, 4, 5, 6)


tr1.per()
tr1.height()
tr1.pl()
print('Периметр:', round(tr1.P, 3), 'Высота:', round(tr1.h, 3), 'Площадь:', round(tr1.S, 3))


#eazy_2

class trap:
    def __init__(self, a1, b1, a2, b2, a3, b3, a4, b4):
      self.a1 = a1
      self.b1 = b1
      self.a2 = a2
      self.b2 = b2
      self.a3 = a3
      self.b3 = b3
      self.a4 = a4
      self.b4 = b4


    #равнобедренный или нет
    def check(self):
        BC = m.sqrt((self.a3 - self.a2) ** 2 + (self.b3 - self.b2) ** 2)
        AD = m.sqrt((self.a4 - self.a1) ** 2 + (self.b4 - self.b1) ** 2)

        while BC != AD:
            break
    #длина сторон
    def length(self):
        AB = m.sqrt((self.a2 - self.a1) ** 2 + (self.b2 - self.b1) ** 2)
        BC = m.sqrt((self.a3 - self.a2) ** 2 + (self.b3 - self.b2) ** 2)
        AD = m.sqrt((self.a4 - self.a1) ** 2 + (self.b4 - self.b1) ** 2)
        CD = m.sqrt((self.a4 - self.a3) ** 2 + (self.b4 - self.b3) ** 2)
    #периметр
    def per(self):
        AB = m.sqrt((self.a2 - self.a1) ** 2 + (self.b2 - self.b1) ** 2)
        BC = m.sqrt((self.a3 - self.a2) ** 2 + (self.b3 - self.b2) ** 2)
        AD = m.sqrt((self.a4 - self.a1) ** 2 + (self.b4 - self.b1) ** 2)
        CD = m.sqrt((self.a4 - self.a3) ** 2 + (self.b4 - self.b3) ** 2)
        self.P = AB + BC + AD +CD
    #высота
    def hight(self):
        AB = m.sqrt((self.a2 - self.a1) ** 2 + (self.b2 - self.b1) ** 2)
        BC = m.sqrt((self.a3 - self.a2) ** 2 + (self.b3 - self.b2) ** 2)
        AD = m.sqrt((self.a4 - self.a1) ** 2 + (self.b4 - self.b1) ** 2)
        CD = m.sqrt((self.a4 - self.a3) ** 2 + (self.b4 - self.b3) ** 2)
        h = m.sqrt(AD ** 2 - ((AB - CD) ** 2) / 4)
    #площадь
    def pl(self):

        AB = m.sqrt((self.a2 - self.a1) ** 2 + (self.b2 - self.b1) ** 2)
        BC = m.sqrt((self.a3 - self.a2) ** 2 + (self.b3 - self.b2) ** 2)
        AD = m.sqrt((self.a4 - self.a1) ** 2 + (self.b4 - self.b1) ** 2)
        CD = m.sqrt((self.a4 - self.a3) ** 2 + (self.b4 - self.b3) ** 2)
        h = m.sqrt(AD ** 2 - ((AB - CD) ** 2) / 4)
        self.S = (h*(CD + AB))/2

trap1 = trap(0, 0, 7, 0, 5, 3, 2, 3)
trap1.per()
trap1.length()
trap1.pl()
print('Периметр:', round(trap1.P, 3), 'Площадь:', round(trap1.S, 3))


#normal_1

#запуталась и не доделала. в особенности в том, как выводить полные списки классов, учителей и тд. пришлите, пожалуйста, какую-нибудь подсказку и я постараюсь доделать в ближайшее время
class Smb:

    def __init__(self, name, surname, mid_name):
        self.name = name
        self.surname = surname
        self.mid_name = mid_name

    @property
    def get_name(self):
        name = '{}{}.{}.'.format(self.surname, self.name[0], self.mid_name[0])
        return name

    @property
    def get_full_name(self):
        name = '{}{}{}'.format(self.surname, self.name, self.mid_name)
        return name


class Student(Smb):
    def __init__(self, name, surname, mid_name, class_, mom, dad):
        Smb.__init__(self, name, surname, mid_name)
        self.class_ = class_
        self.mom = mom
        self.dad = dad

    @property
    def get_parents(self):
        return ['Мама:{}, Папа:{}'.format(self.mom, self.dad)]


class Teacher(Smb):
    def __init__(self, sub, name, surname, mid_name, classes):
        Smb.__init__(self, name, surname, mid_name)
        self.sub = sub
        self.classes = classes


class Classes:
    def __init__(self, number, letter):
        self.number = number
        self.letter = letter
        self.teachers = []
        self.students = []

    @property
    def get_name(self):
        return ['{}{}'.format(self.number, self.letter.upper)]

    def add_teacher(self, *args):
        for a in args:
            self.teachers.append(a)

    def add_student(self, *args):
        for a in args:
            self.students.append(a)


class Subject:
    def __init__(self, name):
        self.name = name

    #def get_all_classes(self):
        #return


class School:
    def __init__(self):
        self.classes = []

    def add_classes(self, *args):
        for a in args:
            self.classes.append(a)

    def get_classes(self):
        return [a.get_name for a in self.classes]


mom = Student("Иванова", "И", "В")
dad = Student("Иванов", "T", "C")

mom2 = Smb("Сидорова", "И", "В")
dad2 = Smb("Сидоров", "T", "C")

mom3 = Smb("Петрова", "И", "В")
dad3 = Smb("Петров", "T", "C")

student1 = Student(mom, dad, "Иванов", "Д", "Т")
student2 = Student(mom2, dad2, "Сидоров", "Д", "Т")
student3 = Student(mom3, dad3, "Петров", "Д", "Т")

math_subj = Subject("Математика")
phys_subj = Subject("Физика")
eng_subg = Subject("Английский язык")

math_teacher = Teacher(math_subj, "Васильева", "О", "П")
phys_teacher = Teacher(phys_subj, "Борисова", "О", "П")
eng_teacher = Teacher(eng_subg, "Дмитриева", "О", "П")

class1 = Classes(9, "A")
class2 = Classes(9, "Б")
class3 = Classes(9, "В")

school = School()

school.add_classes(class1, class2, class3)


print('Все классы:', school.get_classes())
print('Родители ученика:', student1.get_parents())




