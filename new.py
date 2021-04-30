def sum_bowls(r):
    if r==1:
        return 1
    else:
        return r + sum_bowls(r-1)

def sum_bowls_loop(r):
    sum = 0
    for i in range(1, r+1):
        sum = sum+i
    return sum

print(sum_bowls(4))
print(sum_bolws(5))

print(sum_bowls_loop(4))
print(sum_bowls_loop(5))