from abc import abstractclassmethod


class Player():
    
    def __init__(self):
        self.units = []

        
    @abstractclassmethod
    def decide(self, state, unit):
        raise NotImplementedError()


class Human(Player):
    pass

class QAI(Player):
    pass