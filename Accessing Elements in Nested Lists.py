# 🎓 Student Grades Data
students = [
    ["Ali", ["Math", 88], ["Science", 91], ["English", 85]],
    ["Fatuma", ["Math", 92], ["Science", 87], ["English", 90]],
    ["James", ["Math", 76], ["Science", 83], ["English", 79]]
]

# Print all students
for student in students:
    print(student[0])  # student name

# Access Ali's Science score
ali_science = students[0][2][1]
print("Ali Science:", ali_science)

# Access Fatuma's English subject name
fatuma_english = students[1][3][0]
print("Fatuma Subject:", fatuma_english)

# Change James' Math score
students[2][1][1] = 80

# Print James' updated info
print("James Updated Record:", students[2])

# Loop through each student and show total score
for student in students:
    total = sum(sub[1] for sub in student[1:])
    print(f"{student[0]} Total:", total)
