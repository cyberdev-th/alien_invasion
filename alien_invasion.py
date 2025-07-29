import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Classe geral para gerenciar ativos e comportamento do jogo.
    """
    def __init__(self):
        """
        Inicializa o jogo e cria os recursos do jogo.
        """
        pygame.init() # liga o motor do jogo
        self.clock = pygame.time.Clock() # cria um relógio para controlar a taxa de frames do jogo
        self.settings = Settings() # cria uma instância de configurações no jogo

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        """
        Inicia o loop principal do jogo.
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde a eventos de teclado e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Atualiza imagens na tela, e torna tudo visível."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()


