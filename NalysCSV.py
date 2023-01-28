import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def Sensor_val(file):
    table= pd.read_csv(file)
    Humidity= table.loc[:,"Humidity"]
    Avg_Temp= np.mean(table.loc[:,'Temperature'])
    maxhumidity=np.max(Humidity)
    Record_length=len(Humidity)

    #Time increment between readings on arduino
    Increment= 30
    #Read first value from humidity sensors- initial val
    Humidity_old= table.iloc[1]
    print(Humidity_old)
    count=1
    for i in range(2,Record_length):
        Humidity_new= Humidity.iloc[i]
        if (Humidity_new-Humidity_old) > 5 and count==1:
            #time it started absorbing at
            time_abs= Increment*i
            #Stop checking for this conditiom
            count=0
        if Humidity_new > 95:
            #time it became saturated at
            time_sat= Increment*i
    return [Avg_Temp,time_sat,time_abs]

sensor1= Sensor_val('Moisture.csv')
