print('E7.012_mehrad soleymani')
print('2 number vard kon:')
x=str(input('first number:'))
y=str(input('seconde number:'))
if len(x)>len(y) :
    print(int(y))
    print(int(x))
else :
    print(int(x))
    print(int(y))
print('\n')


#013
print('E7.013_mehrad soleymani')
print('enter a number under 20')
num=int(input('number:'))
if num>=20 :
    print(' "too high" ')
else:
    print(' "thank you" ')
print('\n')

#014
print('E7.014_mehrad soleymani')
print("enter one number between 10 and 20")
x=int(input('number:'))
if x>10 and x<20 :
    print('"thank you"')
else :
    print('"incorrect answer"')
print('\n')

#015
print('E7.015_mehrad soleymani')
print('enter your favorite color :')
C = str(input('your color:'))
if C=='red' or C=='RED' or C=='Red' :
    print(" I like red too .")
else :
    print(" I don't like "+C+",I prefer red. ")
print('\n')

#017
print('E7.017_mehrad soleymani')
print('enter your age')
a=int(input('age:'))
if a>=18 :
    print('"you can vote"')
elif a==17:
    print('"you can learn to drive"')
elif a==16:
    print('"you can buy a lottery tickt"')
else :
    print('"you can go trick or-treating"')
print('\n')

#018
print('E7.018_mehrad soleymani')
print('enter a number')
num=int(input('your number:'))
if num<10 :
    print(' Too low ')
elif num>10 and num<20 :
    print(' correct ')
elif num>=20 or num==10 :
    print(' Too high ')
print('\n')

#019
print('E7.019_mehrad soleymani')
print('enter 1,2 or 3')
num=int(input('number:'))
if num==1 :
    print('"Thank you"')
elif num==2 :
    print('"Well done"')
elif num==3 :
    print('"Correct"')
else :
    print('Error message')
print('\n')


