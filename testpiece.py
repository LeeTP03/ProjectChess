from grid import Grid

class TPiece():
    
    def __init__(self, x, y, color) -> None:
        self.name = "TP"
        self.color = None
        self.set_color(color)
        self.position = [x,y]
        
    def set_color(self, color):
        if color == "white":
            self.color = True
        elif color == "black":
            self.color = False
            
    def set_position(self, x, y):
        self.position = [x, y]
    
    def possible_move(self, grid:Grid):
        lst = []
        
        for i in range(grid.row):
            for j in range(grid.columns):
                lst.append([i,j])
        
        return lst