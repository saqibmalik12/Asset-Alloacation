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

class Department:
    def __init__(self, name):
        self.name = name
        self.allocated_assets = []

    def allocate_asset(self, asset):
        self.allocated_assets.append(asset)
        print(f"{asset} allocated to {self.name}.")

class Asset:
    def __init__(self, asset_type, asset_name):
        self.asset_type = asset_type
        self.asset_name = asset_name

    def __str__(self):
        return f"{self.asset_type}: {self.asset_name}"

# Creating University
uni = University("Islamia University")

# Adding Departments
uni.add_department("Software Engineering")
uni.add_department("Computer Science")

# Allocating Assets
asset1 = Asset("Classroom", "Room 2.12")
asset2 = Asset("Laboratory", "Lab A")
asset3 = Asset("Equipment", "Computer Chips")

uni.allocate_asset("Software Engineering", asset1)
uni.allocate_asset("Computer Science", asset2)
uni.allocate_asset("Computer Science", asset3)
