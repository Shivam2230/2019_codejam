t= int(input())
for h in range(1,t+1):
    l=int(input())
    s=str(input())
    #converting string to list because str doesn't support type assignment
    s1=list(s)
    #traverse the whole string and change 'S' with 'E' and vice versa
    for i in range(len(s1)):
        if(s1[i]=='S'):
            s1[i]='E'
        else:
            s1[i]='S'
    #converting list back to string
    s=''.join(c for c in s1)
    print('Case #{}: {}'.format(h,s))
