p = True
q = False


if p and q:
    print('p and q = TRUE')
else:
    print('p and q = NOT TRUE')

if p or q:
    print('p or q = TRUE')
else:
    print('p or q = NOT TRUE')


# xor
if p ^ q:
    print('p xor q = TRUE')
else:
    print('p xor q = NOT TRUE')


for i in range(10):
    if i == 3:
        continue # when we reach i=3, we will not print out 3, will just continue  # pass(dont do anything?) is dif from continue
    print(i)
    if i==7:
        break


def sum(a, b):
    return a + b

print(sum(56, 645))


'''
multiline comment 작성하는 법 => 3 upperstrophe 사용
'''