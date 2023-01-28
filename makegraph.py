import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10.0, 10.0, 0.1)
s = t**2 -5

Max_saturation= max(s)
Q1_val = 0.25*Max_saturation
Q2_val = 0.5*Max_saturation
Q3_val= 0.75*Max_saturation

#Hides values greater than Q1
Q1 = np.ma.masked_outside(s,0 , Q1_val)
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