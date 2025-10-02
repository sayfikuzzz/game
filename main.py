from menu import Menu
from constants import *
import pygame
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.current_state = "menu"  # "menu" или "simulation"
        self.menu = Menu()
        self.simulation = None

    def run(self):
        running = True
        while running:
            if self.current_state == "menu":
                self.run_menu()
            else:
                self.run_simulation()

    def run_menu(self):
        pass

    def run_simulation(self):
        pass
g = Game()
g.run()
