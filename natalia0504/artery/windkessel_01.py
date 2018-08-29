from PIL import Image
from pprint import pprint
import matplotlib.pylab as plt
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import quad
import sympy as sp

R = 2400000  # mmHg/cm**3/s
r = 0.001  # mmHg/cm**3/s
C = 1.0666  # cm**3/mmHG
d = 0.5  # cm
A = 0.25 * np.pi * d ** 2  # cm**2
G = (1 + r / R) * 0.01 * A
H = C * r * 0.01 * A

def model(y,t, W):
    dydt = (1 / R * y + W) / C
    return dydt

def f(t1):
    return np.exp(-t1 / C / R) * np.exp(t1 / C / R) * (
                ((R + r) / (C * R) * A * 0.01 * np.polyval(u, t1)) + A * 0.01 * r * np.polyval(du, t1))

img = Image.open("velocity.bmp")
try:
    data = np.asarray(img, dtype='bool')
except SystemError:
    data = np.asarray(img.getdata(), dtype='bool')

cor_y = []
cor_x = []

for i in range(0, 172):
    for j in range(0, 99):
        if data[i][j] == False:
            cor_x.append(j * 0.01)
            cor_y.append(i * 0.01)

x = np.array(cor_x)
reverse_y = np.array(cor_y)
y = reverse_y[::-1]

n = 200
t = np.linspace(0, 1, n)
u = np.poly1d(np.polyfit(x, y, 8))

# plt.plot(x, y, 'o', t, u(t), ':r')

pprint(u)
du = np.polynomial.polynomial.polyder(u)
pprint(du)

W1 = G * u
W2 = H * du
W = np.polynomial.polynomial.polyadd(W1, W2)
#pprint(W1)
#pprint(W2)

# initial condition
y0 = 80  # mmHg

# solve ODE
for i in range(len(t)):
    y = odeint(model, y0, t, args=(np.polyval(W, t[i]),))

# for i in range (1,len(t)-1):
# P_i=(1/(1+C*R/(t[i+1]-t[i])))*(P[i-1]*C*R/(t[i+1]-t[i])+(A*0.01*np.polyval(u,t[i])*(1+r/R+C*r/(t[i+1]-t[i]))-np.polyval(u,t[i-1]*C*r/(t[i+1]-t[i]))))
# P.append(P_i)

P = []
exp = np.exp
for i in range(len(t)):
    P.append(-11.7224235470914 * t[i] ** 11 + 65.0134604841287 * t[i] ** 10 - 155.740398958344 * t[
        i] ** 9 + 210.903281541584 * t[i] ** 8 - 178.195632365643 * t[i] ** 7 + 98.5524697141024 * t[
                 i] ** 6 - 36.8366315805136 * t[i] ** 5 + 9.57273136380131 * t[i] ** 4 - 1.73545056717 * t[
                 i] ** 3 + 0.189783007969676 * t[i] ** 2 + 0.00573084742324315 * t[i])

#plt.plot(t,P,'g--')
#plt.plot(t,y,'b--')
#plt.xlabel('time')
#plt.ylabel('y')
#plt.show()

t1 = sp.Symbol('t[i]')

B = sp.exp(t1 / C / R) * (((R + r) / (C * R) * A * 0.01 * np.polyval(u, t1)) + A * 0.01 * r * np.polyval(du, t1))
P1 = sp.exp(-t1 / C / R) * B
sp.integrate(P1)



P1 = []

for i in range(len(t)-1):
    P1.append(quad(f, t[i], t[i+1])


pprint(P1)

#np.savetxt("windkessel.csv", P1, delimiter=',')

#with open("windkessel.csv") as f:
    #for line in f:
        #print(line)