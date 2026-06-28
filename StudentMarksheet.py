# Make a student marksheet, witch will contain student name department name, enrollment no, semester, 5 sub marks, total marks, total obtained marks, percentage and grade.
name = input("Enter Student Name: ")
department = input("Enter Department Name: ")
enrollment = input("Enter Enrollment No: ")
semester = input("Enter Semester: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total_marks = 500
obtained_marks = m1 + m2 + m3 + m4 + m5
percentage = (obtained_marks / total_marks) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nSTUDENT MARKSHEET")
print("Student Name      :", name)
print("Department        :", department)
print("Enrollment No     :", enrollment)
print("Semester          :", semester)
print("\n")
print("Subject 1 Marks   :", m1)
print("Subject 2 Marks   :", m2)
print("Subject 3 Marks   :", m3)
print("Subject 4 Marks   :", m4)
print("Subject 5 Marks   :", m5)
print("\n")
print("Total Marks       :", total_marks)
print("Obtained Marks    :", obtained_marks)
print("Percentage        :", round(percentage, 2), "%")
print("Grade             :", grade)