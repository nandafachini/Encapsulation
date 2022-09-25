# Change the Employee class of the program below:
# Transform your attributes into private attributes.
# Create get and set methods for all attributes.
# Make the necessary changes for the main program to 
# work correctly, after the changes made to the class. 


class Employee:
    # private attributes
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary


    # get methods
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary


    # set methods
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_salary(self, salary):
        self.__salary = salary


employee1 = Employee("Pedro", "111222333-22", 1500.0)
employee1.set_salary(2000.0)
print("Name:", employee1.get_name())
print("ID:", employee1.get_id())
print("Salary:", employee1.get_salary())
