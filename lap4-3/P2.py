from datetime import datetime
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age  = age
        self.running_number = 0
        self._id = ""
        self._birthdate = ""
        self.__bloodgroup = ""
        self.__is_marrired = False
        self.__generate_id() += 1
    
    def display_public_info(self):
        return f"Name: {self.name} \nAge: {self.age}"
    
    def __generate_id(self):
        self._id = datetime.now().year + f"{self.running_number}"