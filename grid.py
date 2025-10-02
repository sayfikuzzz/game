import numpy as np
from numba import jit


@jit(nopython=True)
def count_neighbors_numba(grid, x, y, rows, cols):
    """Считает соседей с учётом замкнутости (тороидальное поле)"""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            # Тороидальные координаты
            nx = (x + i) % rows
            ny = (y + j) % cols
            count += grid[nx, ny]
    return count


@jit(nopython=True)
def update_grid_numba(grid, rows, cols):
    """Обновляет поле по правилам игры Жизнь (ускоренная версия)"""
    new_grid = np.zeros((rows, cols), dtype=np.int32)

    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors_numba(grid, x, y, rows, cols)

            # Правила игры Жизнь
            if grid[x, y] == 1:  # Живая клетка
                if neighbors == 2 or neighbors == 3:
                    new_grid[x, y] = 1
                else:
                    new_grid[x, y] = 0
            else:  # Мёртвая клетка
                if neighbors == 3:
                    new_grid[x, y] = 1
                else:
                    new_grid[x, y] = 0

    return new_grid


class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.grid = np.zeros((self.rows, self.cols), dtype=np.int32)

    def random_fill(self, percentage):
        """Заполняет поле случайными значениями с заданным процентом живых клеток"""
        total_cells = self.rows * self.cols
        alive_cells = int(total_cells * percentage / 100)

        # Создаем массив с нужным количеством живых клеток
        flat_grid = np.zeros(total_cells, dtype=np.int32)
        flat_grid[:alive_cells] = 1
        np.random.shuffle(flat_grid)

        self.grid = flat_grid.reshape((self.rows, self.cols))

    def count_neighbors(self, x, y):
        """Считает соседей (обертка для numba функции)"""
        return count_neighbors_numba(self.grid, x, y, self.rows, self.cols)

    def update(self):
        """Обновляет поле по правилам игры Жизнь"""
        self.grid = update_grid_numba(self.grid, self.rows, self.cols)
        return self.grid

    def get_percentage(self):
        """Возвращает текущий процент заполненности"""
        alive_cells = np.sum(self.grid)
        total_cells = self.rows * self.cols
        return (alive_cells / total_cells) * 100 if total_cells > 0 else 0