import sklearn
import math
import copy
t=int(input())
for h in range(1,t+1):
    n,l=[int(x) for x in input().split(" ")]        
    lis=[int(f) for f in input().split(" ")]
    p=[]
    res=[]
    #code to create a list containing prime numbers between 1 and n inclusive
    for num in range(1,n + 1):
        if num > 1:
            for i in range(2,num):            
                if (num % i) == 0:
                    break
            else:
                if(num not in p): 
                    p.append(num)
    #taking each element in given list and check whether any element in list is divisble by prime numbers in p
    #if number is found then break
    for i in lis:
        for z in p:
            #to check whether the element is first element or not i use len(res)==0
            if(len(res)==0):
                if(i%z==0): 
                    woo=z
                    foo=i/woo
                    res.append([woo,foo])
                    break
            else:
                woo=res[-1][1]
                foo=i/woo
                res.append([woo,foo])
                break
    arr=[]
    arr.append(res[0][0])
    for x in res:
        arr.append(x[1])
    unsort=copy.copy(arr)
    arr.sort()
    x=set(arr)
    arr=list(x)
    arr.sort()
    
    idx=[]
    for x in unsort:
        idx.append(arr.index(x))
    s=''
    for c in idx:
        s=s+chr(65+c)
    print('Case #{}: {}'.format(h,s))
    
