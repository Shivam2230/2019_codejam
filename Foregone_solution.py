import random
#taking number of test cases

t=int(input())
for h in range(1,t+1):
    x=int(input())
    #function to check whether the number contains 4 or not
    def checkforfour(n):
        n=list(str(n))
        if ('4' in n):
            return False
        return True
    #iterating until we get a solution
    while True:
        z=random.randint(0,x+1)
        #applying checkfour function for a random number z(between 0 and x inclusive) and x-z also
        if(checkforfour(z) and checkforfour(x-z)):
            print('Case #{}: {} {}'.format(h,z,x-z))
            break
