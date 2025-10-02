import pygame
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pass

    def handle_event(self, event):
        pass


class Menu:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.percentage = 30.0
        self.buttons = []
        self.init_buttons()

    def init_buttons(self):
        """Создаёт кнопки для управления настройками"""
        # Кнопки для ширины: +50, +5, +1, -50, -5, -1
        # Кнопки для высоты: +50, +5, +1, -50, -5, -1
        # Кнопки для процента: +10, +1, +0.1, -10, -1, -0.1
        # Кнопка "Запуск симуляции"
        pass

    def handle_events(self, events):
        pass

    def draw(self, surface):
        pass