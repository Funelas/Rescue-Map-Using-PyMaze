from pymaze import maze, agent, COLOR
from collections import deque
import customtkinter as ctk
def BFS(m, start = (1,1), goal = (1,1)):
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    else:
        print("Path not found!")
    fwdPath={}
    cell=goal
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

hospital_coordinates = [(18,3), (15,7), (10,21), (25,22), (19,22), (11,27), (3,27), (19,29), (9,32), (24,33), (14,45), (30,46), (38,69)]
police_coordinates = [(15,8), (28,12), (20,14), (13,15), (10,20), (13,22), (20,22), (23,23), (19,28), (6,31), (17,33), (20,40), (24,42), (3,49), (13,50), (10,62)]
accidents_coordinates = [(27,16), (38,20), (14,32), (38,36), (31,46), (6,61), (22,61)]
m = maze(40,70)

m.CreateMaze(loadMaze="maze--2025-05-12--18-11-15.csv")


for coord in hospital_coordinates:
    a = agent(m, x=coord[0], y=coord[1], footprints=True, color=COLOR.light)
    path = BFS(m, coord, (21,22))

for coord in police_coordinates:
    a = agent(m, x=coord[0], y=coord[1], footprints=True, color=COLOR.red, filled= True)


for coord in accidents_coordinates:
    a = agent(m, x=coord[0], y=coord[1], footprints=True, filled= True, color=COLOR.green)


goal = (28,12)
sample_agent_pos = (38,20)
sample_agent = agent(m, x= sample_agent_pos[0], y=sample_agent_pos[1], footprints=True)
path = BFS(m,sample_agent_pos, goal)
m.tracePath({sample_agent: path})

m.run()
