# -*- coding: utf-8 -*-
"""
Created on Fri May  6 12:15:41 2022

@author: colin
"""

import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from matplotlib.lines import Line2D

import math
    
# used for testing
def doesInfect():
     if random.randrange(1,10) == 1:
        return 1
     else:
        return 0
         

SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2
DEAD = 3
VACCINATED = 4

COLOURMAP = {
    'susceptible': 'green',
    'infected': 'red',
    'recovered': 'blue',
    'dead': 'black',
    'vaccinated': "white",
    }
COLOURMAP_RGB = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    "white": (),
    }

STATUSES = {
    'susceptible': SUSCEPTIBLE,
    'infected': INFECTED,
    'recovered': RECOVERED,
    'dead': DEAD,
    'vaccinated': VACCINATED,
    }

# def doesInfect():                   # FOR TESTING PURPOSES
#       if random.randrange(1,10) == 1:
#         return 1
#       else:
#         return 0
        
def recovered():
    if random.randrange(1,10) == 2 :
        return 2
    else: 
        return 1
    
def dead():
    if random.randrange(1,10) == 3 :
        return 3
    else: 
        return 2
    
def vaccinated(value):
    if random.randrange(1,10) == 4 :
        return 4
    else: 
        return value 
    
rate_of_infection =3.0
chance_of_recovery = 0.6
fatality_rate = 0.05
rate_of_vaccination = 0.02
r0 = 2.5

num_susceptible = 0
num_infected = 0
num_recovered = 0
num_dead = 0
num_vaccinated = 0
day = 0      
# Used to find size that user wants the graph to be and allows it to be able to run a full number since its 
# a 2D matrix if we ask for a population it will be the number they want^2 so to allow this to work we need to 
# sqrt the number they ask for but that could end up with not full array sizes so we truncate it to give us a size we can use 

hexMatrix_size = input('Please enter how large you wish for the sample size to be ')
hexMatrix_size = int(hexMatrix_size)
hexMatrix_size = hexMatrix_size**(1/2)
hexMatrix_size = math.trunc(hexMatrix_size)

Time_duration = input(
    "how many days will the simulation last for? (to get greater results make days >= 30  ): ")


print('Your matrix will be of this size to allow it to function:')
print(hexMatrix_size)

# our goal is to have an array that allows each cell to interact with another cell (6 cells) 


hexMatrix = [[0 for x in range(hexMatrix_size)] for y in range(hexMatrix_size)]    
# creates the 2D array of the set size

complete_Array = ' '
Infected = 0

if hexMatrix_size <= 10: #infects 1 random person if less than or equal to 100  
    hexMatrix[random.randrange(0,hexMatrix_size-1)][random.randrange(0, hexMatrix_size-1)] = 1 
else: #infects 2 random people if above 100 people 
    hexMatrix[random.randrange(0,hexMatrix_size-1)][random.randrange(0, hexMatrix_size-1)] = 1
    hexMatrix[random.randrange(0,hexMatrix_size-1)][random.randrange(0, hexMatrix_size-1)] = 1
    
