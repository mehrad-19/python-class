#046
print('enter a number:')
x=int(input('a number:'))
while x<=5 :
   x=int(input('a new number:'))
   continue
x=str(x)
print('"The last number you entered was a '+x+' and stop program"')
print('\n')

#047
print('enter a number:')
x=int(input('first number:'))
list=[x]
print('do you enter another number?')
while input('user anwser:')=='y':
     y=int(input('new number:'))
     list.append(y)
     continue
print(list)
print('\n')


#048
print('invite party\n please enter name people for invite party')
list=[]
while input('do you add new somebody in party?')=='y' :
    y=input('name:')
    list.append(y)
    continue
print(list)
print(len(list))
print('\n')

#49
x=int(50)
y=int(input('guess number:'))
ret=0
if y!=x:
    print('to low or to high')
    ret+=ret
print('Well done you took '+int(ret)+' attemps')
print('\n')

#50
print('enter number')
x=int(input('number:'))
while x<10 or
x>20 :
   x=int(input('number:'))
   if x>20 :
       print('too high')
   elif x<10 :
       print('too low')
   continue
else :
    print('Thank you')

   

          


          
    
