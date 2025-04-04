#UNWSP Programming PythonCos2005DEsp25
#Program_3_Employee Class
#04.4.25
#Abraham. N. Andersen

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_employee_info(self):
        print("Name:", self.name)
        print("ID Number:", self.id_number)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("-" * 20)

employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print("Employee Information:")
employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()