Count = 0
day_count = 0
# Double for loop to run through each matrix
while day_count <= int(Time_duration):
    for y in range(hexMatrix_size):
        for x in range(hexMatrix_size):
                            
            if hexMatrix[x][y] == 1: #checks if infected 
                # if rate_of_infection > round(random.random(), 2):  
                #     hexMatrix[x][y] == 1                    
                if y+1 != hexMatrix_size:
                    Infected = doesInfect()
                    if hexMatrix[x][y+1] == 0:
                        hexMatrix[x][y+1] = Infected
                        Infected = 0              
                
                if y-1 > -1:
                    Infected = doesInfect()
                    if hexMatrix[x][y-1] == 0:
                        hexMatrix[x][y-1] = Infected
                        Infected = 0       
                
                if x-1 > -1:
                    Infected = doesInfect()   
                    if hexMatrix[x-1][y] == 0:
                        hexMatrix[x-1][y] = Infected
                        Infected = 0   
                
                if x-1 > -1 and y-1 > -1:
                    Infected = doesInfect()
                    if hexMatrix[x-1][y-1] == 0:
                        hexMatrix[x-1][y-1] = Infected
                        Infected = 0   
                
                if x+1 != hexMatrix_size:  
                    Infected = doesInfect()    
                    if hexMatrix[x+1][y] == 0:
                        hexMatrix[x+1][y] = Infected
                        Infected = 0
                
                if x+1 < hexMatrix_size and y-1 > -1:
                    Infected = doesInfect()
                    if hexMatrix[x+1][y-1] == 0:
                        hexMatrix[x+1][y-1] = Infected
                        Infected = 0
                # num_infected +=1
                # when people recover        
                if chance_of_recovery > round(random.random(), 2):  
                    hexMatrix[x][y] == 2
                    
                if hexMatrix[x][y] == 2:
                    
                    if y+1 != hexMatrix_size:
                        Recovered = recovered()
                        if hexMatrix[x][y+1] == 1:
                            hexMatrix[x][y+1] = Recovered
                            Recovered = 1              
                    
                    if y-1 > -1:
                        Recovered = recovered()
                        if hexMatrix[x][y-1] == 1:
                            hexMatrix[x][y-1] = Recovered
                            Recovered = 1       
                    
                    if x-1 > -1:
                        Infected = doesInfect()   
                        if hexMatrix[x-1][y] == 1:
                            hexMatrix[x-1][y] = Infected
                            Infected = 0   
                    
                    if x-1 > -1 and y-1 > -1:
                        Recovered = recovered()
                        if hexMatrix[x-1][y-1] == 1:
                            hexMatrix[x-1][y-1] = Recovered
                            Recovered = 1   
                    
                    if x+1 != hexMatrix_size:  
                        Recovered = recovered()    
                        if hexMatrix[x+1][y] == 1:
                            hexMatrix[x+1][y] = Recovered
                            Recovered = 1
                    
                    if x+1 < hexMatrix_size and y-1 > -1:
                        Recovered = recovered()
                        if hexMatrix[x+1][y-1] == 1:
                            hexMatrix[x+1][y-1] = Recovered
                            Recovered = 1
                    # num_recovered += 1
                    # num_infected -= 1
                #people who dont recover
                if fatality_rate >  round(random.random(),2):
                    hexMatrix[x][y] = 3
                if hexMatrix[x][y] == 3:
                    if y+1 != hexMatrix_size:
                        Dead = dead()
                        if hexMatrix[x][y+1] == 1:
                            hexMatrix[x][y+1] = Dead
                            Dead = 1             
                    
                    if y-1 > -1:
                        Dead = dead()
                        if hexMatrix[x][y-1] == 1:
                            hexMatrix[x][y-1] = Dead
                            Dead = 1       
                    
                    if x-1 > -1:
                        Dead = dead()   
                        if hexMatrix[x-1][y] == 1:
                            hexMatrix[x-1][y] = Dead
                            Dead = 1   
                    
                    if x-1 > -1 and y-1 > -1:
                        Dead = dead()
                        if hexMatrix[x-1][y-1] == 1:
                            hexMatrix[x-1][y-1] = Dead
                            Dead = 1   
                    
                    if x+1 != hexMatrix_size:  
                        Dead = dead()    
                        if hexMatrix[x+1][y] == 1:
                            hexMatrix[x+1][y] = Dead
                            Dead = 1
                    
                    if x+1 < hexMatrix_size and y-1 > -1:
                        Dead = dead()
                        if hexMatrix[x+1][y-1] == 1:
                            hexMatrix[x+1][y-1] = Dead
                            Dead = 1
                #vaccinations            
                if rate_of_vaccination >  round(random.random(),2):
                    hexMatrix[x][y] = 4
                    
                if hexMatrix[x][y] == 4:
                    if y+1 != hexMatrix_size:
                        Vaccinated = vaccinated(hexMatrix[x][y])
                        if hexMatrix[x][y+1] == 1:
                            hexMatrix[x][y+1] = Vaccinated
                            Vaccinated = 1             
                    
                    if y-1 > -1:
                        Vaccinated = vaccinated(hexMatrix[x][y])
                        if hexMatrix[x][y-1] == 1:
                            hexMatrix[x][y-1] = Vaccinated
                            Vaccinated = 1       
                    
                    if x-1 > -1:
                        Vaccinated = vaccinated(hexMatrix[x][y])   
                        if hexMatrix[x-1][y] == 1:
                            hexMatrix[x-1][y] = vaccinated
                            Vaccinated = 1   
                    
                    if x-1 > -1 and y-1 > -1:
                        Vaccinated = vaccinated(hexMatrix[x][y])
                        if hexMatrix[x-1][y-1] == 1:
                            hexMatrix[x-1][y-1] = Vaccinated
                            Vaccinated = 1   
                    
                    if x+1 != hexMatrix_size:  
                        Vaccinated = vaccinated(hexMatrix[x][y])    
                        if hexMatrix[x+1][y] == 1:
                            hexMatrix[x+1][y] = Vaccinated
                            Vaccinated = 1
                    
                    if x+1 < hexMatrix_size and y-1 > -1:
                        Vaccinated = vaccinated(hexMatrix[x][y])
                        if hexMatrix[x+1][y-1] == 1:
                            hexMatrix[x+1][y-1] = Vaccinated
                            Vaccinated = 1
                    # num_dead += 1
                    # num_infected -= 1
                
    for y in range(hexMatrix_size):
        for x in range(hexMatrix_size):
            
            if hexMatrix[x][y] == 0:
                num_susceptible += 1
                
            if hexMatrix[x][y] == 1:
                num_infected +=1
            elif hexMatrix[x][y] == 2:
                num_recovered += 1
        
            elif hexMatrix[x][y] == 3:
                num_dead += 1

            elif hexMatrix[x][y] == (4):
                num_vaccinated += 1
                
            #Used to display to user for testing purposes 
            complete_Array = (complete_Array + str(hexMatrix[x][y]) + ' ') 
            if Count == hexMatrix_size-1: 
                complete_Array = complete_Array + '\n' + ' ' #used to add the entire array to a displayable string
                if y % 2 == 1:
                    complete_Array = complete_Array + ' '
                    
            Count = Count+1
    
        Count = 0
        
    def calc_percent(total_people, list):
        percentage = (list/total_people)*100
        return percentage
        
    #This iterates through the lists calculating the percentages to then append to the empty lists for the graph
    
    l1 = [calc_percent(num_susceptible, num_susceptible) for i in range(0, num_susceptible)]#susceptible
    
    l2 = [calc_percent(num_susceptible, num_infected) for i in range(0, num_infected)]#infected
    
    l3 = [calc_percent(num_susceptible, num_recovered) for i in range(0, num_recovered)]#recovered
    
    l4 = [calc_percent(num_susceptible, num_dead) for i in range(0, num_dead)]#dead
    
    l5 = [calc_percent(num_susceptible, num_vaccinated) for i in range(0, num_vaccinated)]#vaxed
    
    
    #customising the axes and the style used in ploting
    fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
    axes.set_ylim(0, 100, 0.5)
    axes.set_xlim(0, num_susceptible, 0.5)
    plt.xlabel("days")
    plt.ylabel("percentage")
    plt.style.use("seaborn-whitegrid")
    
    
    #This creates an empty list which after each iterationn of i appends that value to the list in order for it to be plotted
    x1,y1,y2,y3,y4,y5 = [], [], [], [], [], []
    xval = count(0,1)
    def animate(i):
        x1.append(next(xval))
        y1.append((l1[i]))
        y2.append((l2[i]))
        y3.append((l3[i]))
        y4.append((l4[i]))
        y5.append((l5[i]))
        
    
        #plots each line with the line customisation
        axes.plot(x1,y1, color="red")
        axes.plot(x1,y2, color="green", linewidth=5)
        axes.plot(x1,y3, color="blue")
        axes.plot(x1,y4, color="black")
        axes.plot(x1,y5, color="yellow")
        
    anim = FuncAnimation(fig, animate, interval=100)
    
    #creating a legend for the lines to show what each coloured line means
    custom_lines = [Line2D([0], [0], color='red', lw=4,alpha=0.6),
                    Line2D([0], [0], color='green', lw=4,alpha=0.6),
                    Line2D([0], [0], color='blue', lw=4,alpha=0.6),
                    Line2D([0], [0], color='black', lw=4,alpha=0.6),
                    Line2D([0], [0], color='yellow', lw=4,alpha=0.6)]
    
    plt.legend(custom_lines, ['susceptible','infected', 'recovered', 'dead', 'vaxcinated'])
