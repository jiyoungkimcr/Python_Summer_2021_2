l1 = [[3, 6, 9], [6, 8, 5], [9, 5, 2]]
# sum rows
# sum cols
# sum of all elements

#rows
sum_r=([sum(i) for i in l1])
print (sum_r)

#columns
sum_c = sum(i[column] for i in l1)
print (sum_c)
