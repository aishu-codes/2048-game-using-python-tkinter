import tkinter as tk
import random

root = tk.Tk()
root.title("2048 Game")

# Create grid for tiles
grid = [[0]*4 for _ in range(4)]

def draw():
    for i in range(4):
        for j in range(4):
            tile = grid[i][j]
            label = tk.Label(frame, text=str(tile) if tile != 0 else "", width=6, height=3, font=("Helvetica", 24), bg="lavender", fg="black", borderwidth=2, relief="ridge")
            label.grid(row=i, column=j, padx=5, pady=5)

def spawn():
    i, j = random.choice([(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0])
    grid[i][j] = random.choice([2, 4])

def compress(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row)-1):
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            new_row[i+1] = 0
    return [num for num in new_row if num != 0] + [0]*(4-len(new_row))

def move_left():
    global grid
    grid = [compress(row) for row in grid]
    spawn()
    draw()

def move_right():
    global grid
    grid = [list(reversed(compress(reversed(row)))) for row in grid]
    spawn()
    draw()

def move_up():
    global grid
    grid = list(map(list, zip(*grid)))
    grid = [compress(row) for row in grid]
    grid = list(map(list, zip(*grid)))
    spawn()
    draw()

def move_down():
    global grid
    grid = list(map(list, zip(*grid)))
    grid = [list(reversed(compress(reversed(row)))) for row in grid]
    grid = list(map(list, zip(*grid)))
    spawn()
    draw()

def key_press(event):
    if event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()

frame = tk.Frame(root)
frame.pack()

spawn()
spawn()
draw()

root.bind("<Key>", key_press)
root.mainloop()
