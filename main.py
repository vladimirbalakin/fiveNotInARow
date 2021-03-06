import tkinter as tk

w, h = 640, 480
root = tk.Tk()
root.title("Five in a row?")
canvas = tk.Canvas(root, bg="#AF00FF", height=h, width=w)
canvas.pack()


def draw_line(x, y, x_, y_, color):
    canvas.create_line(x, y, x_, y_, width=2, fill=color)
    root.update()


class Point:
    x, y = 0, 0


class Polygon:

    def __init__(self):
        self.scale = 20
        self.table = [[0 for i in range(w // self.scale + 1)] for j in range(h // self.scale + 1)]
        for i in range(0, h, self.scale):
            draw_line(0, i, w, i, '#000000')
        for i in range(0, w, self.scale):
            draw_line(i, 0, i, h, '#000000')

    def add_x(self, x, y):
        x //= self.scale
        y //= self.scale
        if self.table[y][x] == 0:
            self.table[y][x] = 1
        else:
            return 1
        draw_line(x * self.scale, y * self.scale, (x + 1) * self.scale, (y + 1) * self.scale, '#FF0000')
        draw_line(x * self.scale, (y + 1) * self.scale, (x + 1) * self.scale, y * self.scale, '#FF0000')
        return 0

    def add_o(self, x, y):
        x //= self.scale
        y //= self.scale
        if self.table[y][x] == 0:
            self.table[y][x] = -1
        else:
            return 1
        return 0


def upd_mouse(event):
    x = event.x
    y = event.y
    global mouse
    mouse.x = x
    mouse.y = y


def addx(event):
    poly.add_x(mouse.x, mouse.y)


poly = Polygon()
mouse = Point()

root.bind('<Motion>', upd_mouse)
root.bind('<ButtonPress-1>', addx)

canvas.mainloop()
root.mainloop()
