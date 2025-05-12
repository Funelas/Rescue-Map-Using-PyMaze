from pymaze import maze
from turtle import Turtle, Screen

# Create the maze
m = maze(5, 5)
m.CreateMaze()

# Now, use turtle to label coordinates
screen = Screen()
pen = Turtle()
pen.hideturtle()
pen.penup()

cell_size = m._cellSize  # size of one cell (default: 40)
offset = m._Offset       # padding offset

for row in range(m.rows):
    for col in range(m.cols):
        # Convert row, col to turtle x, y coordinates
        x = col * cell_size - offset + cell_size / 3
        y = offset - row * cell_size - cell_size / 1.5
        
        pen.goto(x, y)
        pen.write(f'({row},{col})', font=('Arial', 8, 'normal'))

screen.mainloop()
