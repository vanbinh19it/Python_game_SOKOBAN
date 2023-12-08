def __init__(self, grid):
    self.grid = grid
    self.player_position = None
    self.target_count = 0
    self.finished = False
    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            if self.grid[i][j] == "P":
                self.player_position = (i, j)
            elif self.grid[i][j] == "T":
                self.target_count += 1


def is_valid_move(self, position):
    x, y = position
    if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[x]):
        return False
    elif self.grid[x][y] in ["#", "B"]:
        return False
    return True


def move(self, direction):
    x, y = self.player_position
    dx, dy = direction
    new_position = (x + dx, y + dy)
    if not self.is_valid_move(new_position):
        return
    new_x, new_y = new_position
    old_value = self.grid[x][y]
    new_value = self.grid[new_x][new_y]
    if new_value == "B":
        new_box_position = (new_x + dx, new_y + dy)
        if not self.is_valid_move(new_box_position):
            return
        new_box_x, new_box_y = new_box_position
        self.grid[new_box_x][new_box_y] = "B"
        self.grid[new_x][new_y] = old_value
    self.grid[x][y] = "."
    self.grid[new_x][new_y] = "P"
    self.player_position = new_position
    if old_value == "T":
        self.target_count -= 1
        if self.target_count == 0:
            self.finished = True


def undo_move(self, direction):
    dx, dy = direction
    reversed_direction = (-dx, -dy)
    self.move(reversed_direction)


def solve(self):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    self.backtrack(moves, [])


def backtrack(self, moves, path):
    if self.finished:
        print(path)
        return
    for move in moves:
        self.move(move)
        if self.player_position not in path:
            path.append(self.player_position)
            self.backtrack(moves, path)
            path.pop()
        self.undo_move(move)
