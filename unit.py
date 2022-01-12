from rewards import *

class Unit():
    life = 10
    atk = 1

    action_space = [attack, move]

    directions = {"up" : (-1, 0), "right":(0, 1), "left": (0, -1), "down" : (1, 0)}

    def __init__(self):
        self.life = Unit.life
        self.atk = Unit.atk
    
    def set_pos(self, p):
        self.x, self.y = p

    def attack(self, direction):
        reward = 0
        target = self.x + directions[direction][0], self.y + directions[direction][1]
        victim = env.get_unit(target)
        if victim != None and victim.team == self.team:
            victim.life -= self.atk
            reward += rewards['attack']

        return reward