"""
Program: **kwargs with User Input
Description: Practice taking student details from the user
"""

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)


name = input("Enter your name: ")
course = input("Enter your course: ")
city = input("Enter your city: ")

student_info(
    name=name,
    course=course,
    city=city
)