import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def f_1(t):
    return t
def f_2(t):
    return t**2
def f_3(t):
    return t**3
def f_4(t):
    return t**5

fig, axes = plt.subplots(2,2, figsize=(15,10), sharex=True, sharey=False)

x=[]
y_1=[]
y_2=[]
y_3=[]
y_4=[]

for t in range(-5,6):
    x.append(t)
    y_1.append(f_1(t))
    y_2.append(f_2(t))
    y_3.append(f_3(t))
    y_4.append(f_4(t))
    t+=1

axes[0,0].plot(x, y_1, label='f(x)=x', color='red')
axes[0,0].set_title('funkcja f(x)=x')
axes[0,0].legend(loc=0)
axes[0,0].set_xlim(-5, 5)
axes[0,0].set_ylim(f_1(-5), f_1(5))
axes[0,0].set_xlabel('x')
axes[0,0].set_ylabel('f(x)')

axes[0,1].plot(x, y_2, label='f(x)=x**2', color='yellow')
axes[0,1].set_title('f(x)=x**2')
axes[0,1].legend(loc=0)
axes[0,1].set_xlabel('x')
axes[0,1].set_ylabel('f(x)')

axes[1,0].plot(x, y_3, label='f(x)=x**3', color='green')
axes[1,0].set_title('funkcja f(x)=x**3')
axes[1,0].legend(loc=0)
axes[1,0].set_ylim(f_3(-5), f_3(5))
axes[1,0].set_xlabel('x')
axes[1,0].set_ylabel('f(x)')

axes[1,1].plot(x, y_4, label='f(x)=x**5', color='pink')
axes[1,1].set_title('f(x)=x**5')
axes[1,1].legend(loc=0)
axes[1,1].set_ylim(f_4(-5), f_4(5))
axes[1,1].set_xlabel('x')
axes[1,1].set_ylabel('f(x)')


plt.show()

