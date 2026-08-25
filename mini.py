students = ["shahid", "ali", "ahmed", "sara", "fatima"]

for student in students:
    marks = int(input(student + ", enter your marks:"))
    if marks >= 50:
        print(student + " passed")
    else:
        print(student + " failed")