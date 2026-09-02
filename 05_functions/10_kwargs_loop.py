"""
Program: **kwargs Loop Practice
Description: Access keyword arguments using a loop
"""

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)


student_info(
    name="Aditya",
    course="Python",
    age=21
)