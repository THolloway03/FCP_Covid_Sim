# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:26:50 2022

@author: taiho
"""


import math
import random
    
# used for testing
def doesInfect():
     if random.randrange(1,10) == 1:
        return 1
     else:
        return 0
         

    
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
hexMatrix[3][3] = 1 #TEST
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
    print(day_count)
    print(complete_Array)
    complete_Array = ' '

# if hexMatrix_size <= 10: #infects 1 random person if less than or equal to 100  
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 1 
# else: #infects 2 random people if above 100 people 
#         hexMatrix[random.randrange(0,hexMatrix_size-1)] = 1
#         hexMatrix[random.randrange(0,hexMatrix_size-1)] = 1









        