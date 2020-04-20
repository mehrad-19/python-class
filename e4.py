print('E4_mehrad soleimani')
print('mohasebe chandomin roze sal :')
y = int(input('sal morede nazareto vared kon :'))
m= int(input('mahe morede nazareto vared kon :'))
d = int(input('roze morede nazareto vared kon :'))
print(d,m,y)

listdays=[31,28,31,30,31,30,31,31,30,31,30,31]
if y%400==0 :
    print('sale vared shode kabise ast')
elif y%4==0 :   
    if y%100!=0 :
        print('sale vared shode kabise ast')
        listdays.remove(28)
        listdays.insert(1,29)
    print(listdays)
    result1=0
    for i in listdays[:m-1]:
        result1=result1+i
    print(result1)
    print('teadade rozha az avale sal :')
    print(result1+d)
else:
    print('sale vared shode kabise nist')
    print(listdays)
    result2=0
    for i in listdays[:m-1]:
        result2=result2+i
    print(result2)
    print('teadade rozha az avale sal :')
    print(result2+d)
        
            
