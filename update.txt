#Have it where the cells are interacting with one another

#when highly infective the cells could have an infection rate of 2.0 so 
#the first cell will infect 2 other cells
#this makes the probability of 1 cell infecting 2 of its neighbors by 2/6

#of course this is assuming that there is no vaccination nor restrictions such as social distancing

#when restrictions and vaccination is in the model we will then reduce the rate of infection

#Vaccinations will reduce the rate of infection by more than a half.


from matplotlib.plt import plt
import math
import random
import pandas as pd
import numpy as np
 

class Interaction():
    """ this will import the create grid class to the  """

    COVID19_PARAMS = {
       "R0": 2.5,
       "INCUBATION": 5,
       "MILD_INFECTION": 1.0,
       "SEREVERE_INFECTION": 0.45,
       "MILD_RECOVERY": 2.0,
       "SERVERE_RECOVERY": 0.3,
       "FATALITY_RATE": 0.04,
       "VACCINATION_RATE": 3.0,  #rate of people being vaccinated
    }

    RGB_COLOUR = {
        'light blue': (152,245,255),
        'blue': (0,0,255),
        'purple': (128,0,128),
        'yellow' :(255,255,0),
        'red':(255,0,0),
        'green':(0,255,0),
        'black':(0,0,0),
    }

    STATUSES ={
        'VACCINATED': 'light blue',
        'SUSCEPTIBLE': 'blue',
        'IN-CONATCT': 'PURPLE'
        'INFECTION_MID': 'yellow',
        'INFECTION_SERVERE': 'red', 
        'RECOVERY':  'green',
        'DEAD': 'black',
        'SELF.ISOLATING': #dashed lines on the hexagons
    }


    def __init__(self, PARAMS):
        """ PARAMATERISING """
        self.R0 = PARAMS["R0"]
        self.Susceptible = PARAMS["Susceptible"]
        self.Probability_of_infection_mild = PARAMS[Probability_of_infection_mild]
        self.Probability_of_infection_servere = PARAMS[Probability_of_infection_servere]
        slef.Probability_of_recovery = PARAMS[Probability_of_recovery]
        self.Probability_of_death = PARAMS[Probability_of_death]

        #create number variables 
        #this is the initial number of people with the variables

        self.Population = ...  #this will be the number of hexs in the grid
        self.day = 0
        self.number_infected = 0
        self.number_recovered = 0
        self.number_deaths = 0

        # INITIAL STATE WHERE EVERYONE IS SUSCEPTIBLE
        self.state = np.zeros((width,height),int)
        self.state[:,:] = self.Susceptible

        # INITIAL STATE OF COVID19
        self.COVID_STATE = 

    def before_outbreak(self, population):
        """ Choses one person to be infected (PATIENT ZERO)"""
        for n in range(num):
           i = randint(self.width)
           j = randint(self.height)
           self.state[i,j] = self.INFECTED

    def spread_of_virus(self):
        """UPDATING THE POPULATION BY 1 DAY"""
        #ADVANCING THE SIMULATION BY ONE DAY


    def symptom_management(self): #assign the symptoms
        """  Updates the status of the population"""
        status = state[i,j]

        #update the susceptible person to be in-contact so they'll be in the incubation period
        status = state[i,j]
        
        #updating someone who is susceptible to the incubation period
        if status == self.SUSCEPTUBLE:
           num = self.Infected_around(state, i,j)
           if num * self.Incubation_state > random():
               return self.IN_CONTACT 

        #updting someone who is in contact to someone with servere or mild infection
        if status == self.IN_CONTACT:
            if self.Probability_of_infection_mild > random():
                 return self.Infected_Mild
            elif self.Probability_of_infection_servere > random():     
                  return self.Infected_Servere

        #updating statuses of people with mild or servere symptoms
        if status == self.Infected_Mild:
           if self.recovery_probability > random():
                 return self.Recovered
           elif self.probability_death > random():
                 return self.DEAD

        if status == self.infected_server:
           if self.recovery_probability > random():
                 return self.Recovered   ######## need to make it where its more difficult to recover
           elif self.Probability_death > random():
                 return self.Dead   ####increase the chances of death when the patient has servere symptoms
     

        if status == #either recovered, suceptible, can get vaccinated 

        return status 
         
    def Vaccinations(self):
        """ At a certain point in time there will be a patient who will be vaccinated"""
        """ any random person can be vaccinated they dont have to be next to someone in order to be vaccinated """
        #once the vaccine is released people who are recovered or still susceptible will be able to get vaccinated
        #only getting one vaccination as it'll complicate things too much
        #vaccinated people will be highlighted 

        self.Vaccination_release = Vaccination release

    def Mututations(self):
        """ ORIGINAL -> ALPHA -> BETA-> GAMMA -> DELTA -> OMNICRON  """
        #make the status of covid in the intstuctor and then update the status
        #at random points of time the virus will mutate into the next variant


    def update(self): 
        """updating the animation to where the cells will eventually infect all of its neighbors"""


    def animate(self):
        """ animating the grid over time and updating it by one day """

    def show_matrix(self):
        
        matrix = np.zeros((self.width, self.height, 3), int)
        for status, statusnum in self.STATUSES.items():
            #### this'll show the matrix of people at different stages of the vaccine

    def get_update_count(self):
        """ returns a count of the number of people in each status"""
             #try to show the states of different people in the grid 
             # also show which mutation is at 
        counts = {}


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
