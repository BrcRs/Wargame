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

    def reset(self):
        self.eps = QAI.eps_init

    def decide(self, env, state, unit): # TODO finish
        self.eps *= QAI.eps_decay
        if random.random() < self.eps:
            # action = random action from action space
            # action = random.choice(np.flatnonzero(observation['action_mask']))
            # print(agent, "chose a random action")
            available_actions = env.valid_actions(state, unit) # TODO write that method
            action = random.choice(available_actions) # TODO comprehensive action space in unit
        else:
            # action = best action from Q = max_i(Q(S, i))
            # np.flatnonzero(Q[agent][state][action_mask == 1])
            action = max([i for i in range(nA) if action_mask[i] == 1], key = lambda x: Q[agent][state][x])
        return action