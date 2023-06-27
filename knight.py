from grid import Grid

class Knight():
    
    def __init__(self, x, y, color) -> None:
        self.name = "k"
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
        row = self.position[0]
        col = self.position[1]
        
        if row + 2 <= grid.row:
            if col + 1 <= grid.columns and (grid.get_tile_color(row+2, col+1) == self.enemy_color or grid.check_free(row+2, col+1)):
                lst.append([row+2,col+1])
            if col - 1 > 0 and (grid.get_tile_color(row+2, col-1) == self.enemy_color or grid.check_free(row+2, col-1)):
                lst.append([row+2,col-1])
        
        if row - 2 > 0:
            if col + 1 <= grid.columns and (grid.get_tile_color(row-2, col+1) == self.enemy_color or grid.check_free(row-2, col+1)):
                lst.append([row-2,col+1])
            if col - 1 > 0 and (grid.get_tile_color(row-2, col-1) == self.enemy_color or grid.check_free(row-2, col-1)):
                lst.append([row-2,col-1])
        
        if col + 2 <= grid.row:
            if row + 1 <= grid.columns and (grid.get_tile_color(row+1, col+2) == self.enemy_color or grid.check_free(row+1, col+2)):
                lst.append([row+1,col+2])
            if row - 1 > 0 and (grid.get_tile_color(row-1, col+2) == self.enemy_color or grid.check_free(row-1, col+2)):
                lst.append([row-1,col+2])
        
        if col - 2 > 0:
            if row + 1 <= grid.columns and (grid.get_tile_color(row+1, col-2) == self.enemy_color or grid.check_free(row+1, col-2)):
                lst.append([row+1,col-2])
            if row - 1 > 0 and (grid.get_tile_color(row-1, col-2) == self.enemy_color or grid.check_free(row-1, col-2)):
                lst.append([row-1,col-2])
        print(lst)
        return lst
                