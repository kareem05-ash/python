from datetime import datetime as dt

class Employee:     # Base Class
    total_employees = 0
    company_name = 'Si-Vision'      # Default Company Name

    def __init__(self, name, salary, dep):
        self.name = name.title()
        self.emp_id = 'EMP' + str(Employee.total_employees + 1).zfill(3)
        self.salary = salary
        self.dep = dep
        self.hire_date = dt.now().date()
        Employee.total_employees += 1       # Add new employee
        print(f"A new employee {name} has been added at hire date: {self.hire_date}")

    def calculate_pay(self):
        return self.salary
    
    def get_emp_info(self):     # returns a dictionary of employee information
        return {
            'name': self.name,
            'emp_id':self.emp_id,
            'salary':self.salary,
            'dep':self.dep,
            'hire_date':self.hire_date
        }
    
    def __str__(self):
        return f"An employee in {Employee.company_name} company -> Name: {self.name}, ID: {self.emp_id}, Departemnt: {self.dep}"
    
    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return (self.name == other.name and
                # self.emp_id == other.emp_id and
                self.dep == other.dep and
                self.salary == other.salary and
                self.hire_date == other.hire_date)

    @classmethod
    def get_emp_count(cls):
        return cls.total_employees
    
    @staticmethod
    def validate_salary(salary):    # min salary: 8_000 & max salary: 50_000
        return salary >= 8_000 and salary <= 50_000
    

class Manager(Employee):
    def __init__(self, name, salary, dep, team_size, bonus):
        super().__init__(name, salary, dep)
        self.team_size = team_size
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus


class Developer(Employee):
    def __init__(self, name, salary, dep, programming_lang, level):
        super().__init__(name, salary, dep)
        self.programming_lang = programming_lang
        self.level = level.strip().lower()
        self.projects = []

    def calculate_pay(self):
        if self.level == 'junior':
            return self.salary * 1.1    # Bonus: 10%
        elif self.level == 'senior':
            return self.salary * 1.15   # Bonus: 15%
        elif self.level == 'team leader':
            return self.salary * 1.25   # Bonus: 25%
        else:
            return self.salary          # Return Salary if not defined level
        
    def add_project(self, project_name):
        self.projects.append(project_name)
