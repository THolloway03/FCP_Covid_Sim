import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from matplotlib.lines import Line2D
%matplotlib qt

# Use a count variable in virus.py to add each number of infected, suspetable, recovered and dead people to a
# list which can then iterate each member of the list onto the graph.

#Using the list I can iterate through adding each member to the memeber before and dividing it by the total number
# of suseptable hexagons and multiplying by 100 to get the percentage of infected, dead, recovered or suspetable
#and append these values to the graph


# Test data to show how it works in the simulation
duration = 100#int(input("input the duration of the simulation"))
e = 2.7
l1 = [random.randint(-10,4)+(i**1.68)/(random.randint(13,14)) for i in range(0,160,2)]#suseptable
l2 = [random.randint(0,4)+(i**1.5)/(random.randint(9,11)) for i in range(0,160,2)]#infected
l3 = [5*e**(0.2*i) for i in range(0,duration)]#recovered
l4 = [random.randint(0,4)+(i**1.6)/(random.randint(10,13)) for i in range(0,160,2)]#dead



#customising the axes and the style used in ploting
fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
axes.set_ylim(0, 100)
axes.set_xlim(0, duration)
plt.style.use("seaborn")


#This creates an empty list which after each iterationn of i appends that value to the list in order for it to be plotted
x1,y1,y2,y3,y4 = [], [], [], [], []
xval = count(0,5)
def animate(i):
    x1.append(next(xval))
    y1.append((l1[i]))
    y2.append((l2[i]))
    y3.append((l3[i]))
    y4.append((l4[i]))
    

    #plots each line with the line customisation
    axes.plot(x1,y1, color="red")
    axes.plot(x1,y2, color="green", linewidth=0.5)
    axes.plot(x1,y3, color="blue")
    axes.plot(x1,y4, color="black")
    
anim = FuncAnimation(fig, animate, interval=200)

#creating a legend for the lines to show what each coloured line means
custom_lines = [Line2D([0], [0], color='red', lw=4,alpha=0.6),
                Line2D([0], [0], color='green', lw=4,alpha=0.6),
                Line2D([0], [0], color='blue', lw=4,alpha=0.6),
                Line2D([0], [0], color='black', lw=4,alpha=0.6)]

plt.legend(custom_lines, ['suseptable','infected', 'recovered', 'dead'])
# customize the x ticks
#plt.xticks([e+1 for e in x1])
