import matplotlib.pyplot as plt
import numpy as np


#with open('LastResult/AntPhase-1.txt') as f:
#    a = np.loadtxt(f, delimiter=';',  usecols=(0,1,2), unpack=True)
#
#plt.plot(a[0],a[1], 'o',label='ok')
#plt.plot(a[0],a[2], 'o',label='ok')
#plt.show()



#mesma coisa:
with open('LastResult/AntPhase-1.txt') as f:
    x,y = np.loadtxt(f, delimiter=';', usecols=(0,2),  unpack=True)

#plt.plot(x,y, 'ro',label='ok')
#plt.show()

#plt.plot([1,2,3,4],'ro')
#plt.ylabel('some numbers')
#plt.show()


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def StartsAtI(a,I):
    result = []
    for i in range(len(a)):
        result.append(a[(i+I)%len(a)])
    return result

def InnerProd(a,b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

def Norm(a):
    return np.sqrt(InnerProd(a,a))



def correlation(x,y):
#    print(x)
#    print(y)

    result = []
    part1 = 0.
    part2 = 0.
    part3 = 0.
    mx = mean(x)
    my = mean(y)
    print('Computing correlation...')
    xmx = [k-mx for k in x]
    
    for i in range(1*len(x)):
        
        ymy = [k-my for k in StartsAtI(y,i)]
        
        result+=[InnerProd(xmx,ymy) / (Norm(xmx)*Norm(ymy))]

    return result



a=[1,2,10,3]
b=[1,2,10,3]


a=range(20)
b=StartsAtI(a,0)

#print(a)
#print(StartsAtI(a,0))
#print(StartsAtI(a,1))
#print(StartsAtI(a,2))
#print(StartsAtI(a,3))
#print(StartsAtI(a,18))



cc = correlation(a,b)
#print(correlation(a,b));
#plt.plot(cc,'r')
#plt.show()


ants = 3
x=list(range(ants))
y=list(range(ants))
for i in range(ants):

    filename = 'LastResult/AntPhase-'+str(i+1)+'.txt'
    with open(filename) as f:
        x[i],y[i] = np.loadtxt(f, delimiter=';', usecols=(0,2),  unpack=True)
#        x[i] = np.loadtxt(f, delimiter=';', usecols=0,  unpack=True)
#        y[i] = np.loadtxt(f, delimiter=';', usecols=1,  unpack=True)

#print(y[0])
#print(x[0])
#filename = 'LastResult/AntPhase-1.txt'
#with open(filename) as f:
#    x1 = np.loadtxt(f, delimiter=';', usecols=(0,),  unpack=True)
#
#filename = 'LastResult/AntPhase-2.txt'
#with open(filename) as f:
#    x2 = np.loadtxt(f, delimiter=';', usecols=(0,),  unpack=True)

#cc=range(25)
#cc=[0 for c in cc]
#for i in range(5):
#    for j in range(5):

counter = 0
print(range(ants))
for i in range(ants):
    for j in range(i+1,ants):
        print('(i,j) = (',i,',',j,')')
        c1 = correlation(x[i],x[j])
        c2 = correlation(y[i],y[j])

        plt.figure(counter)
        plt.plot(c1,'b,')
        counter = counter + 1
        plt.figure(counter)
        plt.plot(c2,'r.')
        counter = counter + 1
        plt.figure(counter)
        plt.plot(x[i],'r.')
        counter = counter + 1
plt.show()

#        plt.plot(c1,c2,'r,')

#c2 = correlation(x[0],x[2])
#plt.plot(c2,'r')
#c3 = correlation(x[0],x[3])
#plt.plot(c3,'g')
#c4 = correlation(x[1],x[2])
#plt.plot(c4,'b')
#c5 = correlation(x[1],x[3])
#plt.plot(c5,'r')
#c6 = correlation(x[2],x[3])
#plt.plot(c6,'r')


#plt.show()




