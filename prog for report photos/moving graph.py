#%%
import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import seaborn as sns
import pandas as pd
import numpy as np
import statistics as stat
import scipy.stats as scip
#%%
#makes the plot come out in sns format
sns.set()
#read table into python and duration coloumn
table= pd.read_csv('/Users/Windows/Documents/GitHub/Moisture-Sensors/test/trend.csv')
Sensor_val=np.array([table.loc[:,'M0'],table.loc[:,'M1'],table.loc[:,'M2']])
n=len(Sensor_val[0])
#Moisture array based on increments of moisture added
Moisture= np.array([table.loc[:,'Ml']])
Moisture=Moisture[0]
#%%
x=[]
y1=[]
y2=[]
y3=[]
fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
axes.set_ylim(-5, 120)
axes.set_xlim(0, 32)
axes.set_xlabel('Menstrual Fluid added (Ml)')
axes.set_ylabel('Sensor Output (Arb.)')
plt.style.use("ggplot")
count=0
#%%
def animate(i):
    x.append(Moisture[i])
    y1.append((Sensor_val[0,i]))
    y2.append((Sensor_val[1,i]))
    y3.append((Sensor_val[2,i]))
    plt.title(f"Sensor Outputs for {Moisture[i]}ml of Fluid added")
    axes.plot(x,y1, scaley=True, scalex=True, color="blue",label="Front Sensor")
    axes.plot(x,y2, scaley=True, scalex=True, color="orange",label="Middle Sensor")
    axes.plot(x,y3, scaley=True, scalex=True, color="black",label="Back sensor")
        

#%%
anim = FuncAnimation(fig, animate, interval=1)
#%%
f = r'/Users/Windows/Documents/GitHub/Moisture-Sensors/test/graphtrend.gif'
writergif = animation.PillowWriter(fps=10) 
anim.save(f, writer=writergif)