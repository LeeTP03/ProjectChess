from pawn import Pawn
from king import King
from queen import Queen

class Grid():
    
    def __init__(self) -> None:
        self.row = 8
        self.columns = 8
        self.array = []
        self.last_clicked = [0,0,[None,None,0]]
        
        for i in range(self.row):
            l = []
            for j in range(self.columns):
                l.append([None,None,0])
            self.array.append(l)
                
    def check_free(self, x, y):
        if x < 0 or y < 0 or y > 8 or x > 8:
            return None
        
        if isinstance(self.array[x-1][y-1][0],King):
            print("yes")
            return False
        
        if self.array[x-1][y-1][0] == None:
            return True
        
        else:
            return False
    
    def get_tile_color(self, x, y):
        if isinstance(self.array[x-1][y-1][0],King):
            return None
        
        return self.array[x-1][y-1][1]
    
    def additem(self,item):
        self.array[item.position[0]-1][item.position[1]-1] = [item, item.color, 0]
    
    def clear_grid(self, number = False):
        if number == False:
            for i in range(self.row):
                for j in range(self.columns):
                    self.array[i][j][2] = 0
        
        elif number == 1:
            for i in range(self.row):
                for j in range(self.columns):
                    if self.array[i][j][2] == 1:
                        self.array[i][j][2] = 0
                         
    def print_grid(self):
        for i in self.array:
            print(i)
                    
    def clicked_tile(self,x,y):
        self.clear_grid(1)
        print(self.array[x][y])
        
        if self.array[x][y][2] == 2:
            self.last_clicked[2][0].set_position(x+1,y+1)
            self.additem(self.last_clicked[2][0])
            self.array[self.last_clicked[0]][self.last_clicked[1]] = [None,None,0]
            self.clear_grid()

            if (x == 7 or x == 0) and isinstance(self.last_clicked[2][0],Pawn):
                pawn_asc = self.last_clicked
                print(pawn_asc)
                # userint = input("what to change to?")
                # if userint == "q":
                if x == 7:
                    self.array[x][y] = [(Queen(x+1, y+1, "white")), True, 0]
                if x == 0:
                    self.array[x][y] = [(Queen(x+1, y+1, "black")), False, 0]
            return []
        
        if x != self.last_clicked[0] or y != self.last_clicked[1]:
            self.clear_grid()
            
        if self.array[x][y][0] == None:
            self.clear_grid()
            return []

        self.last_clicked = [x,y,self.array[x][y]]
        self.last_clicked[2][2] = 0
        self.array[x][y][2] = 1
        possible = self.array[x][y][0].possible_move(self)  

        for i,j in possible:           
            if self.array[i-1][j-1][2] == 2:
                self.array[i-1][j-1][2] = 0
            else:
                self.array[i-1][j-1][2] = 2