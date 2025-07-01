import numpy as np
import heapq
import matplotlib.pyplot as plt
from random import randint

#Building the world
class Environment:
    def __init__(self, width, height, wall_stuff, start_spot, goal_spot):
        self.width = width
        self.height = height
        self.start = start_spot
        self.goal = goal_spot

        self.grid = np.zeros((height, width))
        for x, y in wall_stuff:
            self.grid[y][x] = 1
    #Checking if the next spot is clear or not
    def is_spot_valid(self, spot):
        x, y = spot
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 0
        return False

#Finding best path from current spot to the end goal
def best_path(current_spot, goal_spot):
    return abs(current_spot[0] - goal_spot[0]) + abs(current_spot[1] - goal_spot[1])

#Complete movement Logic
def find_path(world, start, goal):
    checked_spots = set()
    steps_till_spot = {start: 0}
    came_from = {}
    spots_left = []
    steps_taken = 0
    i=0
    heapq.heappush(spots_left, (best_path(start, goal), start))
    #The Loooop
    while spots_left:
        estimated_total_steps, current_spot = heapq.heappop(spots_left)
        steps_taken += 1
        if current_spot == goal:
            return rebuild_path(came_from, start, goal), steps_taken
        if current_spot in checked_spots:
            continue
        checked_spots.add(current_spot)
        #Exploration logic
        x, y = current_spot
        for move_x, move_y in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_spot = (x + move_x, y + move_y)
            if not world.is_spot_valid(next_spot):
                continue
            steps_taken = steps_till_spot[current_spot] + 1
            if next_spot not in steps_till_spot or steps_taken < steps_till_spot[next_spot]:
                steps_till_spot[next_spot] = steps_taken
                came_from[next_spot] = current_spot
                estimated_total_steps = steps_taken + best_path(next_spot, goal)
                heapq.heappush(spots_left, (estimated_total_steps, next_spot))
    print("No path found.")
    return None, steps_taken

#Display path taken by retracing path
def rebuild_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

# Visualize the grid using matplotlib
def show_path(world, path):
    plt.imshow(world.grid, cmap='Greys', origin='lower')
    if path:
        x_cor, y_cor = zip(*path)
        plt.plot(x_cor, y_cor, 'bo')
    plt.plot(world.start[0], world.start[1], 'ro')
    plt.plot(world.goal[0], world.goal[1], 'go')
    plt.title("Pathfinding")
    plt.show()

#Using user input for end goal and maybe even start goal
print("Hello!! Please enter the goal position (x and y between 0 and 9)")
goal_x = int(input("Enter x: "))
goal_y = int(input("Enter y: "))
goal_spot = (goal_x, goal_y)
start_decision = input("Would you like to choose the start position? Please type Y/N: ").lower()
if start_decision == "y":
    print("Please enter (x and y between 0 and 9)")
    start_x = int(input("Enter x: "))
    start_y = int(input("Enter y: "))
    start_spot = (start_x, start_y)
#Default starting point given incase of "n" or wrong inputs
else:
    print("Default starting point set as (0,0)")
    start_spot = (0,0)

#Randomising obstacle locations
wall_bro = []
while len(wall_bro) < 5:
    x = randint(1, 9)
    y = randint(1, 9)
    spot = (x, y)
    if spot != start_spot and spot != goal_spot and spot not in wall_bro:
        wall_bro.append(spot)

#Calling all functions
world = Environment(10, 10, wall_bro, start_spot, goal_spot)
path, steps = find_path(world, start_spot, goal_spot)
if path:
    print(f"Path length: {len(path)}")
    for pos in path:
        print(pos)
else:
    print("No path found.")
show_path(world, path)
