from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.geometry(f"{self.height}x{self.width}")
        self.__root.title("Maze Solver")
        C = Canvas(self.__root, bg="black", height=self.height, width=self.width)
        self.running = False

        C.pack()
        self.__root.mainloop()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False