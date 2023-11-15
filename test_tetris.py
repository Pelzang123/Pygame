import unittest
import random
import pygame
from unittest.mock import patch, MagicMock
from tetris import   main, main_menu, check_lost, draw_grid

class TetrisTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
    
    def test_check_lost(self):
        # Test when a piece is at the top of the grid
        positions = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertTrue(check_lost(positions))

    
    def test_main(self):
        # This is a simple test to check if the main function runs without errors
          win = pygame.display.set_mode((800, 700))
          main(win)

    def test_main_menu(self):
        # This is a simple test to check if the main menu function runs without errors
           win = pygame.display.set_mode((800, 700))
           main_menu(win)

    def test_main_menu_quit(self):
        # Test if the main menu function can be quit without errors
           win = pygame.display.set_mode((800, 700))
           pygame.event.post(pygame.event.Event(pygame.QUIT))  # Simulate quitting
           main_menu(win)  # Should exit without errors
    
    def test_main_key_events(self):
        # Test if key events in the main game loop run without errors
            win = pygame.display.set_mode((800, 700))
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT}))  # Simulate left arrow key
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))  # Simulate right arrow key
            main(win)  # Should exit without errors

def draw_grid(surface, grid, top_left_x, top_left_y, block_size, play_width, play_height):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))

class TestDrawGrid(unittest.TestCase):

    @patch('pygame.draw.line')
    def test_draw_grid(self, mock_draw_line):
        # Create a mock surface
        surface = MagicMock()

        # Create a mock grid
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Define the constants used in the function
        top_left_x = 10
        top_left_y = 20
        block_size = 10
        play_width = 30
        play_height = 30

        # Call the function
        draw_grid(surface, grid, top_left_x, top_left_y, block_size, play_width, play_height)

        # Check that the pygame.draw.line() function was called the correct number of times
        expected_call_count = 2 * (len(grid) + len(grid[0]))
        self.assertEqual(mock_draw_line.call_count, expected_call_count)
            

class Piece:
   def __init__(self, x, y, shape):
       self.x = x
       self.y = y
       self.shape = shape

def get_shape(shapes):
   return Piece(5, 0, random.choice(shapes))

class TestGetShape(unittest.TestCase):

   @patch('random.choice', return_value='mocked_shape')
   def test_get_shape(self, mock_random_choice):
       # Define the shapes
       shapes = ['shape1', 'shape2', 'shape3']

       # Call get_shape
       result = get_shape(shapes)

       # Check that random.choice was called with the correct argument
       mock_random_choice.assert_called_once_with(shapes)

       # Check that the result is an instance of the Piece class
       self.assertIsInstance(result, Piece)

       # Check that the attributes of the Piece instance are set correctly
       self.assertEqual(result.x, 5)
       self.assertEqual(result.y, 0)
       self.assertEqual(result.shape, 'mocked_shape')


if __name__ == '__main__':
    unittest.main()
