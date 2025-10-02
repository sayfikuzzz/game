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
        pass

    def update(self):
        """Обновляет поле по правилам игры Жизнь (с учётом замкнутости)"""
        pass

    def count_neighbors(self, x, y):
        """Считает соседей с учётом замкнутости торoidal"""
        pass