def repeatedString(s, n):
    a_og = s.count('a')
    f_rep = n // len(s)
    r = n % len(s)
    a_par = s[:r].count('a')
    a_tot = (a_og * f_rep) + a_par

    return a_tot