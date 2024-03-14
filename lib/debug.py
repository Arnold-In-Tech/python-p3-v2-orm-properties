#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee
import ipdb


def reset_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)


reset_database()
ipdb.set_trace()


# === Test cases

Department.get_all()
#==> [<Department 1: Payroll, Building A, 5th Floor>, <Department 2: Human Resources, Building C, East Wing>]

payroll = Department.find_by_name("Payroll")
payroll
#==> <Department 1: Payroll, Building A, 5th Floor>

payroll.location = 7
#==> *** ValueError: Location must be a non-empty string


# Let's try to set an invalid department id for an employee:

employee = Employee.find_by_id(1)
employee
#==> <Employee 1: Amir, Accountant, Department ID: 1>

employee.department_id = 1000
#==> *** ValueError: department_id must reference a department in the database
