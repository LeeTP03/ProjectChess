from grid import Grid

class Bishop():
    
    def __init__(self, x, y, color) -> None:
        self.name = "B"
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
        
        for i in range(1,grid.row):
            if row + i > grid.row or col + i > grid.row:
                break
            
            if grid.get_tile_color(row+i, col+i) == self.enemy_color:
                lst.append([row+i, col+i])
                break
            
            elif grid.check_free(row+i, col+i) == True:
                lst.append([row+i,col+i])
                
            else:
                break
        
        for i in range(1,grid.row):
            if row - i <= 0 or col - i <= 0:
                break
            
            if grid.get_tile_color(row-i, col-i) == self.enemy_color:
                lst.append([row-i, col-i])
                break
    
            elif grid.check_free(row-i, col-i) == True:
                lst.append([row-i,col-i])
                
            else:
                break
        
        
        for i in range(1,grid.row):
            if row - i <= 0 or col + i > grid.row:
                break
            
            if grid.get_tile_color(row-i, col+i) == self.enemy_color:
                lst.append([row-i, col+i])
                break
            
            elif grid.check_free(row-i, col+i) == True:
                lst.append([row-i,col+i])
            
            else:
                break
        
        for i in range(1,grid.row):
            if row + i > grid.row or col - i <= 0:
                break
            
            if grid.get_tile_color(row+i, col-i) == self.enemy_color:
                lst.append([row+i, col-i])
                break
            
            elif grid.check_free(row+i, col-i) == True:
                lst.append([row+i,col-i])
            
            else:
                break
        
        print(lst, len(lst))
        return lst
        