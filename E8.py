#069
counrty=('Canada','Spain','USA','France','Sewden')
print(counrtya)
counrty1=input('\n Enter one of the counrties shown above: ')
for name in counrty: 
    if counrty1.upper()==name.upper():
        print(name)
    
#070
num=int(input('Enter a number which display the country in that position: '))
for var in counrty:
    if var==num:
        print(var)

    
#072
sport=['fitness','football']
num=input('whats is your favorite sport? ')
sport.append(num)
sport.sort()
print(sport)

#073
    course=['history','math','geography','physique','chemistry','sports']
    print(course)
    like=input("which one you do not like?: ")
    if like.lower() in course:
        course.remove(like.lower())
    print(course)


#074
list_color=['blue','yellow','purple','red','white','pink','grey','brown','black','orange']
print(list_color)
num1=int(input('Enter starting number (between 0 and 4): '))
num2=int(input('Enter end number(between 5 and 9): '))
print(list_color[num1:num1])


#075
list_number=[562,458,457,123]
for var in list_number:
    print(str(var)+'\n')
num=int(input('Enter a three digit number: '))
var1=0
if var1 in list_number:
    while(var1<=3):
        if list1[var1]==num:
            print('the position is:' + str(var1))
else:
    print('this number is not on the list')

    
#076
list_invitation=[]
index=0
while index<3:
    name=input('Enter the names of guests: ')
    list_invitation.append(name)
    index+=1
str1=''
while(str1!='no'):
    names=input('Enter more names: ')
    str1=input('Is it finished?').lower()
    list_invitation.append(names)
for value in list_invitation:
    value+=1
print('you have invited ' + str(value) + ' people.')


#077
print(list_invitation)
name=input('Enter one of the names in the list: ')
for value in list1:
    if value==name:
        print('this is the position on the list: '+str(value))
name1=input('Do you want he/she to be in the list?: ')
if name1.lower()=='no':
    list_invitation.remove(name1)
print(list_invitation)


#078
list_show=['Comedy show','Dance show','series','movie']
print(list_show)
show=input('Enter another TV show: ')
num=int(input('where do you want to insert it?'))
list_show.insert(num,show)
print(list_show)



#079
nums=[]
str1=''
while(str1!='no'):
    num=int(input('Enter a number: '))
    nums.append(num)
    str1=input('Is it finished?').lower()
    list_invitation.append(names)
    print(nums)
last_num=input('Do you want the last number? ')
if last_num.lower()=='no':
    nums.pop()
print(nums)