# customize the x ticks
#plt.xticks([e+1 for e in x1])    
    day_count = day_count+1                
    complete_Array= ' '+ complete_Array
    #displaying the counts after each day wh
    print("Day: ",day_count)
    print("Susceptible:", num_susceptible)
    num_susceptible = 0
    print("Infected: ",num_infected)
    num_infected = 0
    print("Recovered: ",num_recovered)
    num_recovered = 0
    print("Dead: ", num_dead)
    num_dead = 0
    print("Vaccinated: ",num_vaccinated)
    num_vaccinated = 0
    print(complete_Array)
    complete_Array = ' '
    
    
# import random
# import matplotlib
# from matplotlib import animation
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from itertools import count
# from matplotlib.lines import Line2D
# from Grid_array import num_vaccinated, num_recovered, num_dead, num_infected, num_susceptible
# %matplotlib qt

#test variables:
    #infected_list = (1,2,3,4,6,8,12,16,22,28,36,46,59,73,76,82,85,87,90,93,96,99,100)
    #suseptable_list = (100,99,98,97,96,80,70,60,50,40,30,25,23,21,20,15,10,8,6,4,2,1)
    #total_people = 100
    #duration = 100#int(input("input the duration of the simulation"))


    # Use a count variable in grid_array to add each number of infected, suspetable, recovered and dead people to a
    # list which can then iterate each member of the list onto the graph.
    
    #Using the list I can iterate through adding each member to the memeber before and dividing it by the total number
    # of suseptable hexagons and multiplying by 100 to get the percentage of infected, dead, recovered or suspetable
    #and append these values to the graph
    
    #function to calculate the percentage of each item in a list
