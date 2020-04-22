print('E4_mehrad soleimani')
print('mohasebe chandomin roze sal :')

def julian_date(y,m,d):
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
         print('teadade rozha az avale sal :')
         result1+=d
         return result1
    else:
        print('sale vared shode kabise nist')
        print(listdays)
        result2=0
        for i in listdays[:m-1]:
            result2=result2+i
        print('teadade rozha az avale sal :')
        result2+=d
        return result2
def func3(n,m) :
    if n%m==0 :
        print('2 adad barham bakhshpazir ast ')
def func4(num) :
    if num > 1:
        for i in range(2,num//2):
            if num%i!=0 :
                print(num)
                return num
        
        
        
            
