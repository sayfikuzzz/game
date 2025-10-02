import numpy as np


class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.grid = np.zeros((self.rows, self.cols), dtype=int)

    def random_fill(self, percentage):
        """Заполняет поле случайными значениями с заданным процентом живых клеток"""
        total_cells = self.rows * self.cols
        alive_cells = int(total_cells * percentage / 100)

        # Создаем массив с нужным количеством живых клеток
        flat_grid = np.zeros(total_cells, dtype=int)
        flat_grid[:alive_cells] = 1
        np.random.shuffle(flat_grid)

        self.grid = flat_grid.reshape((self.rows, self.cols))

    def count_neighbors(self, x, y):
        """Считает соседей с учётом замкнутости (тороидальное поле)"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                # Тороидальные координаты
                nx = (x + i) % self.rows
                ny = (y + j) % self.cols
                count += self.grid[nx, ny]
        return count

    def update(self):
        """Обновляет поле по правилам игры Жизнь"""
        new_grid = np.zeros((self.rows, self.cols), dtype=int)

        for x in range(self.rows):
            for y in range(self.cols):
                neighbors = self.count_neighbors(x, y)

                # Правила игры Жизнь
                if self.grid[x, y] == 1:  # Живая клетка
                    if neighbors == 2 or neighbors == 3:
                        new_grid[x, y] = 1
                    else:
                        new_grid[x, y] = 0
                else:  # Мёртвая клетка
                    if neighbors == 3:
                        new_grid[x, y] = 1
                    else:
                        new_grid[x, y] = 0

        self.grid = new_grid
        return self.grid