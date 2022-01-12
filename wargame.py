from environment import Environment
import random

# a player can:
# Move a unit in any or four directions
# Attack with a unit in any or four directions

def main():
    mymap = [
        ['1', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ['1', '1', "W", "W", ' ', ' ', "W", ' ', ' ', ' ']
        ['1', '1', "W", ' ', ' ', ' ', "W", ' ', ' ', ' ']
        ["W", ' ', "W", ' ', ' ', ' ', "W", ' ', ' ', ' ']
        ["W", ' ', "W", ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ["W", ' ', "W", ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        [' ', ' ', "W", ' ', ' ', ' ', ' ', "W", "W", "W"]
        [' ', ' ', ' ', ' ', ' ', "W", ' ', ' ', '2', '2']
        [' ', ' ', "W", "W", ' ', "W", ' ', ' ', '2', '2']
        [' ', ' ', ' ', ' ', ' ', "W", ' ', ' ', '2', '2']
    ]

    env = Environment(map=mymap)

    players = env.players

    units = [u for u in p.units for p in players]
    history = []
    while not done:
        if len(units) == 0:
            units = [u for u in p.units for p in players]
        
        u = random.choice(units)
        units.remove(u)
        if u.is_dead():
            continue

        p = u.player
        # step gives the player the moment to play
        done = env.step(p, u)
        history.append(units)
        if display:
            print(env.map)
            time.sleep(0.01)
    # if display:
    #     ani.animate(env.map, history)

if __name__ == "__main__":
    main()