# Simple bar chart plot by Psalm Webb

# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Getting the list of ages
ages = [23,24,26,28,32,33,37,41,43,45]

# Getting the indexes of the ages
indexes = np.arange(len(ages))

# Setting a fixed bar width
width = 0.25


# List of salaries for all developers
dev_y  = [40000,45000,46000,50000,60000,62000,67000,70000,72000,100000]

#List of salaries for python developers

dev_py = [40000,41000,49000,57000,64000,65000,67000,71000,98000,102000]

# For styling the bar chart, Use "plot.style.available" to see available styles...
plt.style.use("ggplot")  

# Setting the y-label for the bar chart
plt.xlabel("Ages")
# Setting the x-label for the chart
plt.ylabel("Salaries")

# Then we plot the ages to their respective salaries
plt.bar(indexes - width,dev_y,label="Devs",color="k",width=width)
plt.bar(indexes,dev_py,label="Py Devs",color="steelblue",width=width)

# We replace the indexes with the ages
plt.xticks(ticks=indexes,labels=ages)

# We need a detailed chart
plt.legend()

# We show the plot
plt.show()
