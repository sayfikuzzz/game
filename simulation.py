from grid import Grid
from constants import DEFAULT_CELL_SIZE
import pygame
class Simulation:
    def __init__(self, width, height, percentage):
        self.grid = Grid(width, height, DEFAULT_CELL_SIZE)
        self.percentage = percentage
        self.paused = False
        self.fps_limited = True
        self.generation = 0
        self.clock = pygame.time.Clock()

    def run(self):
        """Основной цикл симуляции"""
        pass

    def handle_events(self):
        """Обрабатывает события во время симуляции"""
        # Кнопки: Пауза, Перезапуск, Возврат в меню, Переключение FPS
        pass

    def draw(self):
        """Отрисовывает поле и интерфейс"""
        # Поле клеточек
        # Размер поля
        # Процент заполненности
        # FPS/обновления в секунду
        # Кнопки управления
        pass