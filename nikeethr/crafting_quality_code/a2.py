# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, int, int) -> NoneType
        Initialises the rat with it's character representation and it's position in the maze. Sets
        the number of sprouts it has eaten to 0.
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType
        Updates location of the rat.

        >>> rat = Rat('J',2,3)
        >>> rat.set_location(3,4)
        >>> rat.row
        3
        >>> rat.col
        4
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat, int, int) -> NoneType
        Updates the number of sprouts eaten by the rat so far.

        >>> rat = Rat('J',2,3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str
        Returns string of the form
        'symbol at (row, col) ate num_sprouts_eaten sprouts.'

        >>> rat = Rat('J',2,3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat
        'J at (2, 3) ate 2 sprouts.'
        """
        return '{} at ({}, {}) ate {} sprouts.'.format(
                self.symbol,
                self.row,
                self.col,
                self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        Initialises maze with the input maze string and the positions two rats.
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        self.refresh_rats_pos()

        for r in range(len(maze)):
            for c in range(len(maze[r])):
                if maze[r][c] == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
        Returns true if there is a wall in position (row, col) of the maze.
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str
        Returns the character at the position (row, col) of the maze.
        """
        return self.maze[row][col]

    def move(self, rat, vrt, hrz):
        """ (Maze, Rat, int, int) -> bool
        Moves the rat to the specified position if it's not a wall.
        If the rat moves onto a sprout, it will be eaten.

        Returns true iff there is no wall in the way
        """
        row = rat.row + vrt
        col = rat.col + hrz

        if (not self.is_wall(row, col) and 
                (rat.symbol == self.rat_1.symbol or
                 rat.symbol == self.rat_2.symbol)):
            self.maze[rat.row][rat.col] = HALL
            rat.set_location(row, col)

            if self.get_character(row, col) == SPROUT and self.num_sprouts_left > 0:
                rat.eat_sprout()
                self.num_sprouts_left -= 1

            self.refresh_rats_pos()
            return True
        return False

    def refresh_rats_pos(self):
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

    def __str__(self):
        """ (Maze) -> str
        Returns the status of the maze.
        """
        maze_map = '\n'.join([''.join(self.maze[r]) for r in range(len(self.maze))])
        scores = str(self.rat_1) + '\n' + str(self.rat_2)
        return maze_map + '\n' + scores
