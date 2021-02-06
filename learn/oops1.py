class Employee:
    no_of_emps = 0
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
        Employee.no_of_emps += 1

    def printdetails(self):
        print(f'Hi, my name is {self.name} and I earn ${self.salary} by being a {self.role}')


    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_string(cls, emp_str):
        name, salary, role = emp_str.split('-')
        return cls(name, salary, role)


class Developer(Employee):

    def __init__(self,name, salary, role, prog_lang):
        super().__init__(name,salary,role)
        self.prog_lang = prog_lang


pranjal = Developer('Pranjal',1000,'Student','Python')
monil = Employee('Monil',2000,'Student')
rudra = 'Rudra-1001-Writer-Python'
















# #
# pranjal.printdetails()
#
# def dec1(func1):
#     def nowexwc():
#         print('Executing')
#         func1()
#         print('Executed')
#     return nowexwc
# @dec1
# def who_is_pranjal():
#     print('Pranjal is a good boy')
#
# who_is_pranjal()
#
#
# new_emp_1 = Employee.from_string(rudra)
# Employee.change_leaves(34)
# print(monil.no_of_leaves)
# print(Employee.no_of_emps)
# print(new_emp_1.salary)