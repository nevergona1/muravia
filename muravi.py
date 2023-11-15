import tkinter as tk

def draw_maze(canvas, maze):
    cell_size = 30  # Размер ячейки лабиринта

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                cell_color = "black"
            elif maze[row][col] == 2:
                cell_color = "white"
            else:
                cell_color = "gray"

            x = col * cell_size
            y = row * cell_size
            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=cell_color, outline="black")

def toggle_cell(event):
    col = event.x // cell_size
    row = event.y // cell_size

    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        maze[row][col] = 1 if maze[row][col] == 0 else 0
        draw_maze(canvas, maze)

# Создаем главное окно
root = tk.Tk()
root.title("Редактор лабиринта")

# Создаем холст
canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Размер ячейки лабиринта
cell_size = 30  

# Создаем пустой лабиринт
maze_width = canvas_width // cell_size
maze_height = canvas_height // cell_size
maze = [[0] * maze_width for _ in range(maze_height)]

# Привязываем событие клика мыши
canvas.bind("<Button-1>", toggle_cell)

# Рисуем лабиринт на холсте
draw_maze(canvas, maze)

# Запускаем главный цикл
root.mainloop()
