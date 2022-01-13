from abc import abstractclassmethod
from unit import Unit
import random

class Player():
    
    def __init__(self, team):
        self.units = []
        self.team = team

        
    @abstractclassmethod
    def decide(self, state, unit):
        raise NotImplementedError()

    def add_unit(self, pos):
        self.units.append(Unit(pos))

class Human(Player):
    pass

class QAI(Player):
    eps_init = 1.0
    eps_decay = .99999

    def __init__(self, team):
        super().__init__(team)
        self.eps = QAI.eps_init
        self.Q = {}

    def reset(self):
        self.eps = QAI.eps_init

    def decide(self, env, state, unit): # DONE finish
        self.eps *= QAI.eps_decay
        available_actions = unit.valid_actions(env) # TODO write that method
        if state not in self.Q.keys():
            self.Q[state] = {}
        for a in available_actions:
            if a not in self.Q[state].keys():
                self.Q[state][a] = 0.
        if random.random() < self.eps:
            # action = random action from action space
            action = unit.actions[random.choice(available_actions)] # TODO comprehensive action space in unit
        else:
            # action = best action from Q = max_i(Q(S, i))
            action = unit.actions[max(available_actions, key = lambda x: self.Q[state][x])]
        return action