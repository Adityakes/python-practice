"""
Program: Student Profile using **kwargs
Description: Practice storing and displaying profile details
"""

def show_profile(**profile):
    for key, value in profile.items():
        print(key, ":", value)


show_profile(
    name="Aditya",
    course="B.Tech CSE",
    skill="Python",
    goal="Software Development"
)