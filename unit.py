from rewards import *

class Unit():
    life = 10
    atk = 1

    directions = {"U" : (-1, 0), "R":(0, 1), "L": (0, -1), "D" : (1, 0)}

    actions = {
        "atk-U" : lambda env: attack(env, directions["U"]),
        "atk-D" : lambda env: attack(env, directions["D"]),
        "atk-R" : lambda env: attack(env, directions["R"]),
        "atk-L" : lambda env: attack(env, directions["L"]),

        "mov-U" : lambda env: move(env, directions["U"]),
        "mov-D" : lambda env: move(env, directions["D"]),
        "mov-R" : lambda env: move(env, directions["R"]),
        "mov-L" : lambda env: move(env, directions["L"]),
    }

    def __init__(self, pos):
        self.life = Unit.life
        self.atk = Unit.atk
        self.pos = pos
    
    def set_pos(self, p):
        self.x, self.y = p

    def attack(self, env, direction):
        reward = 0
        target = self.x + self.directions[direction][0], self.y + self.directions[direction][1]
        victim = env.get_unit(target)
        if victim != None and victim.team == self.team:
            victim.life -= self.atk
            reward += rewards['atk']

        return reward

    def is_dead(self):
        return self.life <= 0
    
    def valid_actions(self, env):
        valid_actions = [k for k in self.actions.keys() if k[:3] == "atk"]
        mov_keys = [k for k in self.actions.keys() if k[:3] == "mov" and env.is_empty(self.pos + self.directions[k])]
        return valid_actions + mov_keys