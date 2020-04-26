print('E6_donbale fibonachi :')
def fib(n):
    if n==1 or n==2 :
        return 1
    return fib(n-1)+fib(n-2)
def fib2(n):
    list=[]
    for i in range(0,n):
        list.append(fib(n-i))
    return list
        
              
       
        
    
