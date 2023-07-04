#%% 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import pandas as pd
from scipy.interpolate import interp2d
#%%
table= pd.read_csv('/Users/Windows/Documents/GitHub/Moisture-Sensors/test/centered trimmean.csv')
print(table)
Sensor_val=np.array([table.loc[:,'M0'],table.loc[:,'M1'],table.loc[:,'M2']])
# Define the dataset
dataset = Sensor_val
#%%
# Extract the x-axis values (menstrual fluid added volume)
x_values = [0,0,0]#np.array([table.loc[:,'Ml']])[0]

# Extract the y-axis values (sensor positions)
y_values = [1/3,1/2,2/3]#['Front Sensor', 'Middle Sensor', 'Back Sensor']

# Extract the intensity values
intensity_values = Sensor_val
intensity=
#%%
# Define the grid for interpolation
x_grid, y_grid = np.meshgrid(np.arange(0,1,0.01), np.arange(0,2,0.01))

# Perform interpolation
interp_func = interp2d(x_values, y_values, intensity_values, kind='linear')

# Define the number of frames in the animation
num_frames = 100

# Define the x-values for each frame
x_frames = np.linspace(np.min(x_values), np.max(x_values), num_frames)
#%%

# Define the figure and axes
fig, ax = plt.subplots()

# Define the colormap
cmap = plt.cm.get_cmap('hot')

# Define the maximum intensity value for the color scale
max_intensity = np.max(intensity_values)
#%%
# Define the update function for the animation
def update(frame):
    ax.clear()
    ax.set_title('Heat Map')
    ax.set_xlabel('Menstrual Fluid Added Volume')
    ax.set_ylabel('Sensor Position')
    ax.set_xticks(x_values)
    ax.set_yticks(range(len(y_values)))
    ax.set_yticklabels(y_values)

    # Generate the interpolated intensity values for the frame
    interpolated_intensities = interp_func(x_frames[frame], y_grid)

    # Generate the heat map
    im = ax.imshow(interpolated_intensities, cmap=cmap, vmin=0, vmax=max_intensity)

    # Add color bar
    fig.colorbar(im)

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=200)

# Save the animation as a GIF
animation.save('heat_map.gif', writer='pillow')

# Display the plot (optional)
plt.show()
# %%
