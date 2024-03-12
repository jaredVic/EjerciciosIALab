#Esquivel Victoriano Alvaro Jared

import time
import heapq


def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_maze(maze, start, end):
    # 0 = open path, 1 = wall, S = start, E = end
    rows, cols = len(maze), len(maze[0])
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return True, path[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + dx, current[1] + dy
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '1':
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + \
                        heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return False, []


if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    # maze = [
    #     ['1', '1', '1', '1', '1'],
    #     ['S', '0', '1', '0', '1'],
    #     ['1', '0', '1', '0', '1'],
    #     ['1', '0', '0', '0', 'E'],
    #     ['1', '1', '1', '1', '1']
    # ]
    # start = (1, 0)
    # end = (3, 5)
    
    #maze = [
    #     ['1', '1', '1', '1', '1', '1', '1', '1'],
    #     ['S', '0', '0', '1', '0', '1', '0', '1'],
    #     ['1', '1', '0', '1', '0', '1', '0', '1'],
    #     ['1', '0', '0', '0', '0', '1', '0', '1'],
    #     ['1', '0', '1', '1', '1', '1', '0', '1'],
    #     ['1', '0', '1', '0', '0', '0', '0', '1'],
    #     ['1', '0', '1', '1', '1', '1', '0', '1'],
    #     ['1', '0', '0', '0', '0', '0', '0', 'E']
    # ]
    # start = (1, 0)
    # end = (7, 7)
    
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '0', '0', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '1', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '0', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '0', '0', '1', 'E', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]
    start = (1, 0)
    end = (8, 8)

    start_time = time.time()
    solved, path = solve_maze(maze, start, end)
    end_time = time.time()

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

    print("Time taken to solve the maze: {:.6f} seconds".format(
        end_time - start_time))
