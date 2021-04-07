'''
Please write a program that print the first N prime numbers.
N should be declared as a variable at the beginning of your code.
Code Writer: Jiyoung Kim
'''

N = int(input("Please enter the value for N:"))

def Prime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

i=2
p_list=[]

while True:
    if Prime(i):
        p_list.append(i)
        if(len(p_list) == N):
            print("First "+str(N)+" prime numbers:" + str(p_list))
    i+=1

