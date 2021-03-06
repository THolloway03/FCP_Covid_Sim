# -*- coding: utf-8 -*-
"""
Created on Fri May  6 12:15:41 2022

@author: colin
"""



import math
import random
    
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

STATUSES = {
    'susceptible': SUSCEPTIBLE,
    'infected': INFECTED,
    'recovered': RECOVERED,
    'dead': DEAD,
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
    
def vaccinated():
    if random.randrange(1,10) == 4 :
        return 4
    else: 
        return 2 or 3
    
chance_of_infection =1.0
chance_of_recovery = 0.7
fatality_rate = 0.05
rate_of_vaccination = 0.2
r0 = 2.5

num_infected = 0
num_recovered = 0
num_dead = 0
num_vaccinated = 0
day = 0      
# Used to find size that user wants the graph to be and allows it to be able to run a full number since its 
# a 2D matrix if we ask for a population it will be the number they want^2 so to allow this to work we need to 
# sqrt the number they ask for but that could end up with not full array sizes so we truncate it to give us a size we can use 

hexMatrix_size = input('Please enter how large you wish for the sample size to be')
hexMatrix_size = int(hexMatrix_size)
hexMatrix_size = hexMatrix_size**(1/2)
hexMatrix_size = math.trunc(hexMatrix_size)


print('Your matrix will be of this size to allow it to function:')
print(hexMatrix_size)

# our goal is to have an array that allows each cell to interact with another cell (6 cells) 


hexMatrix = [[0 for x in range(hexMatrix_size)] for y in range(hexMatrix_size)]    
# creates the 2D array of the set size

complete_Array = ' '
Infected = 0

hexMatrix[3][3] = 1
# if hexMatrix_size <= 10: #infects 1 random person if less than or equal to 100  
#     hexMatrix[random.randrange(0,hexMatrix_size-1)][random.randrange(0, hexMatrix_size-1)] = 1 
# else: #infects 2 random people if above 100 people 
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 1
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 1
    
count = 0
day_count = 0
# Double for loop to run through each matrix
while day_count <= 9:
    for y in range(hexMatrix_size):
        for x in range(hexMatrix_size):
                            
            if hexMatrix[x][y] == 1: #checks if infected 
                                
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
                    # num_dead += 1
                    # num_infected -= 1
                
    for y in range(hexMatrix_size):
        for x in range(hexMatrix_size):
            
            if hexMatrix[x][y] == 1:
                num_infected +=1
            elif hexMatrix[x][y] == 2:
                num_recovered += 1
        
            elif hexMatrix[x][y] == 3:
                num_dead += 1

            elif hexMatrix[x][y] == (2 or 0):
                num_vaccinated += 1
                
            #Used to display to user for testing purposes 
            complete_Array = (complete_Array + str(hexMatrix[x][y]) + ' ') 
            if count == hexMatrix_size-1: 
                complete_Array = complete_Array + '\n' + ' ' #used to add the entire array to a displayable string
                if y % 2 == 1:
                    complete_Array = complete_Array + ' '
                    
            count = count+1
    
        count = 0
        
    day_count = day_count+1                
    complete_Array= ' '+ complete_Array
    #displaying the counts after each day wh
    print("Day: ",day_count)
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