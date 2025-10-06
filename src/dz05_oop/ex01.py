"""Zadacha.

OOP
"""

class Student:
    """Class student."""
    def __init__(self, name:str, age:int):
        """конструктор."""
        self.name = name
        self._age = age

    def get_info(self):
        """Information."""
        return f'Студент {self.name}, возраст {self._age}'
    
    def __print(self, text):
        print(text)

    def get_info_print(self):
        """PrintInfo."""
        self.__print(self.get_info())

print('1)')
student1 = Student('Анна', 20)
print(student1.get_info())

 
class GraduateStudent(Student):
    """GraduateStudent."""
    def __init__(self, name:str, age:int, research_topic:str):
        """Constr."""
        super().__init__(name, age)  
        self._research_topic = research_topic  
        self.__publications = 0
    
    def get_info(self):
        """New info."""
        return f'Студент {self.name}, возраст {self._age}, тема: {self._research_topic}'
    
    def add_publication(self):
        """Add p."""
        self.__publications += 1

    @property
    def publications(self):
        """Get method."""
        return self.__publications
    


print('2)')
grad_student = GraduateStudent('Петр', 25, 'Искусственный интеллект')
print(grad_student.get_info())   


grad_student.add_publication()
grad_student.add_publication()
print(grad_student.publications) 

class StudentManager:
    """StudentMan."""
    def __init__(self):
        """Init."""
        self.students = []

    def add_student(self, obj:Student):
        """Add."""
        self.students.append(obj)

    def print_all_info(self):
        """Print all."""
        for obj in self.students:
            print(obj.get_info())

    def __str__(self):
        """Str."""
        return f'StudentManager, {len(self.students)} студентов'

    def __len__(self):
        """Len."""
        return len(self.students)

    def __getitem__(self, i):
        """Getitem."""
        return self.students[i]
    


print('3)')
# Образец использования:
manager = StudentManager()

student11 = Student('Анна', 20)
student2 = GraduateStudent('Петр', 25, 'AI')

print('---------------')
student2.get_info_print()
print('---------------')

manager.add_student(student11)
manager.add_student(student2)

print(str(manager)) 
print(len(manager))  # Должно вывести: 2
print(manager[0])    # Должен вывести первого студента
print(manager[0].get_info())

# Полиморфный метод, который выводит информацию о всех студентах
manager.print_all_info()

