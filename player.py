from abc import abstractclassmethod


def Player():
    
    @abstractclassmethod
    def decide(self, state, unit):
        raise NotImplementedError()

def Human(Player):
    pass

def QAI(Player):
    pass