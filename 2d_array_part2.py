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

def susceptible():
    if random.randrange(0,10) == 0 :
        return 0
    else: 
        return 0

def doesInfect():
    if random.randrange(0,10) == 1 :
        return 1
    else: 
        return 0

def recovered():
    if random.randrange(0,10) == 2 :
        return 2
    else: 
        return 0
    
def dead():
    if random.randrange(0,10) == 3 :
        return 3
    else: 
        return 0
    
def vaccinated():
    if random.randrange(0,10) == 4 :
        return 4
    else: 
        return 0
    
chance_of_infection =0.9
chance_of_recovery = 0.8
fatality_rate = 0.1
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
duration = input("How many days would you like to run the simulation?")
hexMatrix_size = int(hexMatrix_size)
hexMatrix_size = hexMatrix_size**(1/2)
hexMatrix_size = math.trunc(hexMatrix_size)
num_susceptible = int(hexMatrix_size)

print('Your matrix will be of this size to allow it to function:')
print(hexMatrix_size)

# our goal is to have an array that allows each cell to interact with another cell (6 cells) 


hexMatrix = [[0 for x in range(hexMatrix_size)] for y in range(hexMatrix_size)] 

state = hexMatrix 

# creates the 2D array of the set size
complete_Array = ' '
Infected = 0
# if hexMatrix_size <= 10: #infects 1 random person if less than or equal to 100
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 2
# else: #infects 2 random people if above 100 people
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 2
#     hexMatrix[random.randrange(0,hexMatrix_size-1)] = 2
hexMatrix[3][3] = 2 #TEST
count = 0
day_count = 0

while day_count <= int(duration):
    
    for y in range(hexMatrix_size):
        for x in range(hexMatrix_size):
            
            #updating the people who are susceptibe to infected
            if hexMatrix[x][y] == 0:
                num = num_infected 
                if num * chance_of_infection > round(random.random(), 2):
                    hexMatrix[x][y] == 1           
                else:
                    hexMatrix[x][y] =0
            #infcted to revered/dead
            if hexMatrix[x][y]== 1:
                if chance_of_recovery >round(random.random(), 2):
                    hexMatrix[x][y] = 2
            
                elif fatality_rate > round(random.random(), 2):
                    hexMatrix[x][y] = 3
            
            if hexMatrix[x][y] ==(0 or 1 or 2):
                if rate_of_vaccination > round(random.random(), 2):
                    hexMatrix[x][y] = 4                    
                       
            if (x,y) == 2:
                num_infected +=1
                num_susceptible -= 1
            elif (x,y) == 3:
                num_recovered +=1
                num_infected -= 1
            elif (x,y) == 4:
                num_vaccinated += 1
    print(day_count)
    print(complete_Array)
    day_count+=1
# Double for loop to run through each matrix
for y in range(hexMatrix_size):
    for x in range(hexMatrix_size):               
        if hexMatrix[x][y] == 1: #checks if infected 
        
            if y+1 != hexMatrix_size:
                Infected = doesInfect()
                hexMatrix[x][y+1] = Infected
                Infected = 0
                       
            if y-1 > 0:
                Infected = doesInfect()
                hexMatrix[x][y-1] = Infected
                Infected = 0
           
            if x-1 > 0:
                Infected = doesInfect()   
                if hexMatrix[x-1][y] == 0:
                    hexMatrix[x-1][y] = Infected
                Infected = 0
            
            if x-1 > 0 and y-1 > 0:
                Infected = doesInfect()
                hexMatrix[x-1][y-1] = Infected
                Infected = 0
            
            if x+1 != hexMatrix_size:  
                Infected = doesInfect()            
                hexMatrix[x+1][y] = Infected
                Infected = 0
            
            if x+1 < hexMatrix_size and y-1 > 0:
                Infected = doesInfect()
                hexMatrix[x+1][y-1] = Infected
                Infected = 0
                
        # if hexMatrix[x][y] == 3: #checks 
        
        #     if y+1 != hexMatrix_size:
        #         Recovered = recovered()
        #         hexMatrix[x][y+1] = Recovered
        #         recovered = 3
            
            
        #     if y-1 > 0:
        #         Recovered = recovered()
        #         hexMatrix[x][y-1] = Recovered
        #         Recovered = 3
           
        #     if x-1 > 0:
        #         Recovred = recovered()   
        #         if hexMatrix[x-1][y] == 0:
        #             hexMatrix[x-1][y] = Recovered
        #         Recovered = 0
            
        #     if x-1 > 0 and y-1 > 0:
        #         Recovered = recovered()
        #         hexMatrix[x-1][y-1] = Recovered
        #         Recovered = 0
        
        #     if x+1 != hexMatrix_size:  
        #         Recovered = recovered()            
        #         hexMatrix[x+1][y] = Recovered
        #         Recovered = 0
            
        #     if x+1 < hexMatrix_size and y-1 > 0:
        #         Recovered = recovered()
        #         hexMatrix[x+1][y-1] = Recovered
        #         Recovered = 0
 
        # if hexMatrix[x][y] == 4: #checks if recovered 
        
        #     if y+1 != hexMatrix_size:
        #         Dead = dead()
        #         hexMatrix[x][y+1] = Dead
        #         Dead = 4
                       
        #     if y-1 > 0:
        #         Dead = dead()
        #         hexMatrix[x][y-1] = Dead
        #         Dead = 4
           
        #     if x-1 > 0:
        #         Dead = dead()   
        #         if hexMatrix[x-1][y] == 0:
        #             hexMatrix[x-1][y] = Dead
        #         Dead = 4
           
        #     if x-1 > 0 and y-1 > 0:
        #         Dead = dead()
        #         hexMatrix[x-1][y-1] = Dead
        #         Dead = 4
            
        #     if x+1 != hexMatrix_size:  
        #         Dead = dead()
        #         hexMatrix[x+1][y] = Dead
        #         Dead = 0
            
        #     if x+1 < hexMatrix_size and y-1 > 0:
        #         Dead = dead()
        #         hexMatrix[x+1][y-1] = Dead
        #         Dead = 0           
        
        #Used to display to user for testing purposes (not complete)
        complete_Array = (complete_Array + str(hexMatrix[x][y]) + ' ') 
        if count == hexMatrix_size-1: 
            complete_Array = complete_Array + '\n' + ' ' #used to add the entire array to a displayable string
            if y % 2 == 1:
                complete_Array = complete_Array + ' '
                
        count = count+1

    count = 0
            
complete_Array= ' '+ complete_Array
print(complete_Array)