class Surface:
    def __init__(self, x, y, w, l):
        self.x = x
        self.y = y
        self.width = w
        self.length = l

    def getRect(self):
        return (self.x, self.y, self.width, self.length)


