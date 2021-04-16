# Reading .txt files
# taking any txt files(simple one) and write a code which print number of words in every ???
# (과제, special symbols 같은 거는 제외한다면 훨씬 쉬울 것)

my_file = 'out'
i = 0
with open(my_file, 'r') as f:
    line = f.readlines()
    for line in lines:
        i += 1
        print("%i: %s" % (i, line))
