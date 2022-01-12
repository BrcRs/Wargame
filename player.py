from abc import abstractclassmethod


def Player():
    
    def __init__(self):
        self.units = []

        
    @abstractclassmethod
    def decide(self, state, unit):
        raise NotImplementedError()


def Human(Player):
    pass

def QAI(Player):
    pass