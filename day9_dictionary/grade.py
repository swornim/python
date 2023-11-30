student_score = {
    "harry": 81,
    "ron":78,
    'hermione':99,
    "draco":74,
    "neville":62    
}

student_grade = {}

for key in student_score:
    if student_score[key] > 90:
        student_grade[key] = 'outstanding'
    elif student_score[key]>80:
        student_grade[key] = 'Exceeds Expectations'
    elif student_score[key] >70:
        student_grade[key] = "acceptable"
    else:
        student_grade[key] = 'fail'
print(student_grade)