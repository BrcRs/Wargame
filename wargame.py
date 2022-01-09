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
        u = random.choice(units)
        p = u.player
        done = env.step(p, u)
        history.append(env.map.copy())
    
    if display:
        ani.animate(history)

if __name__ == "__main__":
    main()