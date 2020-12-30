 # Simple horizontal bar charts by Psalm Webb

 # Import the relevant modules
import matplotlib.pyplot as plt
import numpy as np


# Creating the list of most populous languages
languages = ["Python","Javascript","Java","Php","C","C++","C#","Ruby","Swift","Objective-C"]

percent  = [98,97,90,84,83,83,81,74,70,63]

plt.style.use("ggplot")

plt.title("The Most Populous programming language")

plt.barh(languages,percent)

plt.show()