import random
text=open("text.txt","r")
initial=text.read()
lexis=initial.split()
x=len(lexis)
while(len(lexis)>2):
    x=random.randint(0,len(lexis)-3)
    #print x
    print lexis[x-1],
    print lexis[x],
    print lexis[x+1],
    del lexis[x-1]
    del lexis[x]
    del lexis[x+1]
    #print len(lexis)
#print lexis