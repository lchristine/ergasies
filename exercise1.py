def sumIntervals(x):
    sum=0
    x.sort()
    print x
    for i in range(0,len(x)-1):
        if(x[i][1]>x[i+1][0]):
            if(x[i][1]<x[i+1][1]):
                x[i+1][0]=x[i][1]
            else:
                x[i+1][0]=0
                x[i+1][1]=0
    for i in range(0,len(x)):
        sum+=x[i][1]-x[i][0]
    print sum
 
 
x=[[2,8],[12,23],[3,9],[504,532],[504,503],[401,408]]
sumIntervals(x)