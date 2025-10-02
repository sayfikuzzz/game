import pygame
import sys
import numpy as np
from constants import *
from grid import Grid


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game of Life - Numba Accelerated")
        self.clock = pygame.time.Clock()

        # Создаем поле и заполняем случайно
        self.grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.grid.random_fill(INITIAL_PERCENTAGE)

        self.running = True
        self.paused = True  # По умолчанию на паузе, чтобы можно было рисовать
        self.generation = 0
        self.drawing = False
        self.drawing_mode = 1  # 1 - рисовать живые, 0 - стирать
        self.fps_unlimited = False
        self.last_time = pygame.time.get_ticks()
        self.frame_count = 0
        self.current_fps = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    # Перезаполнить случайно
                    self.grid.random_fill(INITIAL_PERCENTAGE)
                    self.generation = 0
                elif event.key == pygame.K_c:
                    # Очистить поле
                    self.grid.grid = np.zeros((self.grid.rows, self.grid.cols), dtype=np.int32)
                    self.generation = 0
                elif event.key == pygame.K_1:
                    self.drawing_mode = 1  # Рисовать живые клетки
                elif event.key == pygame.K_0:
                    self.drawing_mode = 0  # Стирать клетки
                elif event.key == pygame.K_f:
                    self.fps_unlimited = not self.fps_unlimited  # Переключить FPS

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    self.drawing = True
                    self.draw_at_pos(event.pos)
                elif event.button == 3:  # Правая кнопка мыши
                    self.drawing_mode = 1 - self.drawing_mode  # Переключаем режим
                    self.draw_at_pos(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if self.drawing:
                    self.draw_at_pos(event.pos)

    def draw_at_pos(self, pos):
        """Рисует/стирает клетку в позиции курсора"""
        x, y = pos
        grid_x = y // self.grid.cell_size
        grid_y = x // self.grid.cell_size

        # Проверяем, что координаты в пределах поля
        if 0 <= grid_x < self.grid.rows and 0 <= grid_y < self.grid.cols:
            self.grid.grid[grid_x, grid_y] = self.drawing_mode

    def draw_grid(self):
        """Отрисовывает поле клеточек"""
        for x in range(self.grid.rows):
            for y in range(self.grid.cols):
                color = CELL_ALIVE if self.grid.grid[x, y] == 1 else CELL_DEAD
                rect = pygame.Rect(
                    y * self.grid.cell_size,
                    x * self.grid.cell_size,
                    self.grid.cell_size,
                    self.grid.cell_size
                )
                pygame.draw.rect(self.screen, color, rect)

    def update_fps_counter(self):
        """Обновляет счетчик FPS"""
        self.frame_count += 1
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 1000:  # Каждую секунду
            self.current_fps = self.frame_count
            self.frame_count = 0
            self.last_time = current_time

    def draw_info(self):
        """Отрисовывает информацию о симуляции"""
        font = pygame.font.SysFont(None, 24)

        current_percentage = self.grid.get_percentage()

        info_texts = [
            f"Поколение: {self.generation}",
            f"Размер: {self.grid.cols}x{self.grid.rows}",
            f"Заполненность: {current_percentage:.1f}%",
            f"FPS: {self.current_fps} ({'без ограничений' if self.fps_unlimited else '60'})",
            f"Состояние: {'Пауза' if self.paused else 'Запущено'}",
            f"Режим рисования: {'Живые (1)' if self.drawing_mode == 1 else 'Мёртвые (0)'}",
            "Пробел: пауза/запуск",
            "R: случайное заполнение",
            "C: очистить поле",
            "F: переключить FPS (60/без ограничений)",
            "1/0: переключить режим рисования",
            "ЛКМ: рисовать, ПКМ: переключить режим"
        ]

        for i, text in enumerate(info_texts):
            text_surface = font.render(text, True, TEXT)
            self.screen.blit(text_surface, (10, 10 + i * 25))

    def run(self):
        while self.running:
            self.handle_events()

            # Обновляем логику если не на паузе
            if not self.paused:
                self.grid.update()
                self.generation += 1

            # Отрисовка
            self.screen.fill(BACKGROUND)
            self.draw_grid()
            self.update_fps_counter()
            self.draw_info()

            pygame.display.flip()

            # Управление FPS
            if self.fps_unlimited:
                self.clock.tick()  # Без ограничений
            else:
                self.clock.tick(FPS)  # Ограничение 60 FPS

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()