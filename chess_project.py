import arcade
from grid import Grid
from pawn import Pawn
from testpiece import TPiece
from knight import Knight
from king import King
from rook import Rook
from bishop import Bishop
from queen import Queen

ROW_COUNT = 8
COLUMN_COUNT = 8

WIDTH = 60
HEIGHT = 60

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        self.init_g = Grid()
        self.grid = self.init_g.array

        arcade.set_background_color(arcade.color.BLACK)
        
    def setup(self):
        self.init_g = Grid()
        self.grid = self.init_g.array
        
        rooklst = [[1,1,"white"],[1,8,"white"],[8,1,"black"],[8,8,"black"]]
        knightlst = [[1,2,"white"],[1,7,"white"],[8,2,"black"],[8,7,"black"]]
        bishoplst = [[1,3,"white"],[1,6,"white"],[8,3,"black"],[8,6,"black"]]
        
        [self.init_g.additem(Pawn(2,i,"white")) for i in range(1,9)]
        [self.init_g.additem(Pawn(7,i,"black")) for i in range(1,9)]
        
        for i in rooklst:
            self.init_g.additem(Rook(i[0],i[1],i[2]))

        for i in knightlst:
            self.init_g.additem(Knight(i[0],i[1],i[2]))
            
        for i in bishoplst:
            self.init_g.additem(Bishop(i[0],i[1],i[2]))
            
        self.init_g.additem(Queen(1,4,"white"))
        self.init_g.additem(Queen(8,4,"black"))
        self.init_g.additem(King(1,5,"white"))
        self.init_g.additem(King(8,5,"black"))

    def on_draw(self):

        self.clear()
        i = 0
        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                
                
                if i == 0:
                    color = arcade.color.ANTIQUE_BRASS
                    i=1
                    if column == 7:
                        i=0
                        
                elif i == 1:
                    color = arcade.color.COCONUT
                    i=0
                    if column == 7:
                        i=1
                    
                # if self.grid[row][column][0] != None:
                #     color = arcade.color.YELLOW
                    
                if self.grid[row][column][2] == 1:
                    color = arcade.color.GREEN
                    
                elif self.grid[row][column][2] == 2:
                    color = arcade.color.RED
                
                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                
                if self.grid[row][column][0] != None:
                    if self.grid[row][column][0].color == True:
                        arcade.draw_text(self.grid[row][column][0].name , x-7, y-7, arcade.color.WHITE,15)
                    else:
                        arcade.draw_text(self.grid[row][column][0].name , x-7, y-7, arcade.color.BLACK,15)
                    
    def on_key_press(self, symbol: int, modifiers: int):
        if modifiers == 2:
            if symbol == 114:
                self.setup()
                             

    def on_mouse_press(self, x, y, button, modifiers):
    
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))
        
        self.init_g.clicked_tile(row,column)
              
        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
        # if self.grid[row][column][2] == 0:
            # self.grid[row][column][2] = 1
        # else:
        #     self.grid[row][column][2] = 0


def main():

    g = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    g.setup()
    arcade.run()


if __name__ == "__main__":
    main()
    p = Pawn(2,2,"white")
    ep = Pawn(3,3,"black")
    g = Grid()

    g.additem(p)
    g.additem(ep)