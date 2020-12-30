import matplotlib.pyplot as plt


ages = [23,24,26,28,32,33,37,41,43,45]

# We create a list of developer's ages

dev_y  = [40000,45000,46000,50000,60000,62000,67000,70000,72000,100000]

# And a list of their salaries
dev_py = [40000,41000,49000,57000,64000,65000,67000,71000,98000,102000]

# Adding styles to the plot, To see all available styles run "plt.style.available"
plt.style.use("ggplot")

# We gave the plot a title
plt.title("Medium salary for devs in US")

# We gave the plot x-axis and y-axis labels
plt.xlabel("Ages")
plt.ylabel("Salaries")

# Then we plot
plt.plot(ages,dev_y,marker=".")
plt.plot(ages,dev_py,marker="o")

plt.legend(["Devs","Py Devs"])

# plt.show()


plt.show()
