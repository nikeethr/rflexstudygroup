import a2
import unittest
import logging

maze_path = 'maze.txt'
log_path = 'debug.log'

class TestRateRace(unittest.TestCase):
    def setUp(self):
        maze_str = []
        rat_1 = None
        rat_2 = None
        maze = None

        with open(maze_path, 'r') as m:
            for line in m:
                maze_str.append([ch for ch in line.strip()])

        for r in range(len(maze_str)):
            for c in range(len(maze_str[r])):
                if rat_1 == None and maze_str[r][c] == a2.RAT_1_CHAR:
                    rat_1 = a2.Rat(a2.RAT_1_CHAR,r,c)
                    maze_str[r][c] = a2.HALL
                elif rat_2 == None and maze_str[r][c] == a2.RAT_2_CHAR:
                    rat_2 = a2.Rat(a2.RAT_2_CHAR,r,c)
                    maze_str[r][c] = a2.HALL

        if rat_1 is not None and rat_2 is not None:
            maze = a2.Maze(maze_str, rat_1, rat_2)

        self.maze = maze
        self.log = logging.getLogger("TestMaze")

    def tearDown(self):
        self.maze = None

    def test_load_maze(self):
        self.log.info('test_load_maze')
        self.log.info(str(self.maze))
        self.assertEqual(self.maze.num_sprouts_left, 3)

        tests = [(self.maze.num_sprouts_left, 3),
                 (self.maze.rat_1.symbol, 'J'),
                 ((self.maze.rat_1.row, self.maze.rat_1.col), (1, 1)),
                 (self.maze.rat_2.symbol, 'P'),
                 ((self.maze.rat_2.row, self.maze.rat_2.col), (1, 4))]

        for test in tests:
            self.assertEqual(test[0], test[1])

    def test_move_rat_1_on_rat_2_and_move_away(self):
        self.log.info('test_move_rat_1_on_rat_2_and_move_away')
        self.maze.move(self.maze.rat_1, 0, 3)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[1][4] == 'J' or self.maze.maze[1][4] == 'P')

        self.maze.move(self.maze.rat_1, 0, 1)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[1][4] == 'P' and self.maze.maze[1][5] == 'J')

    def test_move_rat_1_on_sprouts(self):
        self.log.info('test_move_rat_1_on_sprouts')
        self.maze.move(self.maze.rat_1, 2, 2)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[3][3] == 'J'
            and self.maze.num_sprouts_left == 2
            and self.maze.rat_1.num_sprouts_eaten == 1)

        self.maze.move(self.maze.rat_1, 1, 1)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[3][3] == a2.HALL
            and self.maze.maze[4][4] == 'J'
            and self.maze.num_sprouts_left == 1
            and self.maze.rat_1.num_sprouts_eaten == 2)

        self.maze.move(self.maze.rat_1, 0, -3)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[4][4] == a2.HALL
            and self.maze.maze[4][1] == 'J'
            and self.maze.num_sprouts_left == 0
            and self.maze.rat_1.num_sprouts_eaten == 3)

    def test_move_rat_1_onto_wall(self):
        self.log.info('test_move_rat_1_onto_wall')
        self.maze.move(self.maze.rat_1, -1, -1)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[1][1] == 'J' and self.maze.maze[0][0] == '#')

    def test_move_rat_1_onto_hall(self):
        self.log.info('test_move_rat_1_onto_hall')
        self.maze.move(self.maze.rat_1, 1, 0)
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[1][1] == '.' and self.maze.maze[2][1] == 'J')

    def test_is_wall(self):
        self.log.info('test_is_wall')
        self.assertTrue(self.maze.is_wall(0,0) and not self.maze.is_wall(1,1))

    def test_refresh_rats_pos(self):
        self.log.info('test_refresh_rats_pos')
        self.maze.maze[1][1] = a2.HALL
        self.maze.maze[1][4] = a2.HALL
        self.log.info(str(self.maze))
        self.maze.refresh_rats_pos()
        self.log.info(str(self.maze))
        self.assertTrue(self.maze.maze[1][1] == 'J' and self.maze.maze[1][4] == 'P')

if __name__ == "__main__":
    fh = logging.FileHandler(log_path)
    logger = logging.getLogger("TestMaze")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    unittest.main(exit=False)
