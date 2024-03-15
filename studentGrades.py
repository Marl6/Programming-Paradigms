# we created a list of students with their corresponding grades for each of the 3 subjects
studentGrades = {
    "Marl": {"English": 95, "Science": 89, "Math": 90},
    "Carl": {"English": 100, "Science": 95, "Math": 98},
    "Karl": {"English": 75, "Science": 80, "Math": 90},
    "Larl": {"English": 85, "Science": 80, "Math": 87},
    "Darl": {"English": 90, "Science": 85, "Math": 86}
}

# this is the function where we will calculate the average grade of the student for the 3 subjects
# this function accepts a string which is the student's name as its argument
def calculate_Average(student):
    if student in studentGrades:
        grades = studentGrades[student]
        total_grades = sum(grades.values())
        average_grade = total_grades / len(grades)

        print(f"The Average grade of {student} is:", f"{average_grade:.1f}")
    else:
        print("Student not found!")

# this function determines the highest and lowest
def high_Low(student):
    if student in studentGrades:
        grades = studentGrades[student]

        highest_grade = max(grades.values())
        lowest_grade = min(grades.values())

        print(f"The highest grade of {student} is:", highest_grade)
        print(f"The lowest grade of {student} is:", lowest_grade)
    else:
        print("Student not found!")

# this function returns the list of students having grades in a specific subject more than your specified value
def number_students_above(subject, grade):
    students = []
    for student, grades in studentGrades.items():
        if subject in grades and grades[subject] >= grade:
            students.append(student)
    
    print(f"Here are the following students having grades in {subject} above {grade}:")
    for items in students:
        print(items)

# codes below simply showcases the sample usages of the 
calculate_Average("Marl")
high_Low("Darl")
number_students_above("Science", 84)
