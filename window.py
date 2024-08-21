from tkinter import Tk, BOTH, Canvas


class window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        root = Tk()
        root.geometry(f"{self.height}x{self.width}")
        root.title("Maze Solver")


        root.mainloop()


print(window(500, 500))