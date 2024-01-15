from department import Department

class University:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added to {self.name}.")
        else:
            print(f"Department '{department_name}' already exists in {self.name}.")

    def allocate_asset(self, department_name, asset):
        if department_name in self.departments:
            self.departments[department_name].allocate_asset(asset)
        else:
            print(f"Department '{department_name}' does not exist in {self.name}.")
