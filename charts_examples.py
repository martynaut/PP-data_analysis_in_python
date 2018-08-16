import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]
#x=np.array[x]
#y=np.array[y]
print(np.multiply(x,y))

a = np.arange(0,30,0.2).reshape(3,50)
#b=a.reshape(3,50)
print (a, a.size, a.dtype.name, '\n\n')
#print (b, b.size, b.dtype.name)



b = np.linspace(0,29.8,150).reshape(3,50)
print (b, b.size, b.dtype.name, '\n\n')

c=a+b
d=a-b
e=a*b

print (c, '\n\n', d, '\n\n', e, '\n\n')
print ('c=[2,6]-->',c[2,6],', d=[2,6]-->', d[2,6],', e=[2,6]-->', e[2,6])


X=[]
Y_1=[]
Y_2=[]
Y_3=[]
Y_4=[]

for x in np.arange(-10, 11, 0.1):
    y_1=2*pow(x,3)-2*pow(x,2)+7*x-2
    y_2=2*x
    y_3=2*pow(x,2)
    y_4=np.sin(x)
    X.append(x)
    Y_1.append(y_1)
    Y_2.append(y_2)
    Y_3.append(y_3)
    Y_4.append(y_4)
    
    
MIN = min(X)
MAX = max(X)    

plt.figure()
plt.plot(X,Y_1)
plt.show()

plt.figure()
plt.plot(X,Y_2,'green', linewidth=3.0)
plt.show()

plt.figure()
plt.plot(X,Y_3,'green', linewidth=3.0)
plt.show()

plt.figure()
plt.plot(X,Y_4,'green', linewidth=3.0)
plt.show()

plt.figure()
plt.plot(X,Y_1,X,Y_2)
plt.show()


plt.figure(figsize=(12,12))
plt.plot(X,Y_1,'green', linewidth=3.0, label=r'$f(x)=2x^3-2x^2+7x-2$')
plt.plot(X,Y_2,'red', linewidth=3.0, label='f(x)=2x')
plt.plot(X,Y_3,'blue', linewidth=3.0,label=r'$f(x)=2x^2$')
plt.plot(X,Y_4,'black', linewidth=3.0,label=r'$f(x)=sinx$')
plt.grid(True)
plt.legend(shadow=True, fontsize=20)
plt.text(-5,1000,'Multiple chart', style='italic', fontsize=20, bbox={'facecolor':'red', 'alpha':0.2, 'pad':20})
plt.show()



plt.figure(1,figsize=(10,10))
plt.subplot(221)
plt.plot(X,Y_1,'green', linewidth=3.0)
plt.subplot(222)
plt.plot(X,Y_2,'red', linewidth=3.0)
plt.subplot(223)
plt.plot(X,Y_3,'blue', linewidth=3.0)
plt.subplot(224)
plt.plot(X,Y_4,'black', linewidth=3.0)
plt.show()



plt.figure(1,figsize=(18,18))

plt.subplot(3,3,1)
plt.plot(X,Y_1,'green', linewidth=3.0)
plt.subplot(3,3,2)
plt.plot(X,Y_2,'red', linewidth=3.0)
plt.subplot(3,3,3)
plt.plot(X,Y_3,'blue', linewidth=3.0)

plt.subplot(3,3,4)
plt.plot(X,Y_4,'black', linewidth=3.0)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3,3,5)
plt.plot(X,Y_1,'cyan', linewidth=3.0)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3,3,6)
plt.plot(X,Y_2,'yellow', linewidth=3.0)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3,3,7)
plt.plot(X,Y_3,'magenta', linewidth=3.0)
plt.title('f(x)=2*x^2')

plt.subplot(3,3,8)
plt.plot(X,Y_4,'blue', linewidth=3.0)
plt.grid(True)
plt.xlim(-.5,.5)
plt.ylim(-.5,.5)
plt.title('f(x)=sinx')

plt.subplot(3,3,9)
plt.plot(X,Y_1,'green', linewidth=5.0)
plt.title('f(x)=2*x^3-2*x^2+7*x-2')

plt.show()