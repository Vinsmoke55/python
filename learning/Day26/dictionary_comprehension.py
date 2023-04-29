import random

names=["alex","ram","hari","sita","gita"]

student_scores={student:random.randint(1,100) for student in names}

print(student_scores)

passed_score={student:score for (student, score) in student_scores.items() if score>=60}

print(passed_score)