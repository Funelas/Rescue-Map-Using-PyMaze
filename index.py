from pymaze import maze, agent, COLOR

m = maze(40,70)
m.CreateMaze(loadMaze= "maze--2025-05-12--18-11-15.csv")

m.run()