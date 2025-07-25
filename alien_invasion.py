import sys
import pygame

from settings import Settings

class AlienInvasion:
    """
    Classe geral para gerenciar ativos e comportamento do jogo.
    """
    def __init__(self):
        """
        Inicializa o jogo e cria os recursos do jogo.
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """
        Inicia o loop principal do jogo.
        """
        while True:
            # Observa os eventos de mouse e teclado.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # limpa a tela durante casa passagem de loop
            self.screen.fill(self.settings.bg_color)
            
            # Torna o desenho de tela mais recente visível.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Cria uma instância e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()


# criando uma classe de configurações