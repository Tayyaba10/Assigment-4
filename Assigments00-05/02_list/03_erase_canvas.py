"""
Implement an 'eraser' on a canvas.
The canvas consists of a grid of blue 'cells' which are
drawn as rectangles on the screen. We then create an eraser 
rectangle which, when dragged around the canvas, sets all of
the rectangles it is in contact with to white.
"""
import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):

    cells = []

    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):

        row_cells = []

        for col in range(0,CANVAS_WIDTH,CELL_SIZE):

            rect = canvas.create_rectangle(row, col, row + CELL_SIZE, col + CELL_SIZE, fill = "blue", outline ="black")
            row_cells.append(rect)
        cells.append(row_cells)

    return cells        
# create eraser
def erase(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill = "white")


def main():
    # globally use canvas, grid
    global canvas,grid

    root = tk.Tk()
    root.title("Eraser Canvas")

    # create canvas
    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")

    # bind mouse event
    canvas.bind("<B1-Motion>", erase)
    canvas.pack()

    # create grid
    grid = create_grid(canvas)

    root.mainloop()

if __name__ == '__main__':
    main()