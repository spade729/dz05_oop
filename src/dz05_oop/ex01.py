"""1.Создайте класс Student, который должен содержать.

Конструктор, принимающий имя и возраст студента;
Атрибуты name (публичный) и age (защищенный);
Метод get_info(), который возвращает строку: "Студент {name}, возраст {age}".

# Образец использования:
student1 = Student("Анна", 20)
print(student1.get_info())  # Должно вывести: "Студент Анна, возраст 20"    


2.Расширьте класс Student из первой задачи, создав класс GraduateStudent (аспирант), который:

Наследуется от Student;
Добавляет защищенный атрибут _research_topic (тема исследования);
Добавляет приватный атрибут __publications (количество публикаций);
Добавляет метод add_publication(), который увеличивает количество публикаций на 1;
Переопределяет метод get_info(), чтобы он включал тему исследования.


# Образец использования:
grad_student = GraduateStudent("Петр", 25, "Искусственный интеллект")
print(grad_student.get_info())  # "Студент Петр, возраст 25, тема: Искусственный интеллект"

grad_student.add_publication()
grad_student.add_publication()
# Проверка количества публикаций должна быть через специальный метод

3. Создайте систему управления студентами:

+ Реализуйте класс <b>StudentManager</b> для работы с коллекцией студентов;
+ Добавьте магические методы в классы:

    + <b>\_\_str\_\_</b> и <b>\_\_repr\_\_</b> для красивого вывода;
    + <b>\_\_len\_\_</b> для StudentManager (возвращает количество студентов);
    + <b>\_\_getitem\_\_</b> для доступа к студентам по индексу;

+ Реализуйте полиморфизм - метод, который работает с любыми типами студентов.

# Образец использования:
manager = StudentManager()

student1 = Student("Анна", 20)
student2 = GraduateStudent("Петр", 25, "AI")

manager.add_student(student1)
manager.add_student(student2)

print(len(manager))  # Должно вывести: 2
print(manager[0])    # Должен вывести первого студента

# Полиморфный метод, который выводит информацию о всех студентах
manager.print_all_info()
"""

class Student:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def get_info(self):
        return f'Студент {self.name}, возраст {self.age}'

print('1)')
student1 = Student("Анна", 20)
print(student1.get_info())

 
class GraduateStudent(Student):  
    def __init__(self, name:str, age:int, research_topic:str):
        super().__init__(name, age)  
        self._research_topic = research_topic  
        self.__publications = 0
    
    def get_info(self):
        return f'Студент {self.name}, возраст {self.age}, тема: {self._research_topic}'
    
    def add_publication(self):
        self.__publications += 1

    @property
    def publications(self):
        return self.__publications
    


print('2)')
grad_student = GraduateStudent("Петр", 25, "Искусственный интеллект")
print(grad_student.get_info())   


grad_student.add_publication()
grad_student.add_publication()
print(grad_student.publications) 

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, obj:Student):
        self.students.append(obj)

    def print_all_info(self):
        for obj in self.students:
            print(obj.get_info())

    def __str__(self):
        return f'StudentManager, {len(self.students)} студентов'

    def __len__(self):
        return len(self.students)

    def __getitem__(self, i):
        return self.students[i]
    


print('3)')
# Образец использования:
manager = StudentManager()

student11 = Student("Анна", 20)
student2 = GraduateStudent("Петр", 25, "AI")

manager.add_student(student11)
manager.add_student(student2)

print(str(manager)) 
print(len(manager))  # Должно вывести: 2
print(manager[0])    # Должен вывести первого студента
print(manager[0].get_info())

# Полиморфный метод, который выводит информацию о всех студентах
manager.print_all_info()

