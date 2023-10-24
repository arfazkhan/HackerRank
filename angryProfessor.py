#ProblemStatement:
#https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

def angryProfessor(k, a):

    on_time_students = sum(1 for arrival_time in a if arrival_time <= 0)
    
    if on_time_students < k:
        return "YES" 
    else:
        return "NO" 
    