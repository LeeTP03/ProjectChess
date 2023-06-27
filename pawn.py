# from grid import Grid

class Pawn():
    
    def __init__(self, x, y, color) -> None:
        self.name = "P"
        self.color = None
        self.set_color(color)
        self.position = [x,y]
        self.initial_position = True
        
    def set_color(self, color):
        if color == "white":
            self.color = True
        elif color == "black":
            self.color = False
            
    def set_position(self, x, y):
        if self.initial_position == True:
            self.initial_position = False
        self.position = [x, y]
        
    def possible_move(self, grid):
        lst = []
        row, col = self.position[0], self.position[1]
        
        if self.color == True:
        
            if self.initial_position == True and row == 2:
                lst.append([row+2, col])
                
            if row+1 <= grid.row and grid.check_free(row+1, col):
                lst.append([row+1, col])

            if row+1 <= grid.row and col+1 <= grid.columns :
                if grid.get_tile_color(row+1, col+1) == False:
                    lst.append([row+1, col+1])
                    
            if row+1 <= grid.row and col-1 >= 0 :
                if grid.get_tile_color(row+1, col-1) == False:
                    lst.append([row+1, col-1])
        
        elif self.color == False:
            
            if self.initial_position == True and row == 7:
                lst.append([row-2, col])
            
            if row-1 > 0 and grid.check_free(row-1, col):
                lst.append([row-1, col])
            
            if row-1 > 0 and col+1 < grid.columns :
                if grid.get_tile_color(row-1, col+1) == True:
                    lst.append([row-1, col+1])
                    
            if row-1 > 0 and col-1 > 0 :
                if grid.get_tile_color(row-1,col-1) == True:
                    lst.append([row-1, col-1])
        
        return lst

    def __str__(self) -> str:
        return f"{self.color} Pawn"
                
