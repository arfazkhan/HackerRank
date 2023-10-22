#ProblemStatement:
# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = (grade // 5 + 1) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades

#Logic:
#In this code, I'm simplifying grades for students. For each grade, I check if it's less than 38; if it is, I keep it unchanged. If it's 38 or higher, I find the next multiple of 5 and see if the difference is less than 3. If it is, I round up to that multiple of 5; otherwise, I keep the grade as it is. 