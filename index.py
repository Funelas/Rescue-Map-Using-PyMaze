from pymaze import maze, agent, COLOR
from collections import deque
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
    fwdPath={}
    cell=goal
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath


m = maze(40,70)
# m.CreateMaze(loadMaze= "maze--2025-05-12--18-11-15.csv", x= 18, y= 3)
m.CreateMaze(loadMaze="fixed_maze.csv", x=18, y=3)


sample_agent_pos = (27,16)
sample_agent = agent(m, x= sample_agent_pos[0], y=sample_agent_pos[1], footprints=True)
path = BFS(m,sample_agent_pos,(18,3))
m.tracePath({sample_agent: path})
m.run()
# m = maze(5,5)
# m.CreateMaze(loopPercent=100, x=2,y=3)
# path = BFS(m, (2,3))
# a = agent(m, footprints=True, x=2,y=5)
# m.tracePath({a:path})
# m.run()