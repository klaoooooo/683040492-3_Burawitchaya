from datetime import datetime
class Person:
    running_number = 0

    def __init__(self, name, age, id, birthdate, bloodgroup, is_marrired):
        self.name = name 
        self.age  = age
        self._id = Person.__generate_id()
        self._birthdate = birthdate
        self.__bloodgroup = bloodgroup
        self.__is_marrired = is_marrired
        
    
    def display_info(self):
        return f"Name: {self.name} \nAge: {self.age}"
    
    def display_all_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nID: {self._id} \nBirthdate: {self._birthdate} \nBloodgroup: {self.__bloodgroup} \nMarried: {self.__is_marrired}"
    
    def __generate_id(self):
        running_number += 1
        self._id = datetime.now().year + f"{Person.running_number:03d}"

class Staff(Person):
    def __init__(self, name, age, id, birthdate, bloodgroup, is_marrired,  department, start_year, tenure_year, salary):
        super().__init__(name, age, id, birthdate, bloodgroup, is_marrired)
        self.department = department
        self.start_year = start_year
        self.tenure_year = tenure_year
        self.__salary = salary
        

    def calculate_tenure_years(self):
        current_year = datetime.now().year
        self.tenure_year = current_year - self.start_year
        return self.tenure_year
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary

    def display_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nDepartment: {self.department} \nStart year: {self.start_year} \nTenure year: {self.tenure_year} \nSalary: {self.__salary}" 
    
    def display_all_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nID: {self._id} \nBirthdate: {self._birthdate} \nBloodgroup: {self.__bloodgroup} \nMarried: {self.__is_marrired} \nDepartment: {self.department} \nStart year: {self.start_year} \nTenure year: {self.tenure_year} \nSalary: {self.__salary}"

class Student(Person):
    def __init__(self, name, age, id, birthdate, bloodgroup, is_marrired, start_year, major, level, grade_list = [], gpa = 0.0, graduation_date = 0):
        super().__init__(name, age, id, birthdate, bloodgroup, is_marrired)
        self.start_year = start_year
        self.major = major  
        self.level = level
        self.grade_list = grade_list
        self.gpa = gpa
        self.__graduation_date = graduation_date


    def calculate_gpa(self):
        total = sum(self.grade_list)
        self.gpa = total / len(self.grade_list)
        return self.gpa
    
    def __calculate_graduation_date(self):
        if self.level.lower() == "undergraduate":
            self.__graduation_date = self.start_year + 4
        elif self.level.lower() == "graduate":
            self.__graduation_date = self.start_year + 2
        return self.__graduation_date

    def display_info(self):
        return f"Name: {self.name} \nAge: {self.age}"
    
    def display_all_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nID: {self._id} \nBirthdate: {self._birthdate} \nBloodgroup: {self.__bloodgroup} \nMarried: {self.__is_marrired} \nStart year: {self.start_year} \nMajor: {self.major} \nLevel: {self.level} \nGPA: {self.gpa} \nGraduation date: {self.__graduation_date}"

class Professor(Staff):
    dict = {
        0 : "lecturer",
        1 : "assistant professor",
        2 : "associate professor", 
        3 : "full professor",
        4 : "highest full professor"
    }

    def __init__(self, name, age, id, birthdate, bloodgroup, is_marrired, department, start_year, tenure_year, salary, professorship, admin_position):
        super().__init__(name, age, id, birthdate, bloodgroup, is_marrired, department, start_year, tenure_year, salary)
        self.professorship = professorship
        self.admin_position = admin_position
  

    def display_info(self):
        return f"Name: {self.name} \nAge: {self.age}" 
    
    def display_all_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nID: {self._id} \nBirthdate: {self._birthdate} \nBloodgroup: {self.__bloodgroup} \nMarried: {self.__is_marrired} \nDepartment: {self.department} \nStart year: {self.start_year} \nTenure year: {self.tenure_year} \nSalary: {self.get_salary()} \nTitle: {self.title} \nResearch area: {self.research_area}"