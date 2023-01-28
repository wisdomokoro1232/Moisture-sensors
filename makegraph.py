import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 10.0, 0.01)
s = t**2 +2

Max_saturation= max(t)
Q1_val = 0.25*Max_saturation
Q2_val = 0.5*Max_saturation
Q3_val= 0.75*Max_saturation

Q1 = np.ma.masked_where(s < Q1_val, s)
Q2 = np.ma.masked_inside( s,Q1_val, Q2_val)
Q3 = np.ma.masked_inside(s,Q2_val , Q3_val)
Q4= np.ma.masked_where((s>=Q3_val ), s)
fig, ax = plt.subplots()
ax.plot(t, Q1, t, Q2, t, Q3, t, Q4)
plt.show()