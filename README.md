# Pygame
CSF101,CAP 2

#cap 3
TetrisTest Class
setUp Method:

Initializes Pygame using pygame.init().
test_check_lost Method:

Tests the check_lost function.
Verifies that the function correctly returns True when a Tetris piece is at the top of the grid.
test_main Method:

Tests the main function.
Creates a Pygame window with dimensions (800, 700) and runs the main game loop.
test_main_menu Method:

Tests the main_menu function.
Creates a Pygame window with dimensions (800, 700) and runs the main menu loop.
test_main_menu_quit Method:

Tests if the main_menu function can be exited without errors.
Simulates a quit event by posting a pygame.QUIT event.
test_main_key_events Method:

Tests if key events in the main game loop run without errors.
Simulates left and right arrow key events.
draw_grid Function
Parameters:

surface: Pygame surface to draw on.
grid: 2D grid representing the game grid.
top_left_x: x-coordinate of the top-left corner of the grid.
top_left_y: y-coordinate of the top-left corner of the grid.
block_size: Size of each block in pixels.
play_width: Width of the game grid in blocks.
play_height: Height of the game grid in blocks.
Functionality:

Draws grid lines on the provided surface based on the grid dimensions and block size.
TestDrawGrid Class
test_draw_grid Method:
Tests the draw_grid function using the unittest.mock.patch decorator.
Creates a mock surface and a mock grid.
Calls the function and checks that pygame.draw.line is called the correct number of times.
Piece Class
Attributes:

x: x-coordinate of the piece.
y: y-coordinate of the piece.
shape: Shape of the piece.
init Method:

Initializes a piece with the given x, y, and shape.
get_shape Function
Parameters:

shapes: List of shapes to choose from.
Functionality:

Returns a new Piece instance with a fixed x-coordinate (5), y-coordinate (0), and a randomly chosen shape from the provided list.
TestGetShape Class
test_get_shape Method:
Tests the get_shape function using the unittest.mock.patch decorator.
Defines shapes, calls the function, and checks that random.choice is called with the correct argument.
Verifies that the result is an instance of the Piece class with the expected attributes.
Running the Tests
The unittest.main() block runs all the defined tests when the script is executed.
