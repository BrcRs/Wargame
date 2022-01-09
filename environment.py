


def Environment():
    def __init__(self, map=None, discrete=["state", "action"]):
        self.map = map
        self.players = []

    def add_player(self, p):
        self.players.append(p)

    def upd_map(self, player, action):
        raise NotImplementedError()

    def get_state(self, player):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def step(self, player, unit):
        state = get_state(player)
        action = player.decide(state, unit)

        reward = self.upd_map(player, action)


        for p in self.players:
            if len(p.units) == 0:
                return True
        
        return False