#     def calc_percent(total_people, list):
#         percentage = (list/total_people)*100
#         return percentage
        
#     #This iterates through the lists calculating the percentages to then append to the empty lists for the graph
    
#     l1 = [calc_percent(num_susceptible[0], num_susceptible[i]) for i in range(0, num_susceptible)]#susceptible
    
#     l2 = [calc_percent(num_susceptible[0], num_infected[i]) for i in range(0, num_infected)]#infected
    
#     l3 = [calc_percent(num_susceptible[0], num_recovered[i]) for i in range(0, num_recovered)]#recovered
    
#     l4 = [calc_percent(num_susceptible[0], num_dead[i]) for i in range(0, num_dead)]#dead
    
#     l5 = [calc_percent(num_susceptible[0], num_vaccinated[i]) for i in range(0, num_vaccinated)]#vaxed
    
    
#     #customising the axes and the style used in ploting
#     fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
#     axes.set_ylim(0, 100, 0.5)
#     axes.set_xlim(0, num_susceptible, 0.5)
#     plt.xlabel("days")
#     plt.ylabel("percentage")
#     plt.style.use("seaborn-whitegrid")
    
    
#     #This creates an empty list which after each iterationn of i appends that value to the list in order for it to be plotted
#     x1,y1,y2,y3,y4,y5 = [], [], [], [], [], []
#     xval = count(0,1)
#     def animate(i):
#         x1.append(next(xval))
#         y1.append((l1[i]))
#         y2.append((l2[i]))
#         y3.append((l3[i]))
#         y4.append((l4[i]))
#         y5.append((l5[i]))
        
    
#         #plots each line with the line customisation
#         axes.plot(x1,y1, color="red")
#         axes.plot(x1,y2, color="green", linewidth=5)
#         axes.plot(x1,y3, color="blue")
#         axes.plot(x1,y4, color="black")
#         axes.plot(x1,y5, color="yellow")
        
#     anim = FuncAnimation(fig, animate, interval=100)
    
#     #creating a legend for the lines to show what each coloured line means
#     custom_lines = [Line2D([0], [0], color='red', lw=4,alpha=0.6),
#                     Line2D([0], [0], color='green', lw=4,alpha=0.6),
#                     Line2D([0], [0], color='blue', lw=4,alpha=0.6),
#                     Line2D([0], [0], color='black', lw=4,alpha=0.6),
#                     Line2D([0], [0], color='yellow', lw=4,alpha=0.6)]
    
#     plt.legend(custom_lines, ['susceptible','infected', 'recovered', 'dead', 'vaxcinated'])
# # customize the x ticks
# #plt.xticks([e+1 for e in x1])
