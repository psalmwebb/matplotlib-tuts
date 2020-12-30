## Pie chart by Psalm webb

## Import the required modules

import matplotlib.pyplot as plt
import numpy as np


# plt.style.use("ggplot")

# Slices of each languages by popularity..

lang_slices = [100,90,60,55,45]

# Names of the languages..
labels = ["Python","Javascript","Java","C++","C#"]

# Logo Colors of each language
colors = ["#4B8BBE","#f0db4f","lightgrey","#555","#4B0082"]

# Laying emphasis on the javascript programming language
explode_params = [0,0.1,0,0,0]

# The title of the plot
plt.title("Slices of the most populous language")

# The we plot the pie
plt.pie(lang_slices,labels=labels,colors=colors,autopct="%1.1f%%",wedgeprops={"edgecolor":"white"},explode=explode_params)

# We show it
plt.show()




