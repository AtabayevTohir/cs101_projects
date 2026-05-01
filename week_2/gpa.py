name = input("Enter your name: ")
grade = float(input("Enter your GPA: "))
hours = float(input("Enter youtotal credit hours: "))
dean_requirement = grade >= 3.5 and hours >= 12
print(f"Student name is {name}")
print(f"Student's GPA is {grade:.1f}")
print(f"Student's total credit hours are {hours}")
if dean_requirement:
    print(f"Qualifies for Dean's list requirements: {dean_requirement}")
else:
    if grade < 3.5:
        needed_gpa = 3.5 - grade
        print(f"You need {needed_gpa:.2f} GPA points to pass")
    if hours < 12:
        needed_hours = 12 - hours
        print(f"You need {needed_hours} credit hours to pass")


