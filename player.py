from abc import abstractclassmethod


class Player():
    
    def __init__(self, team):
        self.units = []
        self.team = team

        
    @abstractclassmethod
    def decide(self, state, unit):
        raise NotImplementedError()


class Human(Player):
    pass

class QAI(Player):
    def __init__(self, team):
        super().__init__(team)