class PasswordManager:
    def __init__(self):
        self.__password = "1234567"
        self.__failed_attempts = 0

    def __increment_attempts(self):
        self.__failed_attempts += 1

    def __is_locked_out(self):
        if self.__failed_attempts > 3:
          return True
        else:
          return False

    def check_password(self, inpass):
      self.__increment_attempts()
      if self.__is_locked_out():
        return "Too many failed attempts"

      if inpass == self.__password:
        self.__failed_attempts = 0 
        return "Correact Password"
      else:
        return "Wrong Password"
    
    def print_pass(self):
      return self.__passwoed


# Usage
pm = PasswordManager()

print(pm.check_password("124567"))
print(pm.check_password("1234567"))
print(pm.check_password("1247"))
print(pm.check_password("67"))
print(pm.check_password("1"))

# do something here to verify the program
