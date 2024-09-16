from tkinter import Tk, BOTH, Canvas

class Window:
    """ Creates the window that the program will run in """
    def __init__(self, width=500, height=500) -> None:
        # Starts the window & Creates a new root widget using Tk() and saves it as a data member
        self.__root = Tk()
        self.__root.title("----> Maze Solver <----")
        self.__canvas = Canvas(master=self.__root, bg='white', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """ method to redraw all the graphics in the windown. """
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


    def wait_for_close(self):
        """ Sets self.win_running = True and keeps calling redraw() as long as win_running = True """
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

class Point:
    """ drawing some lines """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    """ Creates lines? """
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2


    def draw(self, canvas, fill_color='black'):
        canvas.create_line(
            self.pos1.x, self.pos1.y, self.pos2.x, self.pos2.y, fill=fill_color, width=2
            )
        
class Cell:
    """ Creates cell's needed to fill the grid """
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall: # Just a test, needs to be modified
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        
