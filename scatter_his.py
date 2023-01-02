#pip install mplcursors #conda install -c conda-forge fast-histogram 
#conda install -c conda-forge mpl-scatter-density #pip install mlxtend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.cm as cm
# Read the CSV file 
df = pd.read_csv('/Users/your files dir/example_1.csv')
# x and y columns from the DataFrame has been selected by following line
x = df['X'].values
y = df['Y'].values
# mapping from string values (which can be seen in next line)to integers values
location_mapping = {'c1': 1,'c2': 1, 'c3': 1, 'c4': 1, 'b1': 3, 'b2': 3, 'b3': 3, 'b4': 3, 'center': 5,
                    'b1_center': 4, 'b2_center': 4, 'b3_center': 4, 'b4_center': 4, 
                    'c1_b1': 2, 'c1_b4': 2, 'c4_b4': 2, 'c4_b3': 2, 'c3_b3': 2, 'c3_b2': 2, 'c2_b2': 2, 'c2_b1': 2}
# string values to integers with  mapping method
z = df['ROI_location'].map(location_mapping).values
# create a colormap from the integer values
#cmap = cm.ScalarMappable(cmap='cool')
cmap = cm.ScalarMappable(cmap='viridis')
colors = cmap.to_rgba(z)
#########################################
# list of labels for  different positions in open field box and in 14th line it has been mentioned
location_labels = [1, 2, 3, 4, 5]
#########################################
# create  scatterplot, in here z can be changed into some number 
#but because z is different in different regions so it creates better dots size with different size 
fig, axScatter = plt.subplots(figsize=(10, 11), sharex='col', sharey='row')
axScatter.scatter(x, y, c=colors, s=z*18)
axScatter.set_aspect(1.)
#########################################
# Mark the first x and y values
first_x = x[0]
first_y = y[0]
# make a black star for the first x and y values in your csv file
axScatter.scatter(first_x, first_y, c='black', marker='*', s=600)
#########################################
# this is the list of patch objects for the legend to make a clear the colors understadable
from matplotlib.patches import Rectangle
patches = []
for i in range(1, 6):
    color = cmap.to_rgba(i)
    patch = Rectangle((0, 0), 1, 1, fc=color)
    patches.append(patch)

# Create the legend using the labels and the colormap
legend = plt.legend(patches, location_labels, title='Box positions\n color box', fontsize=6.5, 
                    loc='center', bbox_to_anchor=(1.088, 1.0855), ncol=1, handletextpad=6)
# This is the discription text to the plot at right side
plt.text(1.072, 1.02, "corner\ncor_to_bor \nborder\nbor_to_cen \ncenter",linespacing=1.5,
         transform=axScatter.transAxes, fontsize=7, color='black', fontweight='bold', ha='left', zorder=10)
# you can  chose to set the color of the legend text to match the color of the corresponding data points
#if you deactive his line the numbers will apear in the end of the legend box
plt.setp(legend.get_texts(), color='w')
# Add the legend to the plot
plt.gca().add_artist(legend)
# these are little histogram axes for x anf y which represents the frequencies of the datapoints
divider = make_axes_locatable(axScatter)
axHistx = divider.append_axes("top", 1, pad=0.05, sharex=axScatter)
axHisty = divider.append_axes("right", 1, pad=0.05, sharey=axScatter)
# axis labels
axScatter.set_xlabel('Open field box X-axis', fontsize=15)
axScatter.set_ylabel('Open field box Y-axis', fontsize=15)

# this is the arbitrary limits by hand for your nuber of bars through bins
binwidth = 90
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1)*binwidth
bins = np.arange(0, lim + binwidth, binwidth)
# this is changabel to othr colors too, or you can remove it and then delete  color= HIScolor too 
HIScolor = ['blue']
# plot the histograms . if you like you can add to the next line weights=z, but I do not recommend it
axHistx.hist(x, bins=bins, density=False, color= HIScolor, alpha=0.9 )
axHisty.hist(y, bins=bins, orientation='horizontal')
# these lines are not necessary anymore but it represents the colorbar
#sm = cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=min(z), vmax=max(z)))
#cbar = plt.colorbar(sm, ax=axHistx)
# set tick marks
axHistx.set_yticks([0, 500, 1000, 1500, 2000, 2500])
axHistx.set_title('X-axis', loc='center', fontdict={'fontsize': 13, 'fontweight': 'medium'})
axHisty.set_xticks([0, 1000, 2000])
axHisty.set_title('Y-axis', loc='center', fontdict={'fontsize': 13, 'fontweight': 'medium'}, y=-0.08)
plt.savefig('scat_his.jpg', dpi=600)
plt.show()