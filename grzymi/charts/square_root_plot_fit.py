import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import scipy.optimize as opt

print('Welcome. Please input the main parameters for equation Ax2+Bx+C=0')
a= float(input('Give A: '))
b= float(input('Give B: '))
c= float(input('Give C: '))

print('Your equation looks like:', a, 'x2+', b, 'x+', c, '=0')
d=pow(b,2)-4*a*c
print('Delta is equal:', d)
         
if d<0:
         print('No real solution')
elif d==0:
         x=(-b)/(2*a)
         print('There is only one solution, x=', x)
else:
         x1=(-b-sqrt(d))/(2*a)
         x2=(-b+sqrt(d))/(2*a)
         print('There are two solutions: x1=', round(x1,2), 'x2=', round(x2,2))

print('Equation of first derivative is equal f(x)=', 2*a, 'x+', b)

x_eks = -b/(2*a)
y_eks = a*x_eks**2+b*x_eks+c

if a<0:
    print("This function has maximum in point x=", round(x_eks, 2), 'y=', round(y_eks, 2))
else:
    print("This function has minimum in point x=", round(x_eks, 2), 'y=', round(y_eks, 2))

X_1=[]
Y_1=[]
#file_name = input('Get the file name: ')
for x in range (-5,6,1):
         y=a*(x**2)+b*x+c
         X_1.append(x)
         Y_1.append(y)


'''		 
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(X_1,Y_1, 'rs')
#axes.plot(x_eks,y_eks, 'rs')
plt.grid(True)
plt.show()
#plt.savefig(file_name+'.png')
'''

def func(x,a,b,c):
	return a*(x**2)+b*x+c


fit_curve = np.polyfit(X_1, Y_1, 2)
print (fit_curve)
print ('f(x)=',fit_curve[0], 'x^2+', fit_curve[1], 'x+', fit_curve[2])
X_3 = np.arange(-5,5.1,0.1)
Y_3 = func(X_3, fit_curve[0], fit_curve[1], fit_curve[2])

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(X_1,Y_1, 'rs')
axes.plot(X_3,Y_3)
plt.grid(True)
plt.show()
#plt.savefig(file_name+'.png')

'''
plt.figure()
plt.plot(X,Y,x_eks,y_eks,'rs')
plt.show()
'''

X_2=[]
Y_2=[]
#file_name = input('Get the file name: ')
for x in np.arange (-5,5.1,0.1):
         y=a*(x**2)+b*x+c
         X_2.append(x)
         Y_2.append(y)


etykieta = r'$f(x)=$'+str(a)+r'$x^2+$'+str(b)+r'$x+$'+str(c)

plt.figure()
plt.plot(x_eks,y_eks, 'rs') #
plt.plot(X_2,Y_2,'green',label=etykieta,linewidth=3)
plt.xlabel(r'$X$')
plt.ylabel(r'$Y$')
plt.xlim(min(X_2)-1, max(X_2)+1)
plt.title('Wykres funkcji kwadratowej', fontsize=14,style='italic')
plt.grid(True)
plt.legend(shadow=True, fontsize=12)
plt.show()
		 

		 

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(X_1,Y_1)
plt.plot(x_eks,y_eks, 'rs')
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(x_eks,y_eks, 'cH')
plt.plot(X_2,Y_2,'yellow', linewidth=2, label=etykieta)
plt.xlabel(r'$X$')
plt.ylabel(r'$Y$')
plt.xlim(min(X_2)-1, max(X_2)+1)
plt.title('Wykres funkcji kwadratowej', fontsize=14,style='italic')
plt.grid(True)
plt.legend(shadow=True, fontsize=12)

plt.show()