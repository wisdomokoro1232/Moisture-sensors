#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#makes the plot come out in sns format
sns.set()
#%%
#read table into python and duration coloumn
table= pd.read_csv('Moisture.csv')
Sensor_val= table.loc[:,"Moisture"]

increment= int(input('How often were the values read (In seconds)? '))
n_readings=len(Sensor_val)
t = np.arange(0, n_readings*increment, increment)


#%%
Max_saturation= max(Sensor_val)
Min_saturation= min(Sensor_val)
#get a range of workign values 
Saturation_range= Max_saturation-Min_saturation
Q1_val = 0.25*Saturation_range +Min_saturation
Q2_val = 0.5*Saturation_range + Min_saturation
Q3_val= 0.75*Saturation_range + Min_saturation


#%%
#Hides values greater than Q1
Q1 = np.ma.masked_outside(Sensor_val,Min_saturation , Q1_val)
#Hides values OUTSIDE of Q1 and Q23
Q2 = np.ma.masked_outside( Sensor_val,Q1_val, Q2_val)
#Hides Values outside of Q2 and Q3
Q3 = np.ma.masked_outside(Sensor_val,Q2_val , Q3_val)
#Hides values less than Q3
Q4= np.ma.masked_where(Sensor_val <Q3_val , Sensor_val)

#%%
fig, ax = plt.subplots()
ax.plot(t, Q4, 'r',label= '<25% Saturation')
ax.plot(t, Q3,'blue',label='25%<~<50% Saturation')
ax.plot( t, Q2,'green',label='50%<~<75% Saturation')
ax.plot( t, Q1,'purple',label='>75% Saturation')
leg = ax.legend();
plt.xlabel("Time (s)")
plt.ylabel("Moisture senseor output")
plt.show()
# %%
