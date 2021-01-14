# Written by Alan Tu
# 14 January 2021
# Saga, Elevator Control Exercise

"""
For this problem we make several simplifying assumptions:
1. Requests can only be made at discrete "time steps": at every "exchange", or whenever the elevator is empty.
Multiple people can make requests at each time step. 
2. When requesting a real elevator, people press up or down to specify which direction they want to travel.
We shall ignore this extra piece of information, and pretend that there is only one button to request the elevator.
3. Our elevator has unlimited capacity.
"""

import sys

class Elevator:
    def __init__(self, stories, reqs_list):
        self.stories = stories # number of floors in building
        self.at_reqs = {} # the floors at which people are waiting, outside the elevator;
        # waiting floor corresponds to desired floor(s) (int : list)
        self.to_reqs = {} # the floors requested from people inside the elevator;
        # requested floor corresponds to number of people who requested that floor (int : int)
        self.floor = 0 # the elevator's current floor
        self.up = True # is the elevator going up? (false means it's going down)
        self.reqs_list = reqs_list # ordered list of requests
        self.reqs_done = False # have we taken all the requests?
    
    def update(self):
        """
        Reads one time step worth of requests. Returns True if we've finished reading the request list.
        Returns False otherwise.
        """
        line = self.reqs_list.readline()
        if not line:
            return True
        if not line.strip(): # empty line denotes that no requests were made at this time step
            return False
        parsed = line.strip('\n').split(', ')
        for req in parsed:
            at = int(req.split('-')[0]) # waiting at this floor for elevator to arrive
            to = int(req.split('-')[1]) # would like to reach this floor
            if at in self.at_reqs:
                self.at_reqs[at].append(to)
            else:
                self.at_reqs[at] = [to]
        return False

    def exchange(self):
        """
        Picks up and/or drops off people on a given floor.
        """
        # dropping off
        dropped_off = 0 # number of people dropped off
        if self.floor in self.to_reqs:
            dropped_off = self.to_reqs[self.floor]
            self.to_reqs.pop(self.floor)

        # picking up
        picked_up = 0 # number of people picked up
        if self.floor in self.at_reqs: 
            dests = self.at_reqs[self.floor] # list containing requested destinations
            picked_up = len(dests)
            for d in dests:
                if d in self.to_reqs:
                    self.to_reqs[d] += 1
                else: # no entry exists yet
                    self.to_reqs[d] = 1
            self.at_reqs.pop(self.floor)   

        print("Dropped off %i person(s) and picked up %i person(s) at Floor %s." % (dropped_off, picked_up, self.floor))
    
    def check(self):
        """
        Checks if the elevator needs to open on the current floor.
        """
        if (self.floor in self.at_reqs) or (self.floor in self.to_reqs):
            self.exchange()
            if not self.reqs_done:
                self.reqs_done = self.update()
    
    def run(self):
        """
        Runs the elevator until the elevator is empty and no requests are left.
        """
        self.update() # gotta start somewhere

        while (not self.reqs_done) or self.at_reqs or self.to_reqs:
            # covers the case where there are no requests, and no one is in the elevator,
            # but we have not reached the end of the request list (i.e. an idle elevator)
            while (not self.reqs_done) and (not self.at_reqs) and (not self.to_reqs):
                self.reqs_done = self.update()

            if self.up:
                # while there are still requested floors above us (either from inside or outside), move up
                while self.floor <= max(max(self.at_reqs.keys(), default = 1), 
                                        max(self.to_reqs.keys(), default = 1)):
                    self.floor += 1
                    self.check()
            else:
                while self.floor >= min(min(self.at_reqs.keys(), default = self.stories), 
                                       min(self.to_reqs.keys(), default = self.stories)):
                    self.floor -= 1
                    self.check()

            self.up = not self.up # reverse direction

        
reqs_list = open(sys.argv[1], 'r')
elev = Elevator(int(sys.argv[2]), reqs_list)
elev.run()