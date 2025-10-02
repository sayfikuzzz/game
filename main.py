import pygame
import sys
from constants import *
from grid import Grid


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

        # Создаем поле и заполняем случайно
        self.grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.grid.random_fill(INITIAL_PERCENTAGE)

        self.running = True
        self.paused = False
        self.generation = 0

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

    def draw_info(self):
        """Отрисовывает информацию о симуляции"""
        font = pygame.font.SysFont(None, 24)

        info_texts = [
            f"Поколение: {self.generation}",
            f"Размер: {self.grid.cols}x{self.grid.rows}",
            f"Заполненность: {INITIAL_PERCENTAGE}%",
            f"Состояние: {'Пауза' if self.paused else 'Запущено'}",
            "Пробел: пауза, R: перезапуск"
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
            self.draw_info()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()