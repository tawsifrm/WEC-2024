import turtle
import random
from collections import deque
import time


# Size of the grid and the tiles
GRID_SIZE = 10
TILE_SIZE = 30

# Dictionary for room types, shapes, and exits
ROOM_TYPES = {
    '1x1': {'shape': [(0, 0)], 'color': 'yellow', 'label': 'A'},
    '2x1': {'shape': [(0, 0), (0, 1)], 'color': 'pink', 'label': 'B'},
    '1x2': {'shape': [(0, 0), (1, 0)], 'color': 'pink', 'label': 'G'},
    '2x2': {'shape': [(0, 0), (0, 1), (1, 0), (1, 1)], 'color': 'blue', 'label': 'C'},
    '3x3': {'shape': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 
            'color': 'orange', 'label': 'D'},
    'Heart-shape': {
        'shape': [(1, -1), (1, -2), (1, -3), (0, -2), (2, 0), (2, -1), (2, -2), (2, -3), (2, -4), (3, -1), (3, -3)],
        'color': 'purple', 'label': 'E'
    }
}

# Initialize grid
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to place a room on the grid
def place_room(grid, room, x, y):
    """
    Places a room on the grid at position (x, y).

    Args:
    - grid (list of lists): The grid to place the room on.
    - room (str): The type of room to place.
    - x (int): The starting x-coordinate of the room.
    - y (int): The starting y-coordinate of the room.
    """
    for dx, dy in ROOM_TYPES[room]['shape']:
        grid[x + dx][y + dy] = ROOM_TYPES[room]['label']

# Function to check if a room can be placed
def can_place_room(grid, room, x, y):
    """
    Checks if a room can be placed on the grid without overlap.

    Args:
    - grid (list of lists): The grid to check.
    - room (str): The type of room to place.
    - x (int): The starting x-coordinate of the room.
    - y (int): The starting y-coordinate of the room.

    Returns:
    - bool: True if the room can be placed, False otherwise.
    """
    for dx, dy in ROOM_TYPES[room]['shape']:
        if not (0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE) or grid[x + dx][y + dy] != ' ':
            return False
    return True

# Function to find a path from Start to Finish using BFS
def find_path(grid, start, finish):
    """
    Finds a path from Start to Finish using Breadth-First Search (BFS).

    Args:
    - grid (list of lists): The grid to search.
    - start (tuple): Coordinates (x, y) of the start position.
    - finish (tuple): Coordinates (x, y) of the finish position.

    Returns:
    - bool: True if a path exists, False otherwise.
    """
    queue = deque([start])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == finish:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in visited and grid[nx][ny] != ' ':
                queue.append((nx, ny))
                visited.add((nx, ny))
    return False

# Function to ensure all rooms are connected
def all_rooms_connected(grid):
    """
    Checks if all rooms on the grid are connected.

    Args:
    - grid (list of lists): The grid to check.

    Returns:
    - bool: True if all rooms are connected, False otherwise.
    """
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = None

    # Find the first non-empty cell to start the BFS
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != ' ':
                queue = deque([(i, j)])
                visited.add((i, j))
                break
        if queue:
            break

    if not queue:
        return False

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in visited and grid[nx][ny] != ' ':
                queue.append((nx, ny))
                visited.add((nx, ny))

    # Check if all non-empty cells are visited
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != ' ' and (i, j) not in visited:
                return False
    return True

# Main algorithm to generate the map
def generate_map(grid):
    """
    Generates a map grid with rooms and ensures connectivity.

    Args:
    - grid (list of lists): The grid to populate.
    """

    # Define corner positions
    corners = [(0, 0), (0, GRID_SIZE - 1), (GRID_SIZE - 1, 0), (GRID_SIZE - 1, GRID_SIZE - 1)]
    
    # Loop until a valid map is generated
    while True:
        # Randomly select start and finish positions from corners
        start = random.choice(corners)
        finish = random.choice([corner for corner in corners if corner != start])
        start_x, start_y = start
        finish_x, finish_y = finish

        # Clear the grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                grid[i][j] = ' '

        grid[start_x][start_y] = 'S'
        grid[finish_x][finish_y] = 'F'

        # Try to place rooms
        for _ in range(100):  # Try placing rooms within a reasonable limit
            room_type = random.choice(list(ROOM_TYPES.keys()))
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if can_place_room(grid, room_type, x, y):
                place_room(grid, room_type, x, y)

        # Ensure there's a valid path from Start to Finish and all rooms are connected
        if find_path(grid, start, finish) and all_rooms_connected(grid):
            print("Valid path found and all rooms are connected.")
            break
        else:
            print("No valid path found or rooms are not connected. Regenerating map...")


# Function to draw the grid using Turtle
def draw_grid(grid):
    """
    Draws the grid on the screen using Turtle graphics.

    Args:
    - grid (list of lists): The grid to draw.
    """
    turtle.speed(0)
    turtle.tracer(0, 0)  
    turtle.penup()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x, y = j * TILE_SIZE, -i * TILE_SIZE
            turtle.goto(x, y)
            turtle.pendown()
            if grid[i][j] == ' ':
                turtle.fillcolor('white')
            elif grid[i][j] == 'S':
                turtle.fillcolor('green')
            elif grid[i][j] == 'F':
                turtle.fillcolor('red')
            else:
                for room, details in ROOM_TYPES.items():
                    if grid[i][j] == details['label']:
                        turtle.fillcolor(details['color'])
                        break
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(TILE_SIZE)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
    turtle.update()  # Update the screen

# List of creative titles
TITLES = [
    "Mystery Dungeon", "Enchanted Labyrinth", "Maze of Wonders", "Forgotten Fortress",
    "Secret Passageways", "Hidden Chambers", "The Great Escape", "Puzzle Palace",
    "Cryptic Corridors", "Lost in the Grid", "Chamber of Secrets", "The Final Frontier",
    "The Forbidden City", "The Haunted Maze", "The Cursed Catacombs", "The Dark Domain",
    "The Phantom Zone", "The Twilight Zone", "The Enigma", "The Mind Bender"
]

# Function to draw the title
def draw_title(title):
    """
    Displays the generated map grid using Turtle graphics.

    Args:
    - grid (list of lists): The grid to display.
    """
    turtle.penup()
    turtle.goto(GRID_SIZE * TILE_SIZE / 2, TILE_SIZE / 2)
    turtle.color('black')
    turtle.write(title, align="center", font=("Arial", 16, "bold"))
    turtle.hideturtle()

start_time = time.time()

# Generate the map
generate_map(grid)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Runtime: {elapsed_time:.6f} seconds")

# Setup turtle display
turtle.setup(GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE)
turtle.setworldcoordinates(0, -GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE, 0)
turtle.hideturtle()

# Draw the title
random_title = random.choice(TITLES)
draw_title(random_title)

# Draw the grid 
draw_grid(grid)
turtle.done()
