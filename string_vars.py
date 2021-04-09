s= 'abcdefaa'
print(len(s))
print(s.count('a'))

print(s[1:])
print(s[1:3])
print(s[:2])
print(s[-3:])

s2 = 'abc\n\rdef'
print(s2)

print(ord('a'))

#\r???
s3 = 'gsgaloozzca'
print(s3)

s4 = 'abc\tdef\t\t\tegwg'
print(s4)

# How to escape the characters?
s5 = 'abc\td\ef\t\t\te\gwg'
print(s5)
s6 = "agsag'agsg"
s6 = 'agsag\'agsg'
print(s6)

s7 = '          asgsgsag  asggs   '
print(s7)
print(s7.strip()) #this get rids of the spaces

s5_tab = s5.split('\t')
print(s5_tab)