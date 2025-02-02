students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    
#student in the following code is used as the loop variable
    
scores = sorted(set(student[1] for student in students))

second_lowest_grade = scores[1]

second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
second_lowest_students.sort()

for name in second_lowest_students:
    print(name)

