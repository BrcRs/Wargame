def Unit():
    life = 10
    atk = 1
    def __init__(self):
        self.life = Unit.life
        self.atk = Unit.atk
    
    def set_pos(self, p):
        self.x, self.y = p
        