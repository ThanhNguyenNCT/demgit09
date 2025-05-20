class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.emp_id}: {self.name} ({self.position})"

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, emp_id, name, position):
        employee = Employee(emp_id, name, position)
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]

    def list_employees(self):
        for emp in self.employees:
            print(emp)

if __name__ == "__main__":
    company = Company("DemoGit Inc.")
    company.add_employee(1, "Alice", "Manager")
    company.add_employee(2, "Bob", "Developer")
    company.add_employee(3, "Charlie", "Designer")

    print("All employees:")
    company.list_employees()

    print("\nRemoving employee with ID 2...\n")
    company.remove_employee(2)

    print("Employees after removal:")
    company.list_employees()