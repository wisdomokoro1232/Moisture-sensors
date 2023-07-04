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

    #Time increment between readings on arduino secs
    Increment= 30
    #Read first value from humidity sensors- initial val
    Humidity_old= Humidity.iloc[1]
    print(Humidity_old)
    count=1
    #initialise these so if not changed then you know neither conditions were met
    time_sat='Not applicable'
    time_abs='Not applicable'
    for i in range(2,Record_length):
        #save humidity val being looked at
        Humidity_new= Humidity.iloc[i]
        if (Humidity_new-Humidity_old) > 5 and count==1:
            #time it started absorbing at in hours
            time_abs= (Increment*i)/3600
            #Stop checking for this conditiom
            count=0
        if Humidity_new > 95:
            #time it became saturated at
            time_sat= (Increment*i)/3600
            break
        sensorstat=np.array([Avg_Temp,time_sat,time_abs,maxhumidity])
    return sensorstat

sensor1= Sensor_val('Moisture.csv')
print(sensor1)
