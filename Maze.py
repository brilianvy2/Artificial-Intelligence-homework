from collections import deque

# Maze represented as a 2D grid
maze = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', 'S', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
    ['*', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', '*'],
    ['*', ' ', '*', ' ', '*', 'G', ' ', ' ', '*', ' ', '*'],
    ['*', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', '*'],
    ['*', ' ', '*', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', ' ', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]

def is_valid_move(x, y):
    # Check if the move is within the bounds of the maze
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '*'

def bfs_maze_solver(maze):
    start = (1, 1)  # Starting position
    goal = None

    # Find the coordinates of the 'G' (goal) cell
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'G':
                goal = (i, j)

    if goal is None:
        print("Goal not found in the maze.")
        return

    # Define possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])  # Queue of positions and the path taken

    visited = set()  # Set to keep track of visited nodes

    while queue:
        (x, y), path = queue.popleft()

        # If we reached the goal, return the path
        if (x, y) == goal:
            return path

        # Check each possible move
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                new_path = path + [(new_x, new_y)]
                queue.append(((new_x, new_y), new_path))

    return None  # No path found

# Call the function to solve the maze
solution = bfs_maze_solver(maze)

if solution:
    print("Solution found:")
    for x, y in solution:
        if maze[x][y] == 'G':
            break
        maze[x][y] = 'X'  # Mark the path with 'X'
    for row in maze:
        print(row)
else:
    print("No solution found.")
