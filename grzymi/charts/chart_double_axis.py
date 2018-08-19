import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mp

co = pd.read_csv('zwiazki.out', sep=' ' , usecols=[1], skiprows=3)
thc = pd.read_csv('zwiazki.out', sep=' ' , usecols=[5], skiprows=3)
co2 = pd.read_csv('zwiazki.out', sep=' ' , usecols=[2], skiprows=3)
o2 = pd.read_csv('zwiazki.out', sep=' ' , usecols=[3], skiprows=3)
no = pd.read_csv('zwiazki.out', sep=' ' , usecols=[4], skiprows=3)


fig, ax1 = plt.subplots(figsize=(8,8))
ax1.set_xlabel('Iterations [-]', fontsize=12)
ax1.set_ylabel(r'$CO_2$, $O_2$ [%], $CO$ [ppm]', fontsize=12)
ax1.plot(co, 'blue', label=r'$CO$',linewidth=2)
ax1.plot(co2, 'green', label=r'$CO_2$',linewidth=2)
ax1.plot(o2, 'red', label=r'$O_2$',linewidth=2)
ax1.set_ylim(0,40)
ax1.set_xlim(0,1400)
plt.grid(True)
plt.legend(loc=2, shadow=True, fontsize=12)

ax2 = ax1.twinx()

#color = 'tab:black'
ax2.set_ylabel(r'$THC$, $NO$ [ppm]', fontsize=12)#, color=color)
ax2.plot(thc, 'orange', label=r'$THC$',linewidth=2)
ax2.plot(no, 'black', label=r'$NO$',linewidth=2)
ax2.set_yscale('log')
ax2.set_ylim(10e0, 10e4)

plt.title ('Exhaust gas composition')
plt.grid(True)
#blue_patch = mp.Patch(color='blue', label='Wykres')
#plt.legend(handles=[blue_patch])
plt.legend(loc=0, shadow=True, fontsize=12)
fig.tight_layout()
plt.show()