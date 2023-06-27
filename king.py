from grid import Grid

class King():
    
    def __init__(self, x, y, color) -> None:
        self.name = "K"
        self.color = None
        self.set_color(color)
        self.enemy_color = not self.color
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

        row, col = self.position
        
        if row-1 > 0:
            if grid.check_free(row-1, col) or grid.get_tile_color(row-1, col) == self.enemy_color:
                lst.append([row-1,col])
            if col-1 > 0 and (grid.check_free(row-1, col-1) or grid.get_tile_color(row-1, col-1) == self.enemy_color):
                lst.append([row-1,col-1])
            if col+1 <= grid.columns and (grid.check_free(row-1, col+1) or grid.get_tile_color(row-1, col+1) == self.enemy_color):
                lst.append([row-1,col+1])
        
        if row+1 <= grid.row:
            if grid.check_free(row+1, col) or grid.get_tile_color(row+1, col) == self.enemy_color:
                lst.append([row+1,col])
            if col-1 > 0 and (grid.check_free(row+1, col-1) or grid.get_tile_color(row+1, col-1) == self.enemy_color):
                lst.append([row+1,col-1])
            if col+1 <= grid.columns and (grid.check_free(row+1, col+1) or grid.get_tile_color(row+1, col+1) == self.enemy_color):
                lst.append([row+1,col+1])
                
        if col-1 > 0 and (grid.check_free(row, col-1) or grid.get_tile_color(row, col-1) == self.enemy_color):
            lst.append([row,col-1])
            
        if col+1 <= grid.columns and (grid.check_free(row, col+1) or grid.get_tile_color(row, col+1) == self.enemy_color):
            lst.append([row,col+1])
                
        return lst