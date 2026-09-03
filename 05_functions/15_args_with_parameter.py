"""
Program: LEGB Scope
Author: Aditya Keshri
Description: Understanding args_with_parameter

"""

def student_marks(name, *marks):
    print("Student:", name)
    print("Marks:", marks)
    print("Total:", sum(marks))
    print("Average:", sum(marks) / len(marks))


student_marks("Aditya", 80, 75, 90, 85)