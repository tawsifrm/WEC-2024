## 🌐 Dynamic World Generation Algorithm for Tile-Based Maps

### Overview
Welcome to the repository for our first-place project from the Waterloo Engineering Competition (WEC) 2024 Programming division. This project showcases a dynamic world generation algorithm designed to create engaging and interactive tile-based maps, an essential component in many popular video games.

#### Challenge and Design Requirements
In this project, the term "room" is used to indicate a space on the grid that will be used to generate a playable map for the game. The sizes of the rooms are classified as follows:

![image](https://github.com/user-attachments/assets/849c0114-6663-404f-8e3e-adf20e21c329)



The challenge is to fit a number of these rooms into a 10x10 grid area such that a player can travel from the Start tile to the Finish tile. Each room type has preset restrictions on how a player can enter/exit the room, indicated by specific entry/exit points. Rooms can only be connected if their respective entry/exit points align.

**Key Restrictions:**
- There must always be a Start room and a Finish room.
- Room generations must not exceed the boundaries of the 10x10 grid.
- There must be at least one valid path from the Start room to the Finish room.
- All generated rooms must be reachable.
- Rooms can only be considered connected if their entry/exit points match on the grid.

### Features
- **Random Tile-Based Map Generation**: Creates a diverse and complex environment using 1x1, 2x1, 2x2, and 3x3 room tiles.
- **Pathfinding**: Ensures a valid, non-looping path from Start to Finish.
- **UI Design**: Visual representation of the grid using Python's Turtle graphics library.
- **Error Checking**: Validates room placements and path generation to prevent invalid configurations.

### How It Works
The algorithm works as follows:

1. **Grid Initialization**: A 10x10 grid is initialized with empty spaces.
2. **Room Placement**: Rooms of various shapes and sizes are placed on the grid using the `place_room` function, which ensures no overlap and valid positioning.
3. **Pathfinding**: The `find_path` function uses Breadth-First Search (BFS) to find a valid path from the Start tile to the Finish tile.
4. **Connectivity Check**: The `all_rooms_connected` function ensures that all placed rooms are connected.
5. **Map Generation**: The `generate_map` function orchestrates the overall process, including room placement and pathfinding.
6. **Grid Drawing**: The `draw_grid` function uses Turtle graphics to visually represent the grid and the placed rooms.
7. **Title Drawing**: A creative title is randomly selected and displayed above the grid.

The following is one of infinitely many possible maps our algorithm can generate:

![image](https://github.com/user-attachments/assets/67624aea-5774-4cac-bc27-458e657a1550)


### Acknowledgements
Special thanks to my teammate, Abeer Das, and the organizers of WEC 2024 for providing this incredible opportunity.
