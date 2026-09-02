"""
Program: **kwargs Practice
Description: Practice with variable-length keyword arguments
"""

def student_info(**details):
    print(details)


student_info(name="Aditya", course="Python", age=21)