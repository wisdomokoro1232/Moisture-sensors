import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.tsa import tsatools 

#makes the plot come out in sns format
sns.set()

#read table into python and duration coloumn
table= pd.read_csv('Moisture.csv')
Sensor_Val= table.loc[:,"Value"]

increment= input('How often were the values read (In seconds)? ')
n_readings=len(Sensor_val)
t = np.arange(0, n_readings*increment, increment)

Max_saturation= max(Sensor_val)
Min_saturation= min(Sensor_val)
Saturation_range= Max_saturation-Min_saturation
Q1_val = 0.25*Saturation_range +Min_saturation
Q2_val = 0.5*Saturation_range + Min_saturation
Q3_val= 0.75*Saturation_range + Min_saturation

#Hides values greater than Q1
Q1 = np.ma.masked_outside(s,Min_saturation , Q1_val)
#Hides values OUTSIDE of Q1 and Q2
Q2 = np.ma.masked_outside( s,Q1_val, Q2_val)
#Hides Values outside of Q2 and Q3
Q3 = np.ma.masked_outside(s,Q2_val , Q3_val)
#Hides values less than Q3
Q4= np.ma.masked_where((s<Q3_val ), s)
fig, ax = plt.subplots()
ax.plot(t, Q1, 'r',label= '<25% Saturation')
ax.plot(t, Q2,'blue',label='25%<~<50% Saturation')
ax.plot( t, Q3,'green',label='50%<~<75% Saturation')
ax.plot( t, Q4,'purple',label='>75% Saturation')
leg = ax.legend();
plt.show()