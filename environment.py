
from tools import is_number
from player import *

class Environment():
    def __init__(self, map=None, discrete=["state", "action"]):
        self.map = map
        self.players = {}
        self.walls = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if is_number(self.map[i][j]):
                    n = self.map[i][j]
                    self.map[i][j] = ''
                    if n not in self.players.keys():
                        self.players.append(QAI(n))
                    self.players[n].add_unit((i, j))
                if self.map[i][j] == "W":
                    self.walls.append((i, j))
                    

    def add_player(self, p):
        self.players.append(p)

    def upd_map(self, player, action):
        raise NotImplementedError()

    def get_state(self, player, u):
        """
        Returns the current state of the game in the point of view of `player`.
        The player should know about:
            - The current unit he's about to play
            - The current positions of its units
            - The current health of its units
            (- the map? or static for now?)
            - The current positions of enemy units
            - The current health of enemy units
        """
        state = ""
        
        state += str(u.x) + "," + str(u.y) + " "
        # Allied units
        sorted_units = player.units.copy()
        sorted_units.sort(key = lambda f: f.x * 1000 + f.y) # TODO find something better
        for unit in sorted_units:
            state += str(unit.life) + ":" + str(unit.x) + "," + str(unit.y) + " "
        state += "|"
        # Ennemy units
        s_ennemy_units = [un for un in p.units for p in self.players if un.team != u.team]
        s_ennemy_units.sort(key = lambda f: f.x * 1000 + f.y) # TODO find something better
        for unit in s_ennemy_units:
            state += str(unit.life) + ":" + str(unit.x) + "," + str(unit.y) + " "

        return state

    def render(self):
        raise NotImplementedError()

    def step(self, player, unit):
        state = self.get_state(player)
        action = player.decide(state, unit)

        reward = unit.action(self)
        newstate = self.get_state(player)
        player.get_feedback(state, action, reward, newstate)

        for p in self.players:
            if len(p.units) == 0:
                return True
        
        return False
    
    def is_empty(self, point):
        u_points = [un.pos for un in p.units for p in self.players]
        if point in u_points or point in self.walls:
            return False
        return True