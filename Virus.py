#!/usr/bin/env python3
"""

from matplotlib.plt import plt
import math
import random
import pandas as pd
import numpy as np
 

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import argparse
from matplotlib.collections import PatchCollection
import random
import matplotlib.animation as animation

# def main(*args):
#   """ command line entry point """
#     parser = argparse.ArgumentParser(description='SIMULATING AN EPIDEMIC WITH A GIVEN POPULATION')

#     parser.add_argument('--population', metavar='N', type=int, default=1000,
#                         help='size of population')
#     parser.add_argument('--Vacciantion and Restrictions', metavar='N', type=int, default=1000,
#                         help='size of population')
#     parser.add_argument('--Vaccination', metavar='N', type=int, default=1000,
#                         help='size of population')
#     parser.add_argument('--Restrictions', metavar='N', type=int, default=1000,
#                         help='size of population')
#     args = parser.parse_args(args)
#     virus = 

COVID19_PARAMS = {
       "R0": 1.5,
       "INCUBATION": 7.0,
       "CHANCE_OF_INFECTION": 0.9,
       "INFECTED": (7,12),
       "PERCENT OF RECOVERY": 0.8,
       "FATALITY_RATE": 0.09,
       "SERIAL_INTERVAL": (7, 21),
       "DEATH": (20,30),
       "VACCINATION_RATE": 0.4,  
       "MUTATION_PROB": 0.3,    
    }

nfs = [1,2,3,4]
cols = {
        "1": "blue",
        "2": "red",
        "3": "black",
        "4": "green",
        "5": "white",
        } 
   
RGB_COLOUR = {
       'blue': (0,0,255),
       'red':(255,0,0),
       'green':(0,255,0),
       'black':(0,0,0),
       "white":(),
        }


class Virus():
    
    SUSCEPTIBLE = 0
    INFECTED = 0
    RECOVERED = 0
    DEAD = 0
    
    COVID19_PARAMS = {
       "R0": 1.5,
       "INCUBATION": 7.0,
       "CHANCE_OF_INFECTION": 0.9,
       "INFECTED": (7,12),
       "PERCENT OF RECOVERY": 0.8,
       "FATALITY_RATE": 0.09,
       "SERIAL_INTERVAL": (7, 21),
       "DEATH": (20,30),
       "VACCINATION_RATE": 0.4,  
       "MUTATION_PROB": 0.3,    
    }
    
    STATUSES = {
        'susceptible': SUSCEPTIBLE,
        'infected': INFECTED,
        'recovered': RECOVERED,
        'dead': DEAD,
        }
    
    COVID19_VARIANTS = {
       "ORIGINAL": 1.5,
       "ALPHA": 2.5,
       "BETA": 3.0,
       "GAMMA": 3.5,
       "DELTA": 4.0,
       "OMNICRON": 4.5,
       "RESCRICTIONS": 1.0,
       }
    
    STATUSES = {
        'VACCINATED': 'light blue',
        'susceptible': 'blue',
        'INFECTED': 'yellow',
        'HOSPITILISED': 'red', 
        'RECOVERED':  'green',
        'DEAD': 'black',
        }  

    def __init__(self, args):

        self.R0 = COVID19_PARAMS["R0"]
        self.infected = COVID19_PARAMS["INFECTED"]
        self.infection = COVID19_PARAMS["CHANCE_OF_INFECTION"]
        self.percent_of_recovery = COVID19_PARAMS["PERCENT_OF_RECOVERY"]
        self.incubation = COVID19_PARAMS["INCUBATION"]
        self.dead = COVID19_PARAMS["DEATH"]
        self.serial_interval0 = COVID19_PARAMS["SERIAL_INTERVAL"][0]
        self.serial_interval1 = COVID19_PARAMS["SERIAL_INTERVAL"][1]
        self.infection_slow = COVID19_PARAMS["INCUBATION"] + COVID19_PARAMS["INFECTED"][1]
        self.infection_fast = COVID19_PARAMS["INCUBATION"] + COVID19_PARAMS["INFECTED"][0]
        self.death_slow = COVID19_PARAMS["INCUBATION"] + COVID19_PARAMS["DEATH"][1]
        self.death_fast = COVID19_PARAMS["INCUBATION"] + COVID19_PARAMS["DEATH"][0]
      
        self.day = 0
        self.Population = population
        self.num_infected = 0
        self.number_recovered = 0
        self.number_deaths = 0
        self.num_Vaccinated = 0
        
        #getting values for the hexagons
        self.coords = []
        self.x_coords =[]
        self.xcoord = []
        self.ycoord = []
            
        for num in range(-5, 6):
            self.x_coords.append(num)
            for i in range(6):
                for j in range(6):
                    if (i % 2 != 0) and (j % 2 != 0) and (num < 0) and (num %2 != 0):
                        self.coords.append((num, i, 0))
                        self.coords.append((num, 0, j))
            for i in range(-5,1):
                for j in range(-5,1):
                    if (i % 2 != 0) and (j % 2 != 0) and (num > 0) and (num %2 != 0):
                        self.coords.append((num, i, 0))
                        self.coords.append((num, 0, j))
            for i in range(-4,0):
                for j in range(-4,0):
                    for k in range(1,4):
                        if (i % 2 != 0) and (j % 2 != 0) and (k % 2 != 0) and (num % 2 == 0):
                            self.coords.append((num, 0, 0))
                            self.coords.append((num, i, k))
                            self.coords.append((num, k, j))  
        self.coords = set(self.coords)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        
        self.xcoord = [c[0] for c in self.coords]      
        self.ycoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in self.coords]
        self.ax.set_aspect('equal')
        
        for x, y in zip(self.xcoord, self.ycoord):
            hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
                                  orientation=np.radians(30), facecolor=None,
                                  alpha=1.0, edgecolor='k')
            self.ax.add_patch(hex)

        self.ax.scatter(self.xcoord, self.ycoord, c='blue', alpha=1.0)
        for num in nfs:
            if num == 1:
                self.ax.add_patch(RegularPolygon((self.xcoord, self.ycoord), numVertices=6, radius=2. / 3., 
                                    orientation=np.radians(30), facecolor=cols[str(num)], 
                                    alpha=1.0, edgecolor='k'))
        self.ax.set_axis_off()
        
        #SUSCEPTIBLE PEOPLE
        self.state = [self.xcoord, self.ycoord]
        self.state = self.SUSCEPTIBLE
        self.patient_zero()
        
        self.infected = {i: {"xcoord": [], "ycoord": []} for i in range(self.infected, 365)}
        self.recovered = {"recovered": {i: {"xcoord": [], "ycoord": []} for i in range(self.recovered, 365)}}
        self.dead = {"dead": {i: {"xcoord": [], "ycoord": []} for i in range(self.death_fast, 365)}}

        self.exposed_before = 0
        self.exposed_after = 1 
        self.Vax_before = 0
        self.Vax_after = 1
   #     self.Mutations()

    def patient_zero(self):
        
        self.num_infected = 1
        self.total_infected = 1
        self.x = [i for i in self.xcoord]
        self.y = [i for i in self.ycoord]
        for num in nfs:
            if num == 2:
                self.ax.add_patch(RegularPolygon(
                    (0, 0), numVertices=6, radius=2. / 3., orientation=np.radians(30), 
                    facecolor=cols[str(num)], alpha=1.0, edgecolor='k'))
        
    def spread_virus(self, i):
 
        self.exposed_before = self.exposed_after
        if self.day % self.serial_interval[0] == 0 and self.exposed_before < self.Population:
            self.num_infected = round(self.R0 * self.total_infected)
            self.exposed_after += round(self.new_infected * 1.1)
            if self.exposed > self.Population:
                self.num_new_infected = round((self.Population - self.exposed_before) * 0.9)
                self.exposed_after = len(self.xcoord)
            self.exposed_after = len(self.xcoord)
            self.total_infected += self.num_infected
            #|RANDOMLY SELECT NEWLY INFECT PEOPLE| 
            self.infected_indicies = list(np.random.choice(
                range(self.exposed_before, self.exposed_after),
                self.new_infected, replace=False)
                )
            xcoord = [self.x[i] for i in self.infected_indicies]
            ycoord = [self.y[i] for i in self.infected_indicies]
            self.ax.scatter(self.xcoord,self.ycoord , s=100, c="red")
            for num in nfs:
                if num == 2:
                    self.ax.add_patch(RegularPolygon(
                        (xcoord, ycoord), numVertices=6, radius=2. / 3., orientation=np.radians(30),
                        facecolor=cols[str(num)], alpha=1.0, edgecolor='k'))
            self.symptoms()
            
        self.day +=1
        self.update_status()
        self.UPDATE_ANNOTATIONS()


    def symptoms(self, state, i, j):

        self.num_infection = round(self.infection * self.new_infected)   
        # CHOOSING RANDOM PEOPLE WHO ARE NEWLY INFECTED TO HAVE A MILD SYMPTOMS
        self.infected_indices = np.random.choice(
            self.new_infected_indicies, self.num_infection, replace=False
            )
        
        self.num_recovered = round(self.percent_of_recovery * self.num_infected)
        remaining_indicies = [
            i for i in self.new_infected if i not in self.infected_indices
            ]
        
        self.recovered_indicies = []
        self.death_indicies = []
        if remaining_indicies:
            self.recovered_indicies = random.choice(
                remaining_indicies, self.num_recovered, replace=False)
            self.death_indicies = [
                i for i in remaining_indicies if i not in self.recovered_indicies
                ]
        
        # assigning recovery/death day
        # infected
        #===========================================
        # status = state[i,j]
        # if status == self.infected:
        #     if self.recovery > random():
        #         return self.recovered 
        #     elif self.death > random():
        #         return self.dead
        # elif status == self.susceptible:
        #     if (num * self.infection_fast) or (num * self.infected_slow) > random():
        #         return self.INFECTED
        # return status
        ##=========================================== 
        #recovery day from infected
            low = self.day + self.infection_fast   
            high = self.day + self.infection_slow
            for infected in self.infected_indicies:
                recovery_day = np.random.choice(low, high)
                self.recovered_x = self.xcoord[infected]
                self.recovered_y = self.ycoord[infected]
                self.recovered[recovery_day]["x"].append(self.recovery_x)
                self.infected[recovery_day]["y"].append(self.recovery_y)
        #death
            low = self.day + self.death_fast
            high = self.day + self.death_slow
            for dead in self.death_indicies:
                death_day = np.random.choice(low, high)
                self.dead_x = self.xcoord[dead]
                self.dead_y = self.ycoord[dead]
                self.servere["Dead"][death_day]["xcoords"].append(self.death_x)
                self.servere["Dead"][death_day]["ycoords"].append(self.death_y)
         

    def update_status(self):
        
        if self.day >= (self.infected_fast or self.infected_slow):
            infected_x = self.infected[self.day]["xcoords"]
            infected_y = self.infected[self.day]["ycoords"]
            for num in nfs:
                if num == 2:
                    self.ax.add_patch(RegularPolygon(
                        (infected_x, infected_y), numVertices=6, radius=2. / 3., 
                        orientation=np.radians(30), facecolor=cols[str(num)], 
                        alpha=1.0, edgecolor='k')
                        )
            self.number_recovered += len(infected_x)
            self.num_infected -= len(infected_x)
            
        if self.day >= self.death_fast:
            death_x = self.death["death"][self.day]["xcoords"]
            death_y = self.death["death"][self.day]["ycoords"]
            self.ax.scatter(infected_x, infected_y, s=5, color = "black")
            for num in nfs:
                if num == 3:
                    self.ax.add_patch(RegularPolygon(
                        (death_x, death_y), numVertices=6, radius=2. / 3.,
                        orientation=np.radians(30), facecolor=cols[str(num)],
                        alpha=1.0, edgecolor='k')
                        )
            self.num_dead += len(death_x)
            self.num_infected -= len(death_x)
            
    def Mutations(self):
        """ THE MUTATIONS PROBABILITY WILL BE USED IN THIS FUNCTION TO 
        FOR HOW THIS WORKS IS THAT EVERY WEEK THERE IS A CHANCE THAT 
        ORIGINAL -> ALPHA -> BETA -> GAMMA -> DELTA -> OMNICRON        
        """
        if self.day % self.serial_interval1 == 0:
            if self.MUTATE > random.random():
                up_dict = {"R0": 2.5}
                COVID19_PARAMS.update(up_dict)
                self.R0 = self.COVID19_PARAMS["R0"]
            else:
                return self.R0
    
        if self.day % self.serial_interval1 == 0 and (self.COVID19_PARAMS["R0":2.5]):
            if self.MUTATE > random.random():
                up_dict = {"R0": 3.2}
                COVID19_PARAMS.update(up_dict)
                self.R0 = self.COVID19_PARAMS["R0"]              
            else:
                return self.R0

        if self.day % self.serial_interval1 == 0 and self.COVID19_PARAMS["R0": 3.2]:
            if self.MUTATE > random.random():
                up_dict = {"R0": 3.8}
                COVID19_PARAMS.update(up_dict)
                self.R0 = self.COVID19_PARAMS["R0"]
            else:
                return self.R0

        if self.day % self.serial_interval1 == 0 and self.COVID19_PARAMS["R0": 3.8]:
            if self.MUTATE > random.random():
                up_dict = {"R0": 4.5}
                COVID19_PARAMS.update(up_dict)
                self.R0 = self.COVID19_PARAMS["R0"]
            else:
                return self.R0

        if self.day % self.serial_interval1 == 0 and self.COVID19_PARAMS["R0": 4.5]:
            if self.MUTATE > random.random():
                up_dict = {"R0": 5.2}
                COVID19_PARAMS.update(up_dict)
                self.R0 = self.COVID19_PARAMS["R0"]                
            else:
                return self.R0

    def Spread_Vaccinations(self):
        """
        Vaccine will be 'created' when the percentage of infcted is over 30%
        """

        if (self.num_infected / self.Population * 100) >= 30:
            self.Vaxed_before = self.Vaxed_after
            if (self.day % self.serial_interval1 == 0) and (self.Vax_before < self.Population):
                self.num_vaccinated = round(self.VACCINATION_RATE * self.num_recovered)
                self.Vaxed_after += round(self.newly_Vaxed * 1.1)
                if self.Vax_after > self.Population:
                    self.num_vaccinated = round((self.Population - self.vax_before) * 0.9)
                    self.vax_after = self.Population

                self.currently_vaccinated += self.num_vaccinated
                self.total_vaccinated += self.num_vaccinated

            # |RANDOMLY SELECT NEWLY VACCINATE PEOPLE| 
                self.new_vaccinated_indicies = list(np.random.choice(
                    range(self.vax_before, self.vax_after),self.new_vaccinated, replace=False)
                    )
                xcoords = [self.xcoords[i] for i in self.new_vaccianted_indicies]
                ycoords = [self.ycoords[i] for i in self.new_vaccianted_indicies]
                for num in nfs:
                    if num == 5:
                        self.ax.add_patch(RegularPolygon(
                            (xcoords, ycoords), numVertices=6, radius=2. / 3.,
                            orientation=np.radians(30), facecolor=cols[str(num)],
                            alpha=1.0, edgecolor='k'))
    
    def restrictions(self):

        if (self.num_infection / self.population * 100) >= 40:
        # | reduce the the variables to nearly zero to simulate a full lockdown - escenssial trips only |
            up_dict = {"R0": 0.2}
            COVID19_PARAMS.update(up_dict)
            self.R0 = self.COVID19_PARAMS["R0"]
            self.lockdown_text = self.axes.annotate(
                "Lockdown", ha="centre", va="bottom") 
            
        elif (self.num_infection / self.population * 100) >= 25:
        #| reduce the variables to 1/2 or 1/3 - simulating social distancing, mask wearing, etc|
            up_dict = {"R0": 1.0}
            COVID19_PARAMS.update(up_dict)
            self.R0 = self.COVID19_PARAMS["R0"]
            self.Restrictions_text = self.axes.annotate(
                "Restrictions", ha="centre", va="bottom") 

    def UPDATE_ANNOTATIONS(self):
  
        self.DAY_ANNOTATIONS.set_text("DAY {}".format(self.day))
        self.INFECTED_ANNOTATIONS.set_text("INFECTED: {}".format(self.num_new_infected))
        self.RECOVERED_ANNOTATIONS.set_text("RECOVERED: {}".format(self.num_recovered))
        self.DEATH_ANNOTATIONS.set_text("DEATH: {}".format(self.num_deaths))
        self.MUTANT_ANNOTATIONS.set_text("Mutant: {}".format(self.CURRENT_MUTANT))
      
    def animation(self,filename):
         #""" INITILISE THE ANIMATION AND THE AUTOMATICALLY SAVE IT INTO A FILE """
        self.animation = animation.FuncAnimation(self.fig, self.spread_virus(), frames = 500, repeat=True)
        self.animation.save(filename, fps=30, extra_args=['-vcodec', 'libx264'])


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])