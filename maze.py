import copy
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def up(maze, pt):
    i, j = pt
    if i - 1 >= 0 and maze[i - 1][j] == 0:
        return i - 1, j
    return []


def down(maze, pt):
    i, j = pt
    if i + 1 < len(maze) and maze[i + 1][j] == 0:
        return i + 1, j
    return []


def left(maze, pt):
    i, j = pt
    if j - 1 >= 0 and maze[i][j - 1] == 0:
        return i, j - 1
    return []


def right(maze, pt):
    i, j = pt
    if j + 1 < len(maze[i]) and maze[i][j + 1] == 0:
        return i, j + 1
    return []


def find_neighbors(maze, pt):
    neighbors = []
    left_n = left(maze, pt)
    right_n = right(maze, pt)
    up_n = up(maze, pt)
    down_n = down(maze, pt)

    if len(left_n) != 0:
        neighbors.append(left_n)

    if len(right_n) != 0:
        neighbors.append(right_n)
    if len(up_n) != 0:
        neighbors.append(up_n)
    if len(down_n) != 0:
        neighbors.append(down_n)

    return neighbors


def depth_first_search(maze, start, end):
    if start == end:
        return [start]

    neighbors = [start]
    explored = []
    parents = {}

    while len(neighbors) > 0:
        if neighbors[-1] == end:
            path = [end]
            child = end

            while True:
                parent = parents.get(child)
                path.append(parent)
                child = parent

                if parent == start:
                    break

            return path[::-1], len(explored)

        new_neighbors = find_neighbors(maze, neighbors[-1])
        explored.append(neighbors[-1])
        neighbors.pop()

        for new_neighbor in new_neighbors:
            if new_neighbor not in explored and new_neighbor not in neighbors:
                parents[new_neighbor] = explored[-1]
                neighbors.append(new_neighbor)

    else:
        return


def breadth_first_search(maze, start, end):
    if start == end:
        return [start]

    neighbors = [start]
    explored = []
    parents = {}

    while len(neighbors) > 0:
        if neighbors[0] == end:
            path = [end]
            child = end

            while True:
                parent = parents.get(child)
                path.append(parent)
                child = parent

                if parent == start:
                    break

            return path[::-1], len(explored)

        new_neighbors = find_neighbors(maze, neighbors[0])
        explored.append(neighbors[0])
        neighbors.pop(0)

        for new_neighbor in new_neighbors:
            if new_neighbor not in explored and new_neighbor not in neighbors:
                parents[new_neighbor] = explored[-1]
                neighbors.append(new_neighbor)

    else:
        return


def find_way(maze, start, end, search,title_name="Maze Solution"):
  
    path, steps = search(maze, start, end)
    result_maze = copy.deepcopy(maze)

    if path:
        for position in path:
            i, j = position
            result_maze[i][j] = '*'

        rows = len(result_maze)
        cols = len(result_maze[0])

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.set_xlim(0, cols)
        ax.set_ylim(rows, 0)
        ax.set_aspect('equal')
        ax.axis('off')

        for r in range(rows):
            for c in range(cols):
                val = result_maze[r][c]
                if (r, c) == start:
                    color = (0.16, 0.67, 0.38)
                elif (r, c) == end:
                    color = (0.12, 0.56, 1.0)
                elif val == 1:
                    color = (0.12, 0.12, 0.12)
                elif val == '*':
                    color = (0.98, 0.55, 0.20)
                else:
                    color = (0.96, 0.96, 0.96)

                rect = Rectangle(
                    (c, r),
                    1,
                    1,
                    facecolor=color,
                    edgecolor=(0.45, 0.45, 0.45),
                    linewidth=1.2,
                )
                ax.add_patch(rect)

        for r, c in [start, end]:
            label = 'S' if (r, c) == start else 'E'
            ax.text(c + 0.5, r + 0.5, label, ha='center', va='center', fontsize=12, fontweight='bold', color='white')

        plt.title(f"{title_name} (Nodes Processed: {steps})", fontsize=12)
        plt.tight_layout()
        plt.show()
        return

    print("Can't find a path...")

start = (1, 0)
end = (27, 29)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

find_way(maze,start,end,depth_first_search)
# find_way(maze,start,end,breadth_first_search)