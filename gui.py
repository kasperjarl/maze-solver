from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{height}x{width}")
        self.__root.title("Maze Solver")
        self.__win = Canvas(self.__root, bg="black", height=height, width=width)
        self.__win.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__win, fill_color)

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y

class Line:
    def __init__(self, input1, input2) -> None:
        self.input1 = input1
        self.input2 = input2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.input1.x, self.input1.y, self.input2.x, self.input2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = True
        self._x2 = True
        self._y1 = True
        self._y2 = True
        self._win = True