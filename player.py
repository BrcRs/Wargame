from abc import abstractclassmethod
from unit import Unit

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
    def __init__(self, team):
        super().__init__(team)