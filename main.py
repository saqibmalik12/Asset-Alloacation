from university import University
from department import Department
from asset import Asset

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
