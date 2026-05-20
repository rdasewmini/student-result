tot=0
av=0
c_f_sub=0
for i in range(1,7,1):
  marks=float(input('enter marks of the subject {i}:'))
  tot +=marks
  print(tot)

if marks<50:
    c_f_sub +=1

av=tot/6

print=('total marks:',tot)
print('avarage:',av)
print('f_sub:,c_f_sub')

if av>=60 and c_f_sub ==0:
    print('exellent performance')
elif av>=50:
    print('pass')
else:
    print('fail')
