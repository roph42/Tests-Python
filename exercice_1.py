def sum_of_digits(n):
    """"""
    sum = 0
    if(not isinstance(n, int) or n < 0):
        return f"{n} n'est pas un entier positif"
    
    for digit in str(n):
        sum += int(digit)
    return sum