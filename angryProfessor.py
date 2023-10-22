#ProblemStatement:
#https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

def angryProfessor(k, a):

    on_time_students = sum(1 for arrival_time in a if arrival_time <= 0)
    
    if on_time_students < k:
        return "YES" 
    else:
        return "NO" 
    
#Logic:
#To determine whether the professor is angry or not, We count how many students arrive on time by looking at their arrival times. If the number of on-time students is less than the "k", the professor is angry, and we return "YES." Otherwise, if enough students are on time, we return "NO."